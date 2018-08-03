# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 17:02


def selec_asc(num):

    length = len(num)

    for j in range(length - 1):
        min_index = j
        for i in range(j + 1, length):
            if num[i] < num[min_index]:
                min_index = i
        if num[j] != num[min_index]:
            num[j], num[min_index] = num[min_index], num[j]


def selec_desc(num):

    length = len(num)

    for j in range(length - 1):
        max_index = j
        for i in range(j + 1, length):
            if num[i] > num[max_index]:
                max_index = i
        if num[j] != num[max_index]:
            num[j], num[max_index] = num[max_index], num[j]

