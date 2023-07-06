#!/usr/bin/env python3


'''A module that returns the whole number from a float input'''


def floor(n: float) -> int:
    '''a function that reduces a float to an integer'''
    return int(n)


if __name__ == '__main__':
    import math

    ans = floor(3.14)

    print(floor(3.14))
    print(floor(42.7))
    print(floor(99.9))
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
