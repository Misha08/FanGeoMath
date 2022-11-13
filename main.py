# -*- coding: UTF-8 -*-

'''

The program is implemented without the use of OOP and is still under development!
Works on Python versions 3.0 and above

'''


import sys
from triangles import area_triangle_with_geron_formula


# displays welcome text
def print_maintext():
    print("/*------------------------------------------------------------*/")
    print("                          Hello User!!")
    print("In this program, you can play with the areas of different shapes")
    print("                 and even draw in the console!")
    print("/*------------------------------------------------------------*/")


# MainFunc
def main():
    print(area_triangle_with_geron_formula(4, 2, 3))


# Entry point
if __name__ == "__main__":
    print_maintext()
    print("\n" * 4)
    main()
    sys.exit(0)
