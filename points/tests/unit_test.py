import numpy as np
import points

n = 200

# get a grid
v = np.linspace(-1, 1, n)
x, y = np.meshgrid(v, v, indexing='ij')

# get a boundary
theta = np.linspace(0, 2*np.pi, n, endpoint=False)
bx = 0.5*np.cos(theta)
by = 0.5*np.sin(theta)

pg = points.points(x, y)
pb = points.points(bx, by)

close_pg1 = pb.near_points_slow(pg, 0.02)
close_pg2 = pb.near_points(pg, 0.02)

# test whether the fast and slow give the same result
def test_fast_and_slow_same():
    assert np.allclose(close_pg1, close_pg2)
