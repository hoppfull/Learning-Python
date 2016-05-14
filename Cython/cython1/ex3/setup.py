from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [Extension(#these arguments are named so I can enter them in any order as long as I name them
	sources = ["src//*.pyx"], #where to find the files to compile, I use two slashes becouse I believe unix systems require them. Good practice, I guess.
	name = "*", #This is supposed to be the name of the program but if I put anything other than an asterisk, I get errors
	include_dirs = [np.get_include()] #This gives a directory to where to find numpy header files for compiler
# extension_keywords
					  # 'name', 'sources', 'include_dirs', define_macros', 'undef_macros', 'library_dirs', 'libraries', 'runtime_library_dirs',
                      # 'extra_objects', 'extra_compile_args', 'extra_link_args', 'swig_opts', 'export_symbols', 'depends', 'language'
)]

setup(
	ext_modules = cythonize(extensions),
	script_args = ["build_ext", "--compiler=mingw32", "--inplace"] #This line here took forever to figure out. But I finally did it! Yeeeeehaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!
# setup_keywords
				  # 'distclass', 'script_name', 'script_args', 'options', 'name', 'version', 'author', 'author_email', 'maintainer', 'maintainer_email', 'url', 'license',
                  # 'description', 'long_description', 'keywords', 'platforms', 'classifiers', 'download_url', 'requires', 'provides', 'obsoletes'
)