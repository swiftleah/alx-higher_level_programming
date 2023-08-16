#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight_sum = 0
    total = 0

    for score, weight in my_list:
        total_weight_sum += score * weight
        total += weight

    if total == 0:
        return 0

    weighted_avg = total_weight_sum / total
    return weighted_avg
