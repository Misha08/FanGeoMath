from math import sqrt, sin, asin, cos, radians


# Help Functions
def check_exist_of_triangle(side1=0, side2=0, side3=0):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise(ArithmeticError("This triangle does not exist,\n"
                              "please check the correctness of the entered data."))


def get_semi_perimeter(side1=0, side2=0, side3=0):
    semi_perimeter = (side1 + side2 + side3) / 2
    return semi_perimeter


def get_sinus(angle):
    sinus = round(sin(radians(angle)), 4)
    return sinus


def get_cosinus(angle):
    cosinus = round(cos(radians(angle)), 4)
    return cosinus


# Formulas about Triangles
# Formulas about Areas

def area_triangle_with_geron_formula(side1=0, side2=0, side3=0):
    check_exist_of_triangle(side1, side2, side3)
    semi_perimeter = get_semi_perimeter(side1, side2, side3)
    area = sqrt(semi_perimeter * (semi_perimeter - side1) *
                (semi_perimeter - side2) * (semi_perimeter - side3))
    return f"The are of triangle is {area} m²"


def area_triangle_with_usual_formula(side=0, h=0):
    area = side * h * 0.5
    return f"The are of triangle is {area} m²"


# Formulas about Heights, Meridians, Bisectors
# Heights

def height_in_terms_of_area_and_side(area, side):
    height_of_the_first_side = area * 2 / side
    return f"The length of the height of the side is {height_of_the_first_side} m"


def height_in_terms_of_side_and_angle(side, measure="grad", angle=0, sinus=0):
    if angle != 0:
        if measure == "grad":
            sinus = get_sinus(angle)
        elif measure == "with pi":
            sinus = sin(angle)

    if sinus != 0:
        # For some further help
        angle = asin(sinus)

    height_of_the_first_side = side * sinus

    return f"The height's length is {height_of_the_first_side} m"


def height__in_terms_of_side_and_area(side, area=0):
    height_of_the_first_side = (2 * area) / side
    return f"The length of the median of the side is {height_of_the_first_side} m"


def height__ittsa_radius_of_the_circumscribed_circle(side1=0, side2=0, radius=1):
    height_of_the_first_side = (side1 * side2) / (radius * 2)
    return f"The height's length is {height_of_the_first_side} m"


# Medians

def median_in_terms_of_sides(side1=0, side2=0, side3=0):
    median_of_the_first_side = 0.5 * sqrt(2 * side2 ** 2 + side3 ** 2 - 2 * side1 ** 2)
    return f"The length of the median of the first side is {median_of_the_first_side} m"


# Bisectors

def bisector_of_a_triangle_in_terms_of_sides(side1=0, side2=0, side3=0):
    p = get_semi_perimeter(side1, side2, side3)
    bisector_of_side1 = 2 * sqrt(side2 * side3 * p * (p - side1)) / (side2 + side3)
    return f"The length of the first side's bisector is {bisector_of_side1} m"


def bisector_of_a_triangle_in_terms_of_sides_and_angle(side2=0, side3=0, angle=0):
    bisector_of_side1 = 2 * side2 * side3 * get_cosinus(angle / 2) / (side2 + side3)
    return f"The length of the first side's bisector is {bisector_of_side1} m"
