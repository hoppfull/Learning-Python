from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

##Basic Setup to use with numpy. To run setup simply enter "python setup.py" in console

extensions = [Extension(
	sources = ["src//*.pyx"],
	name = "*",
	include_dirs = [np.get_include()]
	)]

setup(
	ext_modules = cythonize(extensions),
	script_args = ["build_ext", "--compiler=mingw32", "--inplace"]
	)