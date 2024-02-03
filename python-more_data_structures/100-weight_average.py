#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight = sum([row[1] for row in my_list])
    score = sum(list(map(lambda x: x[0] * x[1], my_list)))
    return (score / weight)
