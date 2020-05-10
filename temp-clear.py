#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

__author__ = "Vitalii R. Shakirov"
__copyright__ = "Copyright 2020"
__credits__ = ["", ]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vitalii R. Shakirov"
__email__ = "shakirov.vitaliy@gmail.com"
__status__ = "Production"

import os, shutil

path = 'C:\\Users'
my_list = os.listdir(path)
my_list2 = []
for i in my_list:
    my_list2.append(path + '\\' + i + '\\AppData\\Local\\Temp\\')

for j in my_list2:
    for root, dirs, files in os.walk(j):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except OSError as e:
                print("Ошибка: %s : %s" % (os.path.join(root, name), e.strerror))
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError as e:
                print("Ошибка: %s : %s" % (os.path.join(root, name), e.strerror))
