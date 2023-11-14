import math
from cmath import sin


def first():
    numbers = []
    count = 0
    total = 0
    max_number = 0
    min_number = 0
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            print(f"Amount: {count}, total: {total}, average number: {total/count}, max: {max_number}, min: {min_number}")
            break
        try:
            float_count = float(number)
            numbers.append(float_count)
            count = count + 1
            total = total + float_count
            max_number = max(numbers)
            min_number = min(numbers)
        except:
            print('Invalid number')
            continue

def variantsFirst():
    n = int(input("Enter a natural number: "))
    result = 1.0

    for i in range(1, 1+n):
        result *= (1+1/i**2)
    print(f"The result of the expression is: {result}")
    return result

def variantsSecond():
    n = int(input("Enter a natural number: "))
    result = 0.0

    for i in range(1, 1+n):
        result += 1/math.sin(1)+1/math.sin(1)+math.sin(i)
    print(f"The result of this expression is: {result:.2f}")
    return result

def variantsThird(n_third):

    if n_third == 1:
        return math.sqrt(2)
    else:
        inner_expression = variantsThird(n_third - 1)
        result = math.sqrt(2 + inner_expression)
        return result

n_third = int(input("Enter a natural number: "))
result = variantsThird(n_third)
print(f"The result of the expression is: {result:.10f}")

def variantsFourth():
    n = int(input("Enter the natural number: "))
    numerator = math.cos(1) / math.sin(1)
    sum_cos = 0
    sum_sin = 0
    result = 1.0

    for i in range(1, 2+n):
        sum_cos += math.cos(i)
        sum_sin += math.sin(i)
        result *= numerator * ((math.cos(1) + sum_cos) / (math.sin(1) + sum_sin))
    print(f"The result of expression: {result:.2f}")
    return result

def variantsFifth():
    n = int(input("Enter the natural number: "))

    result = 0
    for i in range(1, n + 1):
        result += 3 * i
        inner_sqrt = math.sqrt(result)
    result = math.sqrt(result)
    print(f"The result of expression: {result:.2f}")
    return result

def variantsSixth():
    n = int(input("Enter the natural number: "))
    a = int(input("Enter the natural number: "))

    result = 0
    denominator = 1
    for k in range(n + 1):
        denominator *= (a + k)
        result += 1 / denominator

    print(f"The result of expression: {result:.2f}")
    return result

def variantsSeventh():
    n = int(input("Enter the natural number: "))
    a = int(input("Enter the natural number: "))

    result = 1
    for i in range(n + 1):
        result *= (a - i * n)

    print(f"The result of expression: {result:.2f}")
    return result

def variantsEighth():
    n = int(input("Enter the natural number: "))
    a = int(input("Enter the natural number: "))

    result = 0
    for i in range(1, 2 * n + 1):
        result += (1 / a ** i)

    print(f"The result of expression is: {result:.2f}")

def variantsNinth():
    n = int(input("Enter the natural number: "))
    a = int(input("Enter the natural number: "))

    result = 1
    for i in range(1, n):
        result *= (a + i)

    print(f"The result of expression: {result:.2f}")
    return result

def variantsTenth():
    result = 1
    for i in range(1, 101):  # Values from 0.1 to 10 with step 0.1
        x = i * 0.1
        result *= (1 + math.sin(x))

    print(f"The result of expression: {result:.2f}")
    return result

def variantEleventh():
    x = int(input("Enter the real number: "))

    result = 0
    num_terms = 7
    for i in range(num_terms):
        expression = ((-1)**i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += expression

    print(f"The result of the expression: {result: .2f} ")
    return result

def variantsTwelveth(x, a, n):

    if n == 1:
        return (x + a) ** 2 + a
    else:
        inner_result = variantsTwelveth(x, a, n - 1)
    return (inner_result ** 2) + a

x = float(input("Enter the value of x: "))
a = float(input("Enter the value of a: "))
n = int(input("Enter the value of n: "))

result = variantsTwelveth(x, a, n)
print(f"The result of the expression is: {result}")

def variantsThirteens():
    x = int(input("Enter the real number: "))

    numerator = 1
    denominator = 1
    for i in range(2, 65 , 2):
        numerator *= (x-i)

    for i in range(1, 63, 2):
        denominator *= (x-i)

    result = numerator/denominator

    print(f"The result of exression: {result}")
    return result

def variantsFourteenth():
    x = int(input("Enter the real number x: "))
    n = int(input("Enter the real number n:"))

    result = 0
    for i in range(1, n + 1):
        result += math.sin(x ** i)

    print(f"The result of expression: {result}")
    return result

def variantsFifteenth():
    x = int(input("Enter the real number x: "))
    n = int(input("Enter the real number n:"))

    result = 0
    for i in range(1, n + 1):
        result += math.sin(x) ** i

    print(f"The result of expression: {result}")
    return result

def variantsSixteenth():
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))

    result = 0;
    sin_result = x;
    for i in range(n):
        sin_result = math.sin(sin_result)
        result += sin_result
    print(f"The result of the expression: {result}")
    return result

def variantsEighteenth(n18):
    if n18 == 1 or n18 == 2:
        return 0
    elif n == 3:
        return 1.5
    else:
        return ((n18 + 1) / (n18 ** 2 + 1)) * variantsEighteenth(n18 - 1) - variantsEighteenth(n18 - 2) * variantsEighteenth(n18 - 3)

n18 = int(input("Enter the value of n (n >= 4): "))
if n >= 4:
    result = variantsEighteenth(n)
    print(f"v({n}) is equal to: {result:.6f}")
else:
    print("Invalid input. Please enter n >= 4.")

def variantsNinteenth(q, r, b, c, d, n):
    if n == 0:
        return c
    elif n == 1:
        return d
    else:
        return q * variantsNinteenth(q, r, b, c, d, n - 1) + r * variantsNinteenth(q, r, b, c, d, n - 2) + b


q = float(input("Enter the value of q: "))
r = float(input("Enter the value of r: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
n = int(input("Enter the value of n (n >= 2): "))

if n >= 2:
    result = variantsNinteenth(q, r, b, c, d, n)
    print(f"x({n}) is equal to: {result:.6f}")
else:
    print("Invalid input. Please enter n >= 2.")
