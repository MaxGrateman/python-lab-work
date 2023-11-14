# 1 2 3
with open('file.txt', 'r') as file:
    components = list(map(float, file.read().split()))

sum_components = sum(components)
print("Sum of the components: ", sum_components)

product_components = 1
for num in components:
    product_components *= num
print("Product of components: ", product_components)

sum_squars = sum(num**2 for num in components)
print("Sum of suqared components: ", sum_squars)

module_sum = abs(sum_components)
square_product = product_components ** 2
print("Module and square of product: ", module_sum, square_product)

last_product = components[1]
print("Last component of the file: ", last_product)

largest_component = max(components)
print("The Largest component: ", largest_component)

even_components = [num for num in components if num % 2 == 0]
if even_components:
    smallest_component = min(even_components)
    print("The smallest even components: ", smallest_component)

else:
    print("There are no even numbers")

odd_components = [abs(num) for num in components if num % 2 != 0]
if odd_components:
   largest_odd_component = max(odd_components)
   print("The largest odd module of components: ", largest_odd_component)
else:
    print("There are no odd components")

smallest_component = min(components)

sum_small_large_components = largest_component + smallest_component
print("Sum of the largest and smallest components: ", sum_small_large_components)

difference_components = components[0] - components[-1]
print("The difference between first and last components: ", difference_components)

even_count = len(even_components)
print("The amount of event numbers is: ", even_count)

doubled_odd_components = [num for num in components if num % 2 != 0 and num * 2 in components]
doubled_odd_count = len(doubled_odd_components)
print("Doubled odd components: ", doubled_odd_count)

square_odd_components = [num for num in components if num % 2 != 0 and num ** 2 in components]
square_odd_count = len(square_odd_components)
print("Squared odd components: ", doubled_odd_count)

# 4
with open('f1.txt', 'r') as f1, open('f2.txt', 'r') as f2, open('order.txt', 'r') as order_file:
    components_f1 = list(map(int, f1.read().split()))
    components_f2 = list(map(int, f2.read().split()))
    order = list(map(int, order_file.read().split()))

rewrite_f2 = [components_f1[order[i]-1] for i in range(len(components_f1))]
with open('f2.txt', 'w') as f2:
    f2.write(' '.join(map(str, rewrite_f2)))

rewrite_f1 = [components_f1[order[i]-1] for i in range(len(components_f1))]
with open('f1.txt', 'w') as f1:
    f2.write(' '.join(map(str, rewrite_f1)))

# 5
with open('f1.txt', 'r') as f1, open('f2.txt', 'r') as f2, open('order.txt', 'r') as order_file, open('f3.txt', 'r') as f3, open('f4.txt', 'r') as f4, open('f5.txt', 'r') as f5, open('order.txt', 'r') as order_file:
    components_f1 = list(map(int, f1.read().split()))
    components_f2 = list(map(int, f2.read().split()))
    order = list(map(int, order_file.read().split()))
    components_f3 = list(map(int, f3.read().split()))
    components_f4 = list(map(int, f4.read().split()))
    components_f5 = list(map(int, f5.read().split()))

rewrite_f2 = [components_f4[order[i]-1] for i in range(len(components_f4))]
with open('f2.txt', 'w') as f2:
    f2.write(' '.join(map(str, rewrite_f2)))

rewrite_f1 = [components_f3[order[i]-1] for i in range(len(components_f3))]
with open('f1.txt', 'w') as f1:
    f3.write(' '.join(map(str, rewrite_f1)))

rewrite_f3 = [components_f5[order[i]-1] for i in range(len(components_f5))]
with open('f3.txt', 'w') as f3:
    f3.write(' '.join(map(str, rewrite_f3)))

rewrite_f4 = [components_f2[order[i]-1] for i in range(len(components_f2))]
with open('f4.txt', 'w') as f4:
    f4.write(' '.join(map(str, rewrite_f4)))

rewrite_f5 = [components_f1[order[i]-1] for i in range(len(components_f1))]
with open('f5.txt', 'w') as f5:
    f5.write(' '.join(map(str, rewrite_f5)))

#6
with open('f6.txt', 'r') as f6:
    content = f6.read()

if content[:2].isdigit():

    number = int(content[:2])

    if number % 2 == 0:
        print("The first two characters are even numbers.")
    else:
        print("The first two characters are odd numbers.")
else:
    print("The first two characters are not digits.")

#7
with open('f7.txt', 'r') as f7:
    numbers = [int(line.strip()) for line in f7.readlines()]

even_numbers = [num for num in numbers if num % 2 == 0]
divisible_numbers = [num for num in numbers if num % 3 == 0 and num % 7 != 0]
perfect_squares = [num for num in numbers if num > 0 and (int(num ** 0.5) ** 2) == num]

with open('g', 'w') as g:
    g.write("Even numbers:\n")
    g.write(' '.join(map(str, even_numbers)))
    g.write("Divisible numbers\n: ")
    g.write(' '.join(map(str, divisible_numbers)))
    g.write("Perfect squares\n")
    g.write(' '.join(map(str, perfect_squares)))

#8
with open('f1.txt', 'r') as f1:
    fibonacci_numbers = list(map(int, f1.read().strip().split(',')))

next_fibonacci_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]

fibonacci_numbers.append(next_fibonacci_number)

with open('f1.txt', 'w') as f1:
    f1.write(','.join(map(str, fibonacci_numbers)))

#9
with open('f1.txt', 'r') as f1:
    content = [int(line.strip().split() for line in f1.read())]

modified_text = content.lower()

with open('g.txt', 'w') as g:
    g.write(modified_text)

#11
with open('f1.txt', 'r') as f1:
    content = [int(line.strip().split() for line in f1.read())]

even_ones = [num for num in content if num % 2 == 0]
odd_ones = [num for num in content if num % 2 != 0]


with open('g.txt', 'w') as g:
    g.write(' '.join(map(str,even_ones)))

with open('h.txt', 'w') as h:
    h.write(' '.join(map(str, odd_ones)))

#12
with open('f1.txt', 'r') as f1:
    components = f1.readlines()

reversed_components = reversed(components)

with open('g.txt', 'w') as g:
    g.writelines(reversed_components)

#13
with open('f1.txt', 'r') as f1:
    components_f = f1.readlines()

with open('g.txt', 'r') as g:
    components_g = g.readlines()

with open('h.txt', 'w') as h:
    h.writelines(components_f)

    h.writelines(components_g)

#14
with open('f1.txt', 'r') as f1:
    numbers = list(map(int, f1.readlines()))

unique_numbers = set(numbers)

with open('g.txt', 'w') as g:
    file.writelines('\n'.join(map(str, unique_numbers)))

#15
with open('f1.txt', 'r') as file_f, open('h.txt', 'r') as file_h:
    numbers_f = list(map(int, file_f.readlines()))
    numbers_h = list(map(int, file_h.readlines()))

positive_numbers = [num for num in numbers_f if num > 0]
negative_numbers = [num for num in numbers_f if num < 0]

positive_numbers_h = [num for num in numbers_h if num > 0]
negative_numbers_h = [num for num in numbers_h if num < 0]

arranged_numbers = []
while positive_numbers and negative_numbers:
    arranged_numbers.extend(positive_numbers_h[:2])
    arranged_numbers.extend(negative_numbers_h[:2])
    positive_numbers_h = positive_numbers_h[2:]
    negative_numbers_h = negative_numbers_h[2:]

with open('g.txt', 'w') as file_g:
    file_g.write('\n'.join(map(str, arranged_numbers)))

#16
with open('f1.txt', 'r') as file_f:
    numbers = list(map(int, file_f.readlines()))

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

arranged_numbers = []
while positive_numbers and negative_numbers:
    arranged_numbers.extend(positive_numbers[:5])
    arranged_numbers.extend(negative_numbers[:5])
    positive_numbers = positive_numbers[5:]
    negative_numbers = negative_numbers[5:]
    arranged_numbers.extend(positive_numbers[:20])
    arranged_numbers.extend(negative_numbers[:20])
    positive_numbers = positive_numbers[20:]
    negative_numbers = negative_numbers[20:]

with open('g.txt', 'w') as file_g:
    file_g.write('\n'.join(map(str, arranged_numbers)))

#18
with open('f3.txt', 'r') as f3:
    content = f3.read()

modified_content = content + 'end'

with open('g.txt', 'w') as g:
    g.write(modified_content)

with open('f3.txt', 'w') as f3:
    f3.write(modified_content)

#19
with open('f1.txt', 'r') as f1, open('g.txt', 'r') as g:
    symbol_content_f1 = f1.read()
    symbol_content_g = g.read()

matching_components = [component for component in symbol_content_f1 if component in symbol_content_g]


with open('h.txt', 'w') as h:
    h.write(matching_components)

#20
with open('f4.txt', 'r') as f4:
    content = f4.read()

processed_content = ''.join(['a' + char + 'a' for char in content])

with open('g.txt', 'w') as g:
    g.write(processed_content)
