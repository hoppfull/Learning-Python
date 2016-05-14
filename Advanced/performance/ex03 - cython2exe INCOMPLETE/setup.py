# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:49:53 2015

@author: Wilhelm
"""
import os
# import sys
import distutils.sysconfig as distconfig

include_dir = distconfig.get_python_inc()
library_dir = distconfig.BASE_PREFIX + "\\libs"  # Is this good code!?
# filename = sys.argv[1]

command = 'x86_64-w64-mingw32-gcc main.c' \
    + ' -I{include_dir}' \
    + '  -L{library_dir}' \
    + ' -lpython34.dll' \
    + ' -o main.exe' \
    + ' -D MS_WIN64' \
    + ' -municode' \
    + ' -fPIC'

os.system(command.format(include_dir=include_dir,
                         library_dir=library_dir))

# print(command.format(include_dir=include_dir,
#                     library_dir=library_dir))
