# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/3 10:49

import random


# Generate 50 random numbers in 1000
def random_num():

    num = []
    for i in range(10):
        j = random.randint(0, 10000)
        num.append(j)
    print("Number before sorting:", num)
    return num
