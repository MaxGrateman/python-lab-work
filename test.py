def split_string(input):

    pattern = r'b\(,.\/|)'
    spliter = input.split(pattern)

    return spliter

input = input("Enter the string")
result = split_string(input)