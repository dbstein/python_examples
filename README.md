# python_examples
Some basic python examples meant for the Biophysical Modeling group.

## What's in here?
1. 3D Laplace Kernel Computation Example (laplace_kernel.ipy)
2. Memory profiling examples
3. The package 'points', which implements a fast tree-based solution for finding which points in one point cloud are within some distance of another point cloud (but mostly is just here to demonstrate how to build a package)

## Requirements
You'll need an installation of python. I highly recommend installing [miniconda3](https://conda.io/miniconda.html), and then following these [instructions](https://software.intel.com/en-us/articles/using-intel-distribution-for-python-with-anaconda) in order to install a fast version of python 3 with good linkage.  After installing the core packages via those instructions, you'll want to install a few more things:
```bash
conda install ipython
conda install numexpr
conda install numba
conda install matplotlib
conda install pytest
```
That should do it.

## The 3D Laplace Kernel Computation Example
If you've done everything correctly, and have activated your virtual environment (source activate idp), then this should be pretty simple. First build the fortran extension:
```bash
f2py -m fortran_kernel -c kernel.f90
```
```bash
ipython laplace_kernel.ipy
```
Alternatively, open ipython and just copy and paste the code into the interpreter. Your timing results may vary from what was given in the presentation, based on the details of your machine.

## Line Profiling Examples
See the file profile_numexpr.ipy file.  Run by copy and pasting, or in bash:
```bash
ipython profile_numexpr.ipy
```


## Memory Profiling Examples
To generate a graphical comparison of memory usage for the numexpr and numba based Lapalce Kernels, run:
```bash
mprof run --interval 0.01 test_memory.py
mprof plot
mprof clean
```

## The points package
To install:
```bash
cd points
pip install .
```
You can test that the package worked correctly by running:
```bash
pytest
```
demo.ipy contains a basic demo.
