#!/usr/bin/env python3


'''A module that concatenates two strings'''


def concat(str1: str, str2: str) -> str:
    '''A function that concatenates 2 strings'''
    return str1 + str2


if __name__ == '__main__':

    str1 = 'fatuma'
    str2 = 'yattani'

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
