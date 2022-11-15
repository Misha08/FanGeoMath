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


# displays welcome text
def print_maintext():
    print("/*------------------------------------------------------------*/")
    print("                          Hello User!!")
    print("In this program, you can play with the areas of different shapes")
    print("                 and even draw in the console!")
    print("/*------------------------------------------------------------*/")


# MainFunc
def main():
    if get_info_from_document(open_text_document(doc_name))[1] == "true":
        print_maintext()
        write_text_to_document(open_text_document(doc_name))
    else:
        print("Good bye")


    print("\n" * 4)
    print(area_triangle_with_geron_formula(4, 2, 3))


# Entry point
if __name__ == "__main__":
    main()
    sys.exit(0)
