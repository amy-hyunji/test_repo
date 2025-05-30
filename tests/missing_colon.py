#!/usr/bin/env python3

from test_tribonaccy import test_tribonacci

def add(a, b):
    test_tribonacci()
    return a+b
def division(a: float, b: float):
    while b > 0:
       add(a, b)
       b-= 1
    return a


if __name__ == "__main__":
    print(division(123, 15))

