# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   作  者：     Johnny
   描  述：
   日  期：     2018/8/22
-------------------------------------------------
   变更历史:
   2018/8/22 16:48:新建
-------------------------------------------------
"""

__author__ = 'Johnny'

to_print_str = "人生苦短，我用Python！"
index = 0
str_len = len(to_print_str)

while index < str_len:
    print(to_print_str[index], end="  ")
    index += 1
