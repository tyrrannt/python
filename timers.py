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
import time


def timers(func):
    def origin_func(num):
        start = time.time()
        func(num)
        stop = time.time()
        print(f"Время на выполнение {stop - start}")
    return origin_func

dict = {'321': 332211, '123': 112233}
for keys in dict:
    print(keys)
    print(dict[keys])