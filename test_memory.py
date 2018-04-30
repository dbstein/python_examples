import numpy as np
from numexpr_kernel import numexpr_kernel
from numba_kernel import numba_kernel

N = 10000
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)
tau = np.random.rand(N)

r1 = numexpr_kernel(x, y, z, tau)
r1 = numexpr_kernel(x, y, z, tau)
r2 = np.zeros(N, dtype=float)
numba_kernel(x, y, z, tau, r2, N)
numba_kernel(x, y, z, tau, r2, N)
