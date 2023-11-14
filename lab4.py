import math

t = int(input("Enter the real number t: "))
s = int (input("Enter the real number s: "))

def function_first(a,b,c):
    return ((2*a-b-math.sin(c))/5+abs(c))

result1 = function_first(t, -2*s, 1.17) + function_first(2.2,t,s-t)

print(f"The result of the first expression: {result1}")

def function_second(a,b):
    return ((a**2+b**2)/(a**2+2*a*b+3*b**2+4))
result2 = function_second(1.2,s)+function_second(t,s)-function_second(2*s-1, s*t)
print (f"The result of the second expression: {result2}")

