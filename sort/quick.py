# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 13:49


def quick_asc(num, start, end):

    if start >= end:
        return

    low = start
    high = end
    flag_value = num[low]

    while low < high:
        while low < high and num[high] >= flag_value:
            high = high - 1
        num[low] = num[high]

        while high > low and num[low] < flag_value:
            low = low + 1
        num[high] = num[low]

    num[low] = flag_value

    quick_asc(num, start, low - 1)
    quick_asc(num, low + 1, end)


def quick_desc(num, start, end):

    if start >= end:
        return

    low = start
    high = end
    flag_value = num[low]

    while low < high:
        while low < high and num[high] < flag_value:
            high = high - 1
        num[low] = num[high]

        while high > low and num[low] >= flag_value:
            low = low + 1
        num[high] = num[low]

    num[low] = flag_value

    quick_desc(num, start, low - 1)
    quick_desc(num, low + 1, end)

