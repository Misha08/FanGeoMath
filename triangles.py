from math import sqrt, sin, degrees, pi


# Help Functions

def get_sin():
    pass





# Formulas about Triangles


def check_exist_of_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise(ArithmeticError("This triangle does not exist,\n"
                              "please check the correctness of the entered data."))


# Formulas about Areas
def area_triangle_with_geron_formula(a, b, c):
    check_exist_of_triangle(a, b, c)
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def area_triangle_with_usual_formula(a, h):
    s = a * h * 0.5
    return s


# Formulas about Heights, Meridians, Bisectors
# Heights
def height_of_a_triangle_in_terms_of_area(s, side):
    h = s * 2 / side
    return h


def height_of_a_triangle_in_terms_of_side_and_angle(side, measure="grad", angle=0, sinus=0):
    if angle != 0:
        if measure == "grad":
            sinus = sin(degrees(angle))
        elif measure == "with pi":
            sinus = sin(angle)

    if sinus != 0:
        angle = ""









