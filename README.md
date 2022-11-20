# The FanGeoMath V 0.43

<!-- The firs text about the end of the work -->
🎉 today I completed my work on this program, the program is built on the principle of the basic geometry of triangles.

<br />
<br />
<!-- The list of the possabilities of my programm -->

### You can select and calculate the principal magnitudes of triangles, for example: 
<ul>
    <li>✅ Areas</li>
    <li>✅ Heights</li>
    <li>✅ Medians</li>
    <li>✅ Bisectors</li>
</ul>

**⚠️ The program is made on the version of Python 3.8 ⚠️**


Have you ever dreamed of a convenient and well-formed way to calculate the size of triangles? Well, I tried to implement this feature in my program :)

<br />

### 🤫 The program implements such features as "Entry point", which is rarely put in Python programs:
<br />

```python
if __main__ == "__main__":
    ...
    sys.exit(0)
```


### 👋 At the beginning, you are only shown welcome words once, because how can you not greet users:
<br />

```python
    def print_maintext():
        print("/*------------------------------------------------------------*/")
        print("                          Hello User!!")
        print("In this program, you can play with the areas of different shapes")
        print("                 and even draw in the console!")
        print("/*------------------------------------------------------------*/")
        print("!!!     All quantities are maintained in the SI system      !!!")
```

### after that, the function from the **"Switches" module** is triggered and the value in the special file changes, then the welcome function is no longer called
<br />

```python
    def main():
    if get_info_from_document(open_text_document(doc_name))[1] == "true":
        print_maintext()
        print("\n" * 4)
        write_text_to_document(doc_name)
```
### Functions of reading, writing and opening a **special file** with "Switch": 
<br />

```python
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
```

### Also used is the replacement of the *~~missing "switch - case" function~~ by creating its artificial analogue like a:
<br />

```python
    def switch(choice):
        if choice == 1:
            ...
        if choice == 2:
            ...
        
        e.t.c

        else:
            ...
```

⚠️⚠️⚠️
_An analogue of the function "Switch - value" is present in python, starting from version 3.10_
⚠️⚠️⚠️

## **Sources**:
<br />

## Link to Documentation
Tap here -> [Python Documentations V 3.10](https://docs.python.org/3/whatsnew/3.10.html)
<br />
<br />

## Link to the video
[![Python 10 Match Case Statements ](https://i.ytimg.com/vi/dFfI6swA7co/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDrQjf1QJk3MmKnIeiTmBTLMQ2Nnw)](https://youtu.be/dFfI6swA7co)

### The choice of the calculation method is given by calling already computational functions from the main computational file:

```python
    def switch_1(choice):
        if choice == 1:
            print("***********Areas**********")
            print("1 - with the Geron formula")
            print("2 - with usual formula")
            switch_2_areas(get_choice())
    ...

    def switch_2_areas(choice):
        if choice == 1:
            print("Please, Enter the lengths of the sides", "\n")
            side1 = int(input("Enter the length of first side: "))
            side2 = int(input("Enter the length of second side: "))
            side3 = int(input("Enter the length of third side: "))
            print(area_triangle_with_geron_formula(side1, side2, side3))
    ...
```

### After selecting the calculation method, the user enters data:

```python
    def switch_2_areas(choice):
        if choice == 1:
            print("Please, Enter the lengths of the sides", "\n")
            side1 = int(input("Enter the length of first side: "))
            side2 = int(input("Enter the length of second side: "))
            side3 = int(input("Enter the length of third side: "))
            print(area_triangle_with_geron_formula(side1, side2, side3))
    ...
```

### **the calculation file contains verification and calculation functions for calculations:**
<br />

### one of the check functions, in this case the existence of a triangle
<br />

```python
    def check_exist_of_triangle(side1=0, side2=0, side3=0):
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise(ArithmeticError("This triangle does not exist,\n"
                                "please check the correctness of the entered data."))
    ...
```

### Direct Computing Function:
<br />

```python
def area_triangle_with_geron_formula(side1=0, side2=0, side3=0):
    check_exist_of_triangle(side1, side2, side3)
    semi_perimeter = get_semi_perimeter(side1, side2, side3)
    area = sqrt(semi_perimeter * (semi_perimeter - side1) *
                (semi_perimeter - side2) * (semi_perimeter - side3))
    return f"The are of triangle is {area} m²"
```
<br />
<br />

⚠️⚠️⚠️
_all values are entered and output in SI, this is also indicated in the welcome text_
⚠️⚠️⚠️


### Challenges for the future:

* [x] Develop your own server and database
* [x] Create Game
* [x] Create AI and ML

**Of course the program was made for educational purposes, but in the future I will create more serious programs.**