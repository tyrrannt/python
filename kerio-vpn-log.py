#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Создает csv файл из логов Kerio
"""

__author__ = "Vitalii R. Shakirov"
__copyright__ = "Copyright 2020"
__credits__ = ["", ]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vitalii R. Shakirov"
__email__ = "shakirov.vitaliy@gmail.com"
__status__ = "Production"
import re
dict = {'Barkol.comp142': "Barkol;Шакиров В.Р.", 'Barkol.comp81': "Barkol;Хабаров М.В.", } #'Barkol.comp': "Barkol;"
res_list = []
with open('dial.log.txt', 'r+') as fd:
    for i in fd:
       res = ''
       res = re.search(r' connected', i, re.M | re.I)
       if not res:
            res = re.sub(r" IPsec VPN client '", ';', i, re.M | re.I)
            res = re.sub(r"' disconnected from ", ';', res, re.M | re.I)
            res = re.sub(r", connection time ", ';', res, re.M | re.I)
            res = re.sub(r" \d\d:\d\d:\d\d]", '', res, re.M | re.I)
            res = re.sub(r"\[", '', res, re.M | re.I)
            res = re.sub(r"/", '.', res, re.M | re.I)
            for j in dict:
                res = re.sub(j, dict.get(j), res, re.M | re.I)
            #res = re.sub(r"Barkol.", 'Barkol;', res, re.M | re.I)
            #res = re.sub(r"Complang.", 'Complang;', res, re.M | re.I)
            res_list.append(res)
            print(res)
with open('dial.log.csv', 'a') as fd:
    for i in res_list:
        fd.write(i)