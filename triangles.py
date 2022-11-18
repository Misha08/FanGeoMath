from math import sqrt, sin, degrees, asin, cos


# Help Functions

def get_semi_perimeter(side1=0, side2=0, side3=0):
    p = (side1 + side2 + side3) / 2
    return p


def get_sinus(angle):
    sinus = sin(degrees(angle))
    return sinus


def get_cosinus(angle):
    cosinus = cos(degrees(angle))
    return cosinus


# Formulas about Triangles
def check_exist_of_triangle(side1=0, side2=0, side3=0):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise(ArithmeticError("This triangle does not exist,\n"
                              "please check the correctness of the entered data."))


# Formulas about Areas
def area_triangle_with_geron_formula(side1=0, side2=0, side3=0):
    check_exist_of_triangle(side1, side2, side3)
    p = (side1 + side2 + side3) / 2
    s = sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return s


def area_triangle_with_usual_formula(side=0, h=0):
    s = side * h * 0.5
    return s


# Formulas about Heights, Meridians, Bisectors
# Heights
def height_in_terms_of_area_and_side(s, side):
    h = s * 2 / side
    return h


def height_in_terms_of_side_and_angle(side, measure="grad", angle=0, sinus=0):
    if angle != 0:
        if measure == "grad":
            sinus = get_sinus(angle)
        elif measure == "with pi":
            sinus = sin(angle)

    if sinus != 0:
        # For some further help
        angle = asin(sinus)

    height = side * sinus

    return height


def height__in_terms_of_side_and_area(side, s=0):
    height = (2 * s) / side
    return height


def height__ittsa_radius_of_the_circumscribed_circle(side1=0, side2=0, r=1):
    height = (side1 * side2) / (r * 2)
    return height


# Medians
def median_in_terms_of_sides(side1=0, side2=0, side3=0):
    m = 0.5 * sqrt(2 * side2 ** 2 + side3 ** 2 - 2 * side1 ** 2)
    return m


# Bisectors
def bisector_of_a_triangle_in_terms_of_sides(side1=0, side2=0, side3=0):
    p = get_semi_perimeter(side1, side2, side3)
    m = 2 * sqrt(side2 * side3 * p * (p - side1)) / (side2 + side3)
    return m


def bisector_of_a_triangle_in_terms_of_sides_and_angle(side2=0, side3=0, angle=0):
    l_of_side1 = 2 * side2 * side3 * get_cosinus(angle / 2) / side2 + side3
    return l_of_side1


