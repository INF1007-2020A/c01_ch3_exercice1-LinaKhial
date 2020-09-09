#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def square_root(number: int) -> float:
    # TODO completer la fonction
     try:
        math.sqrt(number)
   
    return math.sqrt(number)


def square(number: int) -> int:
    # TODO completer la fonction
    return (number * number)


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
