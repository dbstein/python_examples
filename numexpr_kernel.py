import numpy as np
import numexpr as ne

@profile
def numexpr_kernel(x, y, z, tau):
    scale = 1.0/(4*np.pi)
    xT = x[:,None]
    yT = y[:,None]
    zT = z[:,None]
    D = ne.evaluate('1.0/sqrt((x-xT)**2 + (y-yT)**2 + (z-zT)**2)')
    np.fill_diagonal(D, 0.0)
    out = scale*np.dot(D, tau)
    del D
    return out
