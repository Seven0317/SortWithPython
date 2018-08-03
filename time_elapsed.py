# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 11:02

from sort.bubble import bubble_asc, bubble_desc
from sort.insert import insert_asc, insert_desc
from sort.quick import quick_asc, quick_desc
from sort.selection import selec_asc, selec_desc
from sort.shell import shell_asc, shell_desc

from random_num import random_num
import time


def time_elapsed(sort):

    num = random_num()

    if "quick" in sort.__name__:
        t_start = time.time()
        sort(num, 0, len(num) - 1)
        t_end = time.time()
        t_elapsed = t_end - t_start
    else:
        t_start = time.time()
        sort(num)
        t_end = time.time()
        t_elapsed = t_end - t_start

    print("Number after sorting of %s:" % sort.__name__, num)
    print("Elapsed time of %s sort is %f s" % (sort.__name__, t_elapsed))


if __name__ == '__main__':
    time_elapsed(bubble_asc)

