import numpy as np
import pandas as pd

def generate_data(seed=42):
    np.random.seed(seed)
    groups = ['Low Risk', 'Medium Risk', 'High Risk']
    sizes = [150, 150, 150]
    data, labels = [], []
    
    for i, size in enumerate(sizes):
        base = np.array([i*5, i*3, i*2])
        cluster = base + np.random.randn(size, 3)
        data.append(cluster)
        labels += [groups[i]] * size
    
    df = pd.DataFrame(np.vstack(data), columns=['Feature1', 'Feature2', 'Feature3'])
    df['Group'] = labels
    df['RiskScore'] = np.linspace(0, 1, len(df)) + np.random.normal(0, 0.1, len(df))
    
    return df
