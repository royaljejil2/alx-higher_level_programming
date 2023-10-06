#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    jey = sorted(a_dictionary)
    for i in jey:
        print("{}: {}".format(i, a_dictionary[i]))
