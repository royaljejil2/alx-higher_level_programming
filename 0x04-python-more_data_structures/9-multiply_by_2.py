#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for m, n in new_dict.items():
        new_dict[m] = n * 2
    return new_dict
