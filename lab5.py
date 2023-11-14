import math
import re

def first():
    N1 = input('Enter the random text: ')

    digit_finder = re.findall(r'\d+', N1)

    max_length = 0
    for sequence in digit_finder:
        max_length = max(max_length, len(sequence))

    print(f"Largest number of consecutive digits: {max_length}")
    return max_length

def second():
    N2 = input('Enter the random text: ')

    space_determiner = re.search(r'[a-zA-Z/s]', N2)

    if space_determiner:
        print("The text containes special characters.")
    else:
        print("The text only containes letters and spaces")

    return space_determiner is not None
def third():
    N3 = input("Enter the random text: ")

    updated_text = re.sub(r'([a-z])(?=\*)', '3', N3)

    print(f"The changed text: {updated_text}")
    return updated_text

def fourth():
    N4 = input("Enter the random text: ")

    updated_text = re.sub(r'([a-z])(?=\+)', '-', N4)
    
    print(f"The changed text: {updated_text}")
    return updated_text
def fifth():
    N5 = input("Enter the random text with no vowels: ")

    groups = re.findall(r'[a-z]+', N5)

    if not groups:
        return N5

    first_group = groups[0]

    index = N5.find(first_group) + len(first_group)

    updated_text = N5[:index] + re.sub(r'[^\s]', '.', N5[index:])

    print(f"Changed text: {updated_text}")
    return updated_text
def sixth():
    N6 = input("Enter the real nuumber: ")

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
             "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    if 0 <= N6 <= 1000:
        result = ""
        if N6 == 1000:
            result = "Тысяча"
        else:
            if N6 >= 100:
                result += hundreds[N6 // 100] + " "
                N6 %= 100
            if N6 >= 10:
                if N6 >= 11 and N6 <= 19:
                    result += teens[N6 - 10]
                    N6 = 0
                else:
                    result += tens[N6 // 10] + " "
                    N6 %= 10
            if N6 > 0:
                result += units[N6]
        print(f"Число текстом: {result}")
    else:
        print("Число не в рендже.")

def seventh():
        N7 = input("Enter the number: ")

        tenge = N7 // 100
        tiyin = N7 % 100

        if tenge == 1:
            tenge_str = "тенге"
        elif 2 <= tenge <= 4:
            tenge_str = "тенге"
        else:
            tenge_str = "тенге"

        if tiyin == 0:
            tiyin_str = ""
        elif tiyin == 1:
            tiyin_str = "0" + str(tiyin) + " тиын"
        elif 2 <= tiyin <= 4:
            tiyin_str = "0" + str(tiyin) + " тиына"
        else:
            tiyin_str = str(tiyin) + " тиынов"

        result = f"{tenge} {tenge_str}"
        if tiyin_str:
            result += f" {tiyin_str}"

        print(f"Цена {N7} в словах: {result}")
        return result
def eightth():
    N8 = input("Enter the rando text: ")

    letters = re.findall(r'[a-z]+', N8)
    digits = re.findall(r'\d+', N8)
    operators = re.findall(r'[+\-*]', N8)

    contains_one = 'one' in ''.join(letters)

    more_letters_than_operators = len(letters) > len(operators)

    return contains_one, more_letters_than_operators

    print(f"In text contains 'one': {contains_one}")
    print(f"More letters then signs: {more_letters_than_operators}")

def ninth():
    N9 = input("Enter the random text: ")

    letters = re.findall(r'[a-z]+', N9)
    digits = re.findall(r'\d+', N9)
    operators = re.findall(r'[+\-*]', N9)

    count_of_f = re.findall(r'[f]+', N9)

    if len(letters) < 3:
        return "Text contains less then 3 symbols"

    f_count = sum(group.count('f') for group in letters[:3])

    same_letter_groups = sum(1 for group in letters if len(group) >= 2 and group[0] == group[-1])

    return (f"Amount of in 'f' in first three groups: {f_count}\n"
            f"Amount of numbers that starts and ends with same number: {same_letter_groups}")

def tenth():
    N10 = input("Enter the random text: ")

    letters = re.findall(r'[a-z]+', N10)
    digits = re.findall(r'\d+', N10)
    operators = re.findall(r'[+\-*]', N10)

    groups_with_a = [group for group in letters if group.count('a') >= 2]

    longest_digits_group = next(iter(sorted(digits, key=len, reverse=True)), None)

    return groups_with_a, longest_digits_group

    print(f"Groups of words that contains a: {groups_with_a}")
    print(f"The longest number: {longest_digits_group}")
def thirteens():
    N13 = int(input("Enter the real number n: "))


    c = 0
    for i in list:
        if i == 'x':
            c += 1
    return c

    list = []
    for i in range(n):
        char = input("Enter char:")
        list.append(char)

    print(f"{list}")

def fifteenth():
    n = int(input("Enter the number n: "))
    symbols = input(f"Enter the amount of length {n}: ")

    modified_symbols = symbols.replace('.' and '!', '...')
    return modified_symbols
    print(f"The result: {modified_symbols}")

def sixteenth():
    n = int(input("Enter the number n: "))
    symbols = input(f"Enter the amount of length {n}: ")

    search_symbols = symbols.findall(r'-\-')

    if search_symbols:
        print(f"Text has - and - in input")
    else:
        print(f"Text doesn't has - and - in input")

    return search_symbols
def seveteenth():
    n = int(input("Enter the number n: "))
    symbols = input(f"Enter the amount of length {n}: ")

    n = len(symbols)
    for i in range(n - 1):
        if symbols[i] == 'a' and symbols[i + 1] == 'a':
            return i + 1
    return 0
def eighteenth():
    n = int(input("Enter the number n: "))
    symbols = input(f"Enter the amount of length {n}: ")


    filtered_symbols = ''.join(char for char in symbols if char.isalpha() or char.isspace())
    return filtered_symbols
    uppercase_symbols = symbols.upper()
    return uppercase_symbols
    alphanumeric_symbols = ''.join(char.lower() for char in symbols if char.isalnum())
    return alphanumeric_symbols









