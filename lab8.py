#1
word_dictionary = {}
with open('words.txt', 'r') as words_file:
    for line in words_file:
        word = line.strip()
        word_dictionary[word] = True

words_to_check = input("Enter a word to check: ")

if words_to_check in word_dictionary:
    print(f"The word '{words_to_check}' is in the dictionary.")
else:
    print(f"The word '{words_to_check}' is not in the dictionary.")

#2

day_counts = { }

with open('f1.txt', 'r') as file_f1 :
    for line in file_f1:
        if line.startswith("From "):
            words = line.split()
            day = words[2]
            day_counts[day] = day_counts.get(day, 0) + 1
print(day_counts)

#3
dictionary_addresses = dict()
file_name = input('Enter file name: ')
try:
    file_hand = open(file_name)
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()

for line in file_hand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1

print(dictionary_addresses)

#4
dictionary_addresses = dict()
max = 0
max_address = ''

file_name = input('Enter file name: ')
try:
    file_hand = open(file_name)
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    quit()

for line in file_hand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dictionary_addresses:
        dictionary_addresses[words[1]] = 1
    else:
        dictionary_addresses[words[1]] += 1

for address in dictionary_addresses:
    if dictionary_addresses[address] > max:
        max = dictionary_addresses[address]
        max_address = address

print(max_address, max)

#5
dictionary_domains = dict()

file_name = input('Enter file name: ')
try:
    file_hand = open(file_name)
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    quit()

for line in file_hand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos + 1:]
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1
        else:
            dictionary_domains[domain] += 1

print(dictionary_domains)
