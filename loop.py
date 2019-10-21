#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program asks the user for a positive integer,
#  then add all the whole numbers up to that number


def main():
    # This function asks the user for a positive integer,
    #  then add all the whole numbers up to that number
    number = input("enter a number: ")
    result = 0
    x = 1  # Doesn’t matter if it is 0 or 1
    try:
        number = int(number)
        while x <= number:
            result = x + result
            x += 1
        print(result)
    except(Exception):
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
