#  3D Health Landscape with Clustering, Nonlinear Surfaces & Advanced Statistics

This project visualizes a simulated health-related dataset using advanced 3D statistical techniques.
This project combines advanced multivariate statistics, geometric topology, and interactive 3D visualization to explore complex health datasets and ecological influences.

 UMAP-based dimensionality reduction  
 Nonlinear regression surface approximation  
 Geometric cluster highlighting (spheres, cubes)  
 Bezier-curve multivariate correlation visualization  
 Risk score gradient with high-fidelity rendering  
&
- Synthetic or real-world health data generation
- Multidimensional clustering & correlation analysis
- Topological data visualization with spheres, wireframe cubes, and curved connections
- Nonlinear regression surface fitting
- Integration-ready for ecological or environmental datasets
- High-resolution publication-ready figures


---

##   Project Structure

health-landscape-analysis/
├── src/
│ ├── data_generation.py # Data simulation
│ ├── statistics.py # Statistical models (regression)
│ ├── utils.py # Bezier curves & helpers
│ ├── visualization.py # 3D Plotly visualization
├── main.py # Project execution
└── README.md # Project documentation

 

---

##  Requirements

- Python 3.8+
- numpy
- pandas
- plotly
- scikit-learn
- umap-learn

---


 ## Mathematical Foundations

### 1. Dimensionality Reduction with UMAP

We reduce the original feature space \( \mathbf{X} \in \mathbb{R}^n \) to a 3-dimensional embedding \( \mathbf{Y} \in \mathbb{R}^3 \):

$$
\mathbf{Y} = \text{UMAP}(\mathbf{X})
$$

UMAP preserves local and global data structure for meaningful clustering.

---

### 2. Nonlinear Surface Fitting with Polynomial Regression

We model the relationship between coordinates \( (x, y) \) and the target \( z \) using a polynomial of degree 3:

$$
z = f(x,y) = \sum_{i=0}^{3} \sum_{j=0}^{3-i} a_{ij} x^i y^j
$$

The coefficients \( a_{ij} \) are estimated robustly using RANSAC regression to reduce the influence of outliers.

---

### 3. Correlation Visualization Using Quadratic Bezier Curves

Clusters centers \( P_0, P_2 \in \mathbb{R}^3 \) are connected by a smooth curve defined as:

$$
B(t) = (1 - t)^2 P_0 + 2(1 - t) t P_1 + t^2 P_2, \quad t \in [0,1]
$$

where \( P_1 \) is the control point elevated in 3D space to create a visually appealing curved connection.

---


##  Example Visualization

<img width="858" alt="3D landscape" src="https://github.com/user-attachments/assets/d006abf1-7dad-41f4-aa52-d325bafda366" />


This preserves both local and global structure ideal for cluster identification.

--- 
---

##  Scientific Report

You can find the corresponding research paper, edit it collaboratively via Overleaf:
[Overleaf Project]([https://www.overleaf.com/read/XYZ-YOUR-LINK](https://www.overleaf.com/read/qtfbdwknkxjp#bcf527))

##   Author
Artem V. Sinitsa, PhD
Research Fellow in Computational Modeling & AI-driven Digital Twin Systems
SISSA – International School for Advanced Studies
✉️ artem.sinitsa@sissa.it | asinitsa@sissa.it
---

##   Quick Start

```bash
git clone https://github.com/YourUsername/health-landscape-analysis.git
cd health-landscape-analysis
pip install -r requirements.txt

python main.py

