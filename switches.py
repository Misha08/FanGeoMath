from triangles import *

# Help functions
def get_choose():
    choose = int(input())
    return choose


def open_text_document(doc_name):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()

    return doc


def get_info_from_document(doc):
    info = doc.split(":")
    return info


def write_text_to_document(doc_name):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()
        rw_file.write(doc.split(":")[0] + "False")


# Analogues of the expression "switch - case"
def switch_1(choice):
    if choice == 1:
        print("***********Areas**********")
        print("1 - with the Geron formula")
        print("2 - with usual formula")
        switch_2_areas(get_choose())

    elif choice == 2:
        print("*************************Heights************************")
        print("1 - with the Area and the Side")
        print("2 - with the Side and the Angle")
        print("3 - with the Area and the Angle")
        print("4 - with the Side and Radius of the Circumscribed Circle")
        # switch_2_1(get_choose())

    elif choice == 3:
        print("*********Medians*********")
        print("Medians with Sides")
        # switch_2_1(get_choose())

    elif choice == 4:
        print("***********Bisectors**********")
        print("1 - with the Sides")
        print("2 - with the Sides ang the Angle")
        # switch_2_1(get_choose())
    else:
        return 0


def switch_2_areas(choice):
    if choice == 1:
        print("Please, Enter the lengths of the sides", "\n")
        side1 = int(input("Enter the length of first side: "))
        side2 = int(input("Enter the length of second side: "))
        side3 = int(input("Enter the length of third side: "))
        print(area_triangle_with_geron_formula(side1, side2, side3))

    elif choice == 2:
        print("Please, Enter the lengths of the side and the height", "\n")
        side = int(input("Enter the length of the side: "))
        height = int(input("Enter the length of the height: "))
        print(area_triangle_with_usual_formula(side, height))


def switch_2_heights(value):
    print("")

