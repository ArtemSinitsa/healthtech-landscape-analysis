import numpy as np

def bezier_curve(points, num=100):
    t = np.linspace(0, 1, num)
    p0, p1, p2 = points
    curve = (1 - t)[:, None]**2 * p0 + 2*(1 - t)[:, None]*t[:, None]*p1 + t[:, None]**2 * p2
    return curve
