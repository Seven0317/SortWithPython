# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 10:32


# Bubble sort ascending
def bubble_asc(num):

    for j in range(len(num)-1, 0, -1):
        for i in range(j):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]


# Bubble sort descending
def bubble_desc(num):

    for j in range(len(num)-1, 0, -1):
        for i in range(j):
            if num[i] < num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]

