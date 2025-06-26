import plotly.graph_objects as go
import numpy as np
import umap
from src.statistics import nonlinear_surface_fit
from src.utils import bezier_curve

def plot_visualization(df):
    
    reducer = umap.UMAP(n_components=3, random_state=42)
    embedding = reducer.fit_transform(df[['Feature1', 'Feature2', 'Feature3']])
    df[['DimX', 'DimY', 'DimZ']] = embedding
    
    fig = go.Figure()
    colors = {'Low Risk': 'green', 'Medium Risk': 'orange', 'High Risk': 'red'}
    
    for group in df['Group'].unique():
        dfg = df[df['Group'] == group]
        fig.add_trace(go.Scatter3d(
            x=dfg['DimX'], y=dfg['DimY'], z=dfg['DimZ'],
            mode='markers',
            marker=dict(size=6, color=dfg['RiskScore'], colorscale='Viridis',
                        cmin=0, cmax=1, colorbar=dict(title='Risk Score'),
                        opacity=0.9, line=dict(width=0.5, color='DarkSlateGrey')),
            name=f'Patients {group}',
            text=[f'Group: {group}<br>Risk Score: {rs:.2f}' for rs in dfg['RiskScore']],
            hoverinfo='text'
        ))
    
    # Nonlinear Surface
    X = df[['DimX', 'DimY']].values
    y = df['DimZ'].values
    model = nonlinear_surface_fit(X, y)
    x_lin = np.linspace(X[:,0].min(), X[:,0].max(), 40)
    y_lin = np.linspace(X[:,1].min(), X[:,1].max(), 40)
    xx, yy = np.meshgrid(x_lin, y_lin)
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    
    fig.add_trace(go.Surface(x=xx, y=yy, z=zz, colorscale='Viridis', opacity=0.5, showscale=False, name='Nonlinear Surface Fit'))
    
    # Cluster Spheres & Cubes
    cluster_centers = df.groupby('Group')[['DimX', 'DimY', 'DimZ', 'RiskScore']].mean()
    
    for group, row in cluster_centers.iterrows():
        # Sphere
        u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
        r = 0.35
        x_sphere = r*np.cos(u)*np.sin(v) + row['DimX']
        y_sphere = r*np.sin(u)*np.sin(v) + row['DimY']
        z_sphere = r*np.cos(v) + row['DimZ']
        fig.add_trace(go.Surface(
            x=x_sphere, y=y_sphere, z=z_sphere,
            opacity=0.2, showscale=False,
            colorscale=[[0, colors[group]], [1, colors[group]]],
            name=f'Sphere Cluster {group}', hoverinfo='skip', showlegend=True
        ))
        
        # Cube
        s = 0.6
        x, y_, z = [row['DimX'] - s/2, row['DimX'] + s/2], [row['DimY'] - s/2, row['DimY'] + s/2], [row['DimZ'] - s/2, row['DimZ'] + s/2]
        Xc, Yc, Zc = np.meshgrid(x, y_, z)
        fig.add_trace(go.Scatter3d(
            x=Xc.flatten(), y=Yc.flatten(), z=Zc.flatten(),
            mode='markers', marker=dict(size=2, color=colors[group]),
            name=f'Cube Cluster {group}', showlegend=False
        ))
        
        # Text label
        fig.add_trace(go.Scatter3d(
            x=[row['DimX']], y=[row['DimY']], z=[row['DimZ'] + 0.6],
            mode='text', text=[f"{group}<br>Avg Risk: {row['RiskScore']:.2f}"],
            showlegend=False, textfont=dict(color=colors[group], size=14)
        ))
    
    # Correlation Bezier Curves
    centers = cluster_centers[['DimX', 'DimY', 'DimZ']].values
    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            curve = bezier_curve([centers[i], (centers[i] + centers[j]) / 2 + np.array([0, 0, 1.0]), centers[j]], num=80)
            fig.add_trace(go.Scatter3d(
                x=curve[:,0], y=curve[:,1], z=curve[:,2],
                mode='lines', line=dict(color='purple', width=3, dash='dash'),
                name=f'Correlation {i}-{j}'
            ))
    
    # Layout
    fig.update_layout(
        title="<b>3D Statistical Health Landscape with Clusters & Correlations</b><br>Simulated Dataset: 450 Patients",
        scene=dict(
            xaxis=dict(title='Risk Index', backgroundcolor='rgb(245,245,245)', showbackground=True),
            yaxis=dict(title='Metabolic Health (mg/dL)', backgroundcolor='rgb(245,245,245)', showbackground=True),
            zaxis=dict(title='Environmental Stress', backgroundcolor='rgb(245,245,245)', showbackground=True),
            bgcolor='white'
        ),
        margin=dict(l=0, r=250, b=0, t=120),
        height=800, width=1150
    )
    
    fig.show()
