from triangles import *


# Help functions
# Provides a choice a Method for Calculating Certain Values
def get_choice():
    choice = int(input("Enter your choice: "))
    return choice


# Open the text files with switch parameters
def open_text_document(doc_name):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()

    return doc


# Get information about the switch status of functions
def get_info_from_document(doc):
    info = doc.split(":")
    return info


# Write information only in the document about the switch status of functions
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
        switch_2_areas(get_choice())

    elif choice == 2:
        print("*************************Heights************************")
        print("1 - with the Area and the Side")
        print("2 - with the Side and the Angle")
        print("3 - with the Side and the Area")
        print("4 - with the Side and Radius of the Circumscribed Circle")
        switch_2_heights(get_choice())

    elif choice == 3:
        print("*********Medians*********")
        print("Medians with Sides")
        switch_2_medians()

    elif choice == 4:
        print("***********Bisectors**********")
        print("1 - with the Sides")
        print("2 - with the Sides ang the Angle")
        switch_2_bisectors(get_choice())
    else:
        return 0


# The Functions to switch a method to calculation of quantities
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

    else:
        raise ValueError("you must have entered a valid value")


def switch_2_heights(choice):
    if choice == 1:
        print("Please, Enter the length of the Side and measure of the Area", "\n")
        side = int(input("Enter the length of the side: "))
        area = int(input("Enter the Area"))
        print(height_in_terms_of_area_and_side(area, side))

    elif choice == 2:
        print("Please, Enter the length of the side and degree measure of the angle", "\n")
        side = int(input("Enter the length of the side: "))
        angle = int(input("Enter degree measure of the angle: "))
        print(height_in_terms_of_side_and_angle(side, "grad", angle))

    elif choice == 3:
        print("Please, Enter the length of the side and measure of the area", "\n")
        s = int(input("Enter the length of the area: "))
        side = int(input("Enter degree measure of the side: "))
        print(height__in_terms_of_side_and_area(side, s))

    elif choice == 4:
        print("Please, Enter the lengths of the sides and the radius", "\n")
        side1 = int(input("Enter the length of the first side: "))
        side2 = int(input("Enter the length of the second side: "))
        radius = int(input("Enter the length of the radius of the circumscribed circle"))
        print(height__ittsa_radius_of_the_circumscribed_circle(side1, side2, radius))

    else:
        raise ValueError("you must have entered a valid value")


def switch_2_medians():
    print("Please, Enter the lengths of the sides", "\n")
    side1 = int(input("Enter the length of first side: "))
    side2 = int(input("Enter the length of second side: "))
    side3 = int(input("Enter the length of third side: "))
    print(median_in_terms_of_sides(side1, side2, side3))


def switch_2_bisectors(choice):
    if choice == 1:
        print("Please, Enter the lengths of the sides", "\n")
        side1 = int(input("Enter the length of first side: "))
        side2 = int(input("Enter the length of second side: "))
        side3 = int(input("Enter the length of third side: "))
        print(bisector_of_a_triangle_in_terms_of_sides(side1, side2, side3))

    elif choice == 2:
        print("Please, Enter the lengths of the sides and the degree measure of the angle", "\n")
        side2 = int(input("Enter the length of second side: "))
        side3 = int(input("Enter the length of third side: "))
        angle = int(input("Enter degree measure of the angle: "))
        print(bisector_of_a_triangle_in_terms_of_sides_and_angle(side2, side3, angle))

    else:
        raise ValueError("you must have entered a valid value")
