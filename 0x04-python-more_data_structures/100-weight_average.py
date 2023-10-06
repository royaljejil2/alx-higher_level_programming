#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    jey = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        jey += tup[1]

    return (num / jey)
