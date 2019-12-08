#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates the largest number in a list.

import random


def largest_number(random_list):
    # this function returns the largest number
    largest_random = 0

    for loop_counter in range(0, len(random_list)):
        if random_list[loop_counter] > largest_random:
            largest_random = random_list[loop_counter]

    return largest_random


def main():
    # this function calculates the average of randomized numbers

    list_random = []

    # input
    print("The randomized numbers are:")
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        list_random.append(random_number)
        print("{0}, ".format(random_number), end="")
    print("")

    large = largest_number(list_random)

    print("The largest number of all numbers is {0}".format(large))


if __name__ == "__main__":
    main()
