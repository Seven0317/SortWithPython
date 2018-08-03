# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 18:50


def insert_asc(num):

    length = len(num)
    for j in range(1, length):
        for i in range(j, 0, -1):
            if num[i] < num[i-1]:
                num[i], num[i-1] = num[i-1], num[i]


def insert_desc(num):

    length = len(num)
    for j in range(1, length):
        for i in range(j, 0, -1):
            if num[i] > num[i-1]:
                num[i], num[i-1] = num[i-1], num[i]

