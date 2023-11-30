import re

#1
def encode_symbol(symbol, shift):
    if 'a' <= symbol <= 'z':
        encryptedSymbol = chr((ord(symbol) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= symbol <= 'Z':
        encryptedSymbol = chr((ord(symbol) - ord('a') + shift) % 26 + ord('a'))
    else:
        encryptedSymbol = symbol

    return encryptedSymbol

symbol = 'A'
shift = 3
print(f"{encode_symbol(symbol, shift)}")

#2
def encode_str(input_str, key):
    encoded_str = ""
    for char in input_str:
        if char.isalpha():
            shifted_char = chr((ord(char) + key - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) + key - ord('a')) % 26 + ord('a'))
            encoded_str += shifted_char
        else:
            encoded_str += char
    return encoded_str

input2 = input("Enter the string")
encryption_key = 2
encoded_text = encode_str(input2, encryption_key)

print("Encoded Text:", encoded_text)

#5
def strong_str(input3):
    words = input3.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    highlighted_str = ""
    for word in words:
        if word_count[word] > 1:
            highlighted_str += f'<strong>{word}</strong> '
        else:
            highlighted_str += f'{word} '

    return highlighted_str.strip()
input3 = input("Enter th string")

#7
def format_ipv4(input7):
    if not (0 <= input7 <= 0xFFFFFFFF):
        raise ValueError("Invalid format")

    decimal_format = ".".join(str((input7 >> shift) & 0xFF) for shift in (24, 16, 8, 0))

    hex_format = hex(input7)[2:]

    octal_format = oct(input7)[2:]

    return decimal_format, hex_format, octal_format

input7 = input("Enter the ip adress")
decimal, hexa, octal = format_ipv4(input7)

print(f"Decimal: {decimal}")
print(f"Hexadecimal: {hexa}")
print(f"Octal: {octal}")

#8
def unique_alphabets(input8):
    cleaned_str = ''.join(char.lower() for char in input8 if char != ' ')
    unique_chars = ''.join(sorted(set(cleaned_str)))

    return unique_chars

input8 = input("Enter the string")
result = unique_alphabets(input8)

#9
def format_text(input9):
    cleaned_text = re.sub(r'\s+', ' ', input9)
    formatted_text = re.sub(r'(?<=[.!?]) +', '  ', cleaned_text)

    return formatted_text


input9 = input("Enter the sentence with 2 spaces and dots")
formatted_text = format_text(input9)

print("\nFormatted Text:")
print(formatted_text)

#12
def find_word(input12, target_word):
    pattern = r'\b' + re.escape(target_word) + r'\b'
    matches = re.findall(pattern, input12)
    return matches

input12 = input("Enter the sentence")
target_word = input("Enter the target word")

result = find_word(input12, target_word)
print(result)

#13
def find_ciphers(input13):
    pattern = r'\b[A-Za-z0-9]+\b'

    matches = re.findall(pattern, input13)
    return matches

input13 = input("Enter the sentence")
ciphers_found = find_ciphers(input13)

print(ciphers_found)

#14
def lo_finder(input14):
    pattern = re.compile(r'\w*lo')
    with open('txt1.txt', 'r') as file:
        text = file.read()
        matches = pattern.findall(text)
    print(matches)

input14 = input("Enter the words with 'io'")
result = lo_finder(input14)

#15

def find_phone():
    phone_numbers = [
        "+7 (775) 448-85-06",
        "+7 (701) 654-12-23",
        "+7 (708) 653-65-99",
    ]

    pattern = re.compile(r'\+7\(\d{3} \d{3}-\d{4}$')

    for phone_number in phone_numbers:
        if re.match(pattern,phone_number):
            print(f"{phone_number} valid")
        else:
            print(f"{phone_number} isn't valid")
#16
def split_str(input16):
    spliter = input16.split(",")

    return spliter

input16 = input("Enter the sentence with spaces")
result = split_str(input16)

#18
def time_finder(input18):
    pattern = re.compile(r'\b\d{2}:\d{2}\b')
    input18_result = input18.findall(pattern)
    return input18_result
input18 = "Enter the time and thing to do"
result = time_finder(input18)

#17
def teg_open(text, tag):
    pattern = rf'<{tag}>(.*?)</{tag}>'
    matches = re.findall(pattern, text, re.DOTALL)

    for match in matches:
        print(match)

text = input("Enter text inside the tag")