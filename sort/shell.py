# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 19:32


def shell_asc(num):

    length = len(num)
    gap = length // 2

    while gap > 0:
        for j in range(gap, length):
            i = j
            while i >= gap and num[i] < num[i-gap]:
                num[i], num[i-gap] = num[i-gap], num[i]
                i = i - gap
        gap = gap // 2


def shell_desc(num):

    length = len(num)
    gap = length // 2

    while gap > 0:
        for j in range(gap, length):
            i = j
            while i >= gap and num[i] > num[i-gap]:
                num[i], num[i-gap] = num[i-gap], num[i]
                i = i - gap
        gap = gap // 2
