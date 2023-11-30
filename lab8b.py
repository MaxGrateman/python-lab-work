#1
word_dictionary = {}
with open('words.txt', 'r') as words_file:
    for line in words_file:
        word = line.strip()
        word_dictionary[word] = True

words_to_check = input("Enter a word to check: ")

if words_to_check in word_dictionary:
    print(f"The word {words_to_check} is in the dictionary")
else:
    print(f"The word {words_to_check} is not in the dictionary")

#2
massage_dictionary = {}
with open('mbox-short.txt', 'r') as mailbox_file:
    for line in mailbox_file:
        if line.startswith('From'):
            word = line.strip()
            day = word[2]
            day_counts = day_counts.get(day, 0) + 1

print(day_counts)


#3
massage_dictionary_count = dict()
file_name = input('Enter file name: ')

try:
    file_open = open(file_name)
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    quit()

for line in file_open:
    words = line.strip().split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in massage_dictionary_count:
            massage_dictionary_count[words[1]] = 1
        else:
            massage_dictionary_count[words[1]] += 1

print(massage_dictionary_count)

max_key = max(massage_dictionary_count, key=massage_dictionary_count.get)
print(f"Key with max value: {max_key}, value: {massage_dictionary_count[max_key]}")


#4
dictionary_domain = {}
file_name = input("Enter the name of existing file: ")

try:
    open_file = open(file_name)
except FileNotFoundError:
    print('File cannot be opened: ', file_name)
    quit()

for line in open_file:
    words = line.strip().split()
    if len(words) < 2 or words[1] != 'From':
        continue
    else:
        doggy = words[1].find("@")
        domain = words[1][doggy + 1:]
        if domain not in dictionary_domain:
            dictionary_domain[domain] = 1
        else:
            dictionary_domain[domain] += 1

print(dictionary_domain)

faivorite_music = [
    'Fleetwood Mac',
    'Johnny Cash',
    'Avril Lavigne',
    'The Outfield',
    'Mazzy Star'
]

myself_dictionary = {
    'height':  168,
    'fav_color': 'warm-orange',
    'fav_actress': 'Emma Stone',
    'fav_band': 'Queen',
    'fav_game': 'Minecraft'
}

def get_info():
    user_input = input("Enter height, fav color, actress, band and game")

    if user_input == 'height':
        return f"Your height is {myself_dictionary['height']}"
    elif user_input == 'fav color':
        return f"Your fav color {myself_dictionary['fav_color']}"
    elif user_input == 'fav_actress':
        return f"Yuor fav actress {myself_dictionary['fav_actress']}"
    elif user_input == 'fav_band':
        return f"Your fav band {myself_dictionary['fav_band']}"
    elif user_input == 'fav_game':
        return f"Yuor fav game {myself_dictionary['fav_game']}"
    else:
        return "Invalid request"

result = get_info()
print(result)

fav_music_dictionary = {
    'Mazzy Star': ['Into Dust', 'Look on Down the Bridge', 'Fade Into You'],
    'Johnny Cash': ['Hurt', 'Man in Black', 'The Man Comes Around'],
    'Avril Lavigne': ['Complicated', 'Sk8ter Boi', 'Im with You']
}

print("My fav singers and thier songs")
for singer, songs in fav_music_dictionary.items():
    print(f"/n{singer}")
    for song in songs:
        print(f": {song}")