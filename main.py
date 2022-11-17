# -*- coding: UTF-8 -*-

'''

The program is implemented without the use of OOP and is still under development!
Works on Python versions 3.0 and above

'''


import sys
from triangles import *
from switches import open_text_document, get_info_from_document, write_text_to_document

# Parameters
doc_name = "Switches.txt"

# Help functions
# Displays welcome text
def print_maintext():
    print("/*------------------------------------------------------------*/")
    print("                          Hello User!!")
    print("In this program, you can play with the areas of different shapes")
    print("                 and even draw in the console!")
    print("/*------------------------------------------------------------*/")


# Analogues of the expression "switch - case"
def switch_1(value):
    if value == 1:
        return 1
    elif value == 2:
        return 2
    elif value == 3:
        return 3
    elif value == 4:
        return 4
    else:
        return 0


def switch_2(value):
    if value == 1:
        return 1
    elif value == 2:
        return 2
    elif value == 3:
        return 3
    elif value == 4:
        return 4


# MainFunc
def main():
    if get_info_from_document(open_text_document(doc_name))[1] == "true":
        print_maintext()
        print("\n" * 4)
        write_text_to_document(doc_name)

    print("1 - area")
    print("2 - height")
    print("3 - medians")
    print("4 - bisectors")

    choose = int(input("what will you choose?: "))
    switch_1(choose)


# Entry point
if __name__ == "__main__":
    main()
    sys.exit(0)



