import numpy as np
import scipy as sp
import scipy.spatial

def near_points(px, qx, r, pxtree=None, qxtree=None):
    """
    Finds points in qx that are within a distance r of any point in px
    Parameters:
        px, required, float(np, dim), coordinates of px
        qx, required, float(nq, dim), coordinates of py
        r,  required, float,          radius of closeness
        pxtree, optional, cKDTree, tree for px, makes computation more efficient
        qxtree, optional, cKDTree, tree for qx, makes computation more efficient
    Returns:
        Tuple of:
            bool, of length (nq), with True denoting a close point
            pxtree,
            qxtree,
    """
    if pxtree is None:
        pxtree = sp.spatial.cKDTree(px, balanced_tree=False)
    if qxtree is None:
        qxtree = sp.spatial.cKDTree(qx, balanced_tree=False)
    groups = pxtree.query_ball_tree(qxtree, r)  
    out = np.zeros(qx.shape[0], dtype=bool)
    for group in groups:
        out[np.array(group)] = True
    return out, pxtree, qxtree

class points(object):
    """
    Class to represent a point collection in 2D
    """
    def __init__(self, x, y):
        """
        Initialize a point collection in 2D
        Parameters:
            x, required, float(*), x coordinates of points
            y, required, float(*), y coordinates of points
        """
        self.x = x
        self.y = y
        self.X = np.column_stack([self.x.flatten(), self.y.flatten()])
    def near_points_slow(self, p, r):
        """
        Return an array with which points in p are within a distance r of any
        point in self
        Parameters:
            points, required, class(points), points to check for close points
            r,      required, float,         radius of closeness
        """
        dx = self.x.flatten() - p.x.flatten()[:,None]
        dy = self.y.flatten() - p.y.flatten()[:,None]
        d2 = dx**2 + dy**2
        min_d2 = np.min(d2, 1)
        close = min_d2 < r**2
        return close.reshape(p.x.shape)
    def compute_tree(self):
        self.tree = sp.spatial.cKDTree(self.X)
    def near_points_fast(self, p, r):
        if not hasattr(p, 'tree'):
            p.compute_tree()
        if not hasattr(self, 'tree'):
            self.compute_tree()
        groups = self.tree.query_ball_tree(p.tree, r)
        out = np.zeros(np.prod(p.x.shape))
        for group in groups:
            out[np.array(group)] = 1.0
        return out.astype(bool).reshape(p.x.shape)
    def near_points(self, p, r):
        has_ptree = hasattr(p, 'tree')
        has_stree = hasattr(self, 'tree')
        ptree = p.tree if has_ptree else None
        stree = self.tree if has_stree else None
        close, stree, ptree = near_points(self.X, p.X, r, stree, ptree)
        if not has_ptree:
            p.tree = ptree
        if not has_stree:
            self.tree = stree
        return close.reshape(p.x.shape)


