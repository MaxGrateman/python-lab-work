import math
import numpy as np
import np


def first():
    num1= float(input("Enter the first number: "))
    num2=float(input("Enter the second number "))
    num3=float(input("Enter the third number: "))

    interval_check_num1 = 1 < num1 < 3
    interval_check_num2 = 1 < num1 < 3
    interval_check_num3 = 1 < num1 < 3

    if interval_check_num1:
        print(f"{num1} belongs to the interval")
    if interval_check_num2:
        print(f"{num2} belongs to the interval")
    if interval_check_num3:
        print(f"{num3} belongs to the interval")

def second():
    x = float(input("Enter the x number: "))
    y = float(input("Enter the y number: "))

    if x < y:
        small = x
        large = y
    else:
        small = y
        large = x

    new_small = (small + large) / 2
    new_large = 2 * (small * large)

    if x < y:
        new_small = x
        new_large = y
    else:
        y = new_small
        x = new_large
    print(f"Updated x: {x}")
    print(f"Updated y: {y}")

def third():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number "))
    c = float(input("Enter the third number: "))

    if a >= 0:
        a_squared = a ** 2
    else:
        a_squared = a

    if b >= 0:
        b_squared = b ** 2
    else:
        b_squared = b

    if c >= 0:
        c_squared = c ** 2
    else:
        c_squared = c

    print(f"Squared value of the a: {a_squared}")
    print(f"Squared value of the b: {b_squared}")
    print(f"Squared value of the c: {c_squared}")

def fourth():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number "))
    z = float(input("Enter the third number: "))

    sum_xyz = x*y*z

    if sum_xyz < 1:
        smallest = min(x,y,z)
        if smallest == x:
            x = (y + z)/2
        elif smallest == y:
            y=(x+z)/2
        else:
            z=(x+y)/2
    else:
        if x < y:
            x = (z+y)/2
        else:
            y=(x+z)/2

    print(f"Updated x: {x}")
    print(f"Updated y: {y}")
    print(f"Updated z: {z}")

def variantsFirst():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number "))
    c = float(input("Enter the third number: "))
    d = float(input("Enter the fourth number: "))

    if a <= b <= c <= d:
        a = b = c = d
    elif a < b < c < d:
        pass
    else:
       a = a ** 2
       b = b ** 2
       c = c ** 2
       d = d ** 2

    print(f"Updated a: {a}")
    print(f"Updated b: {b}")
    print(f"Updated c: {c}")
    print(f"Updated d: {d}")

def variantsSecond():
    x = float(input("Enter the number x: "))
    y = float(input("Enter the number y: "))

    if x < 0 and y < 0:
        x = abs(x)
        y=abs(y)
    elif x < 0 or y < 0:
        x += 0.5
        y += 0.5
    elif 0.5 <= x < 2.0 or 0.5 <= y <= 2.0:
        pass
    else:
        x /= 10
        y /= 10

    print(f"Updated x: {x}")
    print(f"Updated y: {y}")

def variantsThird():
    x = float(input("Enter the number x: "))
    y = float(input("Enter the number y: "))
    z = float(input("Enter the number z: "))

    if x + y > z and y + z > x and z + x > y:
        print("Triangle can exist")

        sides = [x,y,z]
        sides.sort()
        a, b, c = sides
        if c ** 2 < a ** 2 + b ** 2:
            print("Acute-angle triangle")
        else:
            print("This is not an acute-angle triangle")

    else:
        print("Triangle with this sides cannot exist")

def variantsFourth():
    a = float(input("Enter the first number ≠ 0: "))
    b = float(input("Enter the second number "))
    c = float(input("Enter the third number: "))

    if a == 0:
        print("a cannot be equal zero")
    else:
        pass

    D = b ** 2 - 4 * a * c

    if D > 0:
        root1=(-b + D ** 0.5) / (2*a)
        root2=(b+D**0.5) / (2*a)
        print(f"The first root: {root1}, the second root: {root2}")
    elif D == 0:
        root = -b / (2*a)
    else:
        print("There are no valid roots")

def variantsFifth():
    h = float(input("Enter the h number"))

    a = math.sqrt((abs(math.sin(8 * h)) + 17) / (1 - math.sin(4 * h) * math.cos(h ** 2 + 18)) ** 3)

    b = 1 - math.sqrt(3 / (3 + abs(math.tan(h ** 2) - math.sin(a * h))))

    c = a * h ** 2 * math.sin(b * h) + b * h ** 2 * math.cos(a * h)

    D = b ** 2 - 4 * a * c

    if D > 0:
        # Находим действительные корни
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        print("Valid roots:")
        print("x1 =", root1)
        print("x2 =", root2)
    elif D == 0:
        root = -b / (2 * a)
        print("Only one valid root:")
        print("x =", root)
    else:
        print("No valid roots")

def variantsSixth():
    a1 = float(input("Enter a1: "))
    c1 = float(input("Enter c1: "))
    c1_ = float(input("Enter c1_: "))
    a2 = float(input("Enter a2: "))
    c2 = float(input("Enter c2: "))
    c2_ = float(input("Enter c2_: "))

    abs_values= abs(a1*c2_ - a2 * c1_)

    if abs_values >= 0.0001:
        A = np.array([[a1, c1, c1_],
                      [a2, c2, c2_]])
        B = np.array([0, 0])
        solution = np.linalg.solve(A, B)
        print("Solution:")
        print(f"x = {solution[0]}")
        print(f"y = {solution[1]}")
    else:
        print("||a1*b2 - a2*b1|| < 0.0001, no solution available.")

def variantsSeventh():
    a = float(input("Enter the first number ≠ 0: "))
    b = float(input("Enter the second number "))
    c = float(input("Enter the third number: "))

    if a == 0:
        print("a cannot be equal zero")
    else:
        pass

    D = b ** 2 - 4 * a * c

    if D > 0:
        y1 = (-b + math.sqrt(D)) / (2*a)
        y2 = (-b - math.sqrt(D)) / (2*a)

        x1=math.sqrt(y1)
        x2=-math.sqrt(y1)
        x3=math.sqrt(y2)
        x4=-math.sqrt(y2)

        print(f"The four roots are: {x1},{x2},{x3},{x4}")
    elif D == 0:
        y = -b / (2*a)

        if y >= 0:
            x5 = math.sqrt(y)
            x6 = -math.sqrt(y)
            print(f"if D equals zero, then roots are: {x5}, {x6}")
    else:
        print(f"No valid roots")
def variantsEighth():
    a = float(input("Enter the a number: "))
    b = float(input("Enter the b number "))
    c = float(input("Enter the c number: "))
    d = float(input("Enter the d number: "))
    s = float(input("Enter the s number: "))
    t = float(input("Enter the t number: "))
    u = float(input("Enther the u number"))

    value_first = s*a+t*b+u
    value_second = s*c+t*d+u
    # Если точки имеют одинаковые знаки, то они находятся на одной плоскости, если разные, то на разных
    if (value_first > 0 and value_second < 0) or (value_first < 0 and value_second > 0):
        print("The (a,b) points and (c,d) belongs to different planes")
    else:
        print("The points belong to the same plane")
def variantsNinth():
    a = float(input("Enter the a number: "))
    b = float(input("Enter the b number "))
    c = float(input("Enter the c number: "))
    d = float(input("Enter the d number: "))
    e = float(input("Enter the e number: "))
    f = float(input("Enter the f number: "))
    g = float(input("Enther the g number"))
    h = float(input("Enter the h number"))

    oriented_area_efg = 0.5 * (e - a) * (h - f) - (g - e) * (f - b)

    oriented_area_efc = 0.5 * (e - c) * (h - f) - (g - e) * (f - d)

    # если оренитрованые координаты двух треуголников имеют одинаковые знаки, то они находятся в одной плоскости
    if (oriented_area_efg > 0 and oriented_area_efc > 0) or (oriented_area_efg < 0 and oriented_area_efc < 0):
        print("Points (a, b) and (c, d) belong to the same plane.")
    else:
        print("Points (a, b) and (c, d) belong to diferent planes.")
def variantsTenth():
    x1 = float(input("Enter the x1 coordinate: "))
    y1 = float(input("Enter the y1 coordinate: "))
    x2 = float(input("Enter the x2 coordinate: "))
    y2 = float(input("Enter the y2 coordinate: "))
    x3 = float(input("Enter the x3 coordinate: "))
    y3 = float(input("Enter the y3 coordinate: "))

    A1 = 0.5 * ((0 - x2) * (y1 - y2) - (x1 - x2) * (0 - y2))
    A2 = 0.5 * ((0 - x3) * (y2 - y3) - (x2 - x3) * (0 - y3))
    A3 = 0.5 * ((0 - x1) * (y3 - y1) - (x3 - x1) * (0 - y1))

    triangle_area = abs(A1 + A2 + A3)

    if abs(A1 + A2 + A3) == triangle_area:
        print("The origin is inside the area")
    else:
        print("The origin is outside the area")

def variantEleventh():
    a = float(input("Enter the a number: "))
    b = float(input("Enter the b number "))
    c = float(input("Enter the c number: "))
    d = float(input("Enter the d number: "))

    # условие на поворт 90 градусов
    if (a <= c and b <= d) or (b <= c and a <= d):
        print("Smaller rectangle CAN fit inside the big one")
    else:
        print("Smaller rectangle CANNOT fit inside the big one")

def variantsTwelveth():
    a = float(input("Enter the a number: "))
    b = float(input("Enter the b number "))
    c = float(input("Enter the c number: "))
    x = float(input("Enter the x number: "))
    y = float(input("Enther the y number: "))

    if (a <= x and b <= y) or (a <= y and b <= x) \
            or (a <= x and c <= y) or (a <= y and c <= x) \
            or (b <= x and c <= y) or (b <= y and c <= x):
        print("The brick CAN fit into the hole.")
    else:
        print("The brick CAN'T fit into the hole.")

def variantsThirteenth():
    x = float(input("Enter the real number x: "))

    if -2 <= x < 2:
        F_a = x ** 2
    else:
        a = 4
    print(f"f(x) = {F_a}")

def variantsFourteenth():
    x = float(input("Enter the real number x: "))

    if x <= 2:
        F_a = x**2 + 4*x + 5
    else:
        F_a = 1/(x**2 + 4*x + 5)
    print(f"F({x}) = {F_a}")

def variantsFifteenth():
    x = float(input("Enter the real number x: "))

    if x <= 0:
        F_a = 0
    elif 0 < x <= 1:
        F_a = x
    else:
        F_a = x ** 4

    print(f"F({x}) = {F_a}")

def variantsSixteenth():
    x = float(input("Enter the real number x: "))

    if x <= 0:
        F_a = 0
    elif 0 < x <= 1:
        F_a = x ** 2 - x
    else:
        F_a = x ** 2 - math.sin(math.pi * x ** 2)

    print(f"F({x}) = {F_a}")

def variantsSeveteenth():
    a = float(input("Enter the number a: "))

    if a <= 0:
        F_a = -a if a >= -1 else a ** 2
    elif 0 < a <= 1:
        F_a = a ** 2
    elif a == 2:
        F_a = 4
    else:
        F_a = -1 / (a ** 2)

    print(f"F(a) = {F_a}")
def variantsEightnth():
    a = float(input("Enter the number a: "))

    if -2 <= a <= -1:
        F_a_1 = 1
    elif -1 <= a <= 0:
        F_a_1 = 0
    elif 0 <= a <= 1:
        F_a_1 = 1
    elif 1 <= a <= 2:
        F_a_1 = 1
    else:
        F_a_1 = 1

    if 0 <= a <= 1:
        F_a_2 = 1
    elif a == 1:
        F_a_2 = 1
    elif 0 <= a <= 3:
        F_a_2 = -2.5
    else:
        F_a_2 = -1

    print(f"F(a) Graph 1: {F_a_1}")
    print(f"F(a) Graph 2: {F_a_2}")

def variantsNinteenth():
    x = float(input("Enter the point x: "))
    y = float(input("Enter the point y: "))

    # уравнение окружности
    if x**2 + y**2 <= 1:
        print("Point belong to first graph")
    else:
        print("Point doesn't belong to first graph")


    if (-1 <= x <= -0.5 or 0.5 <= x <= 1) and (-1 <= y <= -0.5 or 0.5 <= y <= 1):
        print("Point belong to second graph")
    else:
        if x ** 2 + y ** 2 <= 0.25 and (x >= 0 or y >= 0):
            print("Point belong to second graph")
        else:
            print("Point doesn't belong to second graph")

    if -1 <= x <= 1 and -1 <= y <= 1:
        print("Point belong to third graph")
    else:
        print("Point doesn't belong to third graph")

def variantsTwentyth():
    x = float(input("Enter the point x: "))
    y = float(input("Enter the point y: "))

    if (-1 <= x <= 1) and (-1 <= y <= 1 - abs(x)):
        print("Point belong to first graph.")
    else:
        print("Point doesn't belong to first graph")

    if (-0.5 <= x <= 0.5) and (-1 <= y <= 1 - abs(x)):
        print("Point belong to second graph.")
    else:
        print("Point doesn't belong to second graph")

    if ((x >= -2 and x <= 1) and (y >= -1 and y <= 1) and
        ((x + 2) ** 2 + y ** 2 <= 1)) or ((x >= -2 and x <= -1)
        and (y >= -1 and y <= 1) and (y >= -x - 1)):
        print("Point belong to third graph")
    else:
        print("Point doesn't belong to third graph")