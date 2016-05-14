from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [Extension("*", ["*.pyx"])]	#This line tells to load all .pyx files in same directory

setup(
	name = "my Hello world program",	#Don't know what this does to be honest...
	ext_modules = cythonize(extensions) #This starts the compilation process
)