def seventeenth():
    a = float(input("Enter the point x"))

    if a == 2:
        F_x=4
    elif 0 < a <= 1:
        F_x= a**2
    else:
        F_x=-1/a**2

    print(f"F({a}={F_x}")

seventeenth()
