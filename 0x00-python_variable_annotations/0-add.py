#!/usr/bin/env python3

'''An Python module designed to provide the sum of two decimal numbers'''


def add(a: float, b: float) -> float:
    '''A function that calculates and outputs the sum of two floating-point numbers'''
    return a + b


if __name__ == '__main__':

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__
