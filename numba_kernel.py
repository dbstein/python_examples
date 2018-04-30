import numpy as np
from numba import njit, prange

@profile
@njit(parallel=True)
def numba_kernel(x, y, z, tau, out, N):
    scale = 1.0/(4.0*np.pi)
    for i in prange(N):
        for j in range(i):
            out[i] += tau[j]*np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2)
        for j in range(i+1,N):
            out[i] += tau[j]/np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2)
    for i in range(N):
        out[i] *= scale
