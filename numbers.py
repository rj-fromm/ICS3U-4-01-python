#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Sept 2019
# This program adds many numbers together


def main():

    number = int(input("Please enter a number : "))

    number1 = number

    counter = 0

    total = 0

    while counter != number1:

        number = number + counter

        counter = counter + 1

        total = number

        print("{0}".format(total))


if __name__ == "__main__":
    main()
