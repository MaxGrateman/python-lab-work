#1
from collections import deque

def tpl_sort():
    if all(isinstance(elem, int) for elem in input1):
        sorted_tuple = tuple(sorted(input1))
        return sorted_tuple
    else:
        return input1

input1 = (2,3,7,4,1)
result = tpl_sort(input1)
print(result)


#2
def slicer(input2, element):
    if element not in input2:
        return tuple()
    start_index = input2.index(element)

    if input2.count(element) > 1:
        end_index = input2.index(element, start_index + 1)
    else:
        end_index = len(input2)

    result_tuple = input2[start_index:end_index + 1]
    return result_tuple

input2 = (1,2,4,5,7,4,2,6)
element = 2
result2 = slicer(input2, element)
print(result2)

#3
def sieve(input3):
    if all(isinstance(elem,int) for elem in input3):
        list_of_unique_numbers = []
        unique_integers = set(input3)
        for elem in unique_integers:
            list_of_unique_numbers.append(elem)
        return list_of_unique_numbers

input3 = (1,2,5,4,6)
print(sieve(input3))

#4
def del_form_tuple(input4):
        del input4[0]
        print(input4)
input4 = (1,2,3,4,5)
print(del_form_tuple(input4))

#6
athlets = [
    {"name": "Max Astakhov", "sport":"swimming", "age": 36, "years_playing": 15},
    {"name": "Dulat Khalbaev", "sport":"boxing", "age": 37, "years_playing": 14}
]

for athlete in athlets:
    if athlets["sport"].lower() == "swimming":
        print(f"{athlete['name']} (age: {athlete['age']} years playing {athlete['years_playing']}")


#7
def qualification(skaters):
    for skater in skaters:
        if skater["skating_score"] > 70:
            print(f"This skater passed the qualification: {skater['name']}, {skater['skating_score']}")

skaters = [
    {"name": "Veronika Yun", "skating_score": 75},
    {"name": "Timur Mironov", "skating_score": 68},
    {"name": "Zharas Biketov", "skating_score": 85},
]

#8
def descinding_remove_tuple(input8,element_to_remove):
    new_tuple = tuple(elem for elem in input8 if elem != element_to_remove)

input8 = (1,3,5,6,9,2,7)
max_element = max(input8)
min_element = min(input8)

filtered_tuple = descinding_remove_tuple(input8,max_element)
filtered_tuple = descinding_remove_tuple(filtered_tuple,min_element)

sorted_result = sorted(filtered_tuple, reverse=True)

print(f"Result of input8: {sorted_result}")

#9
def exchange_tuple(input9):
    max_element = max(input9)
    min_element = min(input9)

    max_index = input9.index(max_element)
    min_index = input9.index(min_element)

    new_list = list(input9)

    new_list[max_index], new_list[min_index] = new_list[min_index], new_list[max_index]

    result_exchange = tuple(new_list)

    return result_exchange

input9 = [(1), (3), (7), (4)]
print(exchange_tuple(input9))

#10
def arith_tuple(input10):
    positive_numbers = [num for num in input10 if num > 0]
    squared_elements = [num**2 for num in positive_numbers]

    if squared_elements:
        arith_mean = sum(squared_elements)/len(squared_elements)
        return arith_mean
    else:
        print("There are no positive numbers")


input10 = (9,6,3,2,8)
print(arith_tuple())

#11

def contactList(input11):
    contacts = [
        ("Dulta", 18),
        ("Emma",21),
        ("Ellie",25),
        ("Joel",42),
        ("Kim",35)
    ]

    for contact in contacts:
        if contact[0] == input11:
            return contact[1]
        return "Not found"

input11 = input("Enter first name: ")
print(contactList(input11))

#12
def commaSeparatedSymbols(input12):
    char_list = input12.split(',')
    char_tuple = tuple(char_list)
    print(char_list)
    print(char_tuple)

input12 = input("Enter the comma-separated items: ")
commaSeparatedSymbols(input12)

#13
def listCombiner():
    names = ["Joel", "Tommy", "Sarah"]
    ages = [52,42,16]
    specialities = ["Shooter", "Keeper", "Writer"]
    groups = ["A", "B", "A"]

    combined_list = list(zip(names,ages, specialities, groups))

    print("List: ")
    for item in combined_list:
        print(item)

#14
def queueType():
    queue = deque([1,'orange', 1.5, 5,'Name','Age',True, 'life', 'song', 'guitar', 3.0, 'Max', 'Python'])

    queue.insert(7, 'Qalaisyn?')
    print("My queue: ", queue)

    valueSix = queue[6]
    queue.appendleft(valueSix)

    del queue[7]

    print("New queue: ", queue)

    repeatValues = len(queue) - len(set(queue))
    print("Repeated values: ", repeatValues)

    sortQueue = deque(sorted(queue))
    print("Sorted queue: ", sortQueue)

#15
def taskfifteen():
    studentData = (["Math", "PE", "Programming"],
                   [45, 56, 92],
                   deque(["Joel Miller", "Ellie Williams", "Tommy Miller"]))
    print("Initial table: ")
    for subject,grade,student in zip(*studentData):
        print(f"{subject: 15} | {grade:13} | {student}")

    mathGradeIndex = studentData[0].index("Mathematics")
    failedStudIndex = studentData[2].index("Joel Miller")
    if studentData[1][mathGradeIndex] < 50:
        studentData[1][mathGradeIndex] = 55

    print("\nUpdated Table: ")
    for subject, grade, student in zip(*studentData):
        print(f"{subject}, {grade}, {student}")

def taskSixteen():
    different = ["one", "two", "one", "1", 1, "5", 1, "1", 123, 321, 123, 321 , 90, "Python", "python", "Python", "lecture 4"]
    uniqueNumbers = set(different)
    print("Amount of unique numbers: ", len(uniqueNumbers))
    for value in sorted(uniqueNumbers):
        print(value)

    set1 = {"apple", "orange", "peach"}
    set2 = {"tasty", "bitter", "hot"}

    thirdSet = set1.union(set2)

    isSubset = set1.issubset(thirdSet)

    print("Third set", thirdSet)
    print("Subset?: ", isSubset)

    setNumbers1 = {4,6,11,5,23,65}
    setNumbers2 = {7,1,3,5,45,31}

    max_setNumber1 = max(setNumbers1)
    min_setNumber1 = min(setNumbers1)
    max_setNumber2 = max(setNumbers2)
    min_setNumber2 = min(setNumbers2)

    maxSet = max([setNumbers1, setNumbers2], key=max)

    print("First set max and min: ", max_setNumber1, min_setNumber1)
    print("Second set max and min: ", max_setNumber2, min_setNumber2)
    print("Max set among sets: ", maxSet)
def taskSeventeen(input17):
    dictionary = {
        "doomer": "depressive person with bright inside world",
        "zoomer": "New generation person with stupid jokes",
        "boomer": "Pretty old person with old view of the world"
    }

    if input17 in dictionary:
        print(f"\nDefinition of '{input17}'")
        definitions = dictionary[input17]
        if isinstance(definitions, list):
            for i, definition in enumerate(definitions, 1):
                print(f"{i}, {definition}")
        else:
            print(definitions)
    else:
        print(f"{input17} not found")

    peopleDatabase = {
        "12345": {"full_name": "Joel Miller", "birthday": "1975-06-14", "mobile_number": "123-456-7890"},
        "67890": {"full_name": "Ellie Williams", "birthday": "2014-08-03", "mobile_number": "987-654-3210"},
    }

    inputIIN = input("Enter the iderntification number")
    if inputIIN in peopleDatabase:
        print("\nPerson info: ")
        for key, value in peopleDatabase[inputIIN].item():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("Not found")

    currencyInfo = {
        "usd": 456.5,
        "eur": 532.2,
        "gbp": 603.8,
    }

    inputCurrency = input("Enter the curency name: ")

    if inputCurrency in currencyInfo:
        exchangeRate = currencyInfo[inputCurrency]
        print(f"\n {inputCurrency.upper()} is equal to {exchangeRate}")
    else:
        print("Error in request")

input17 = input("Enter the word as doomer, zoomer or boomer").lower