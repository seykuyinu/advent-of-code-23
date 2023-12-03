word_digits = {
    "one" : 1,
    "two" : 2, 
    "three" : 3, 
    "four" : 4, 
    "five" : 5, 
    "six" : 6, 
    "seven" : 7, 
    "eight" : 8, 
    "nine" : 9,
}

def read_file(file_path):
    content = open(file_path, 'r')

    return content

def find_words(line):
# inspo from: https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string/
    words = []
    for key, value in word_digits.items():
        for i in range(len(line)):
            if line.startswith(key, i):
                words.append([value, i])
    
    return words


def find_numbers(line):
    numbers_index = []
    for index, c in enumerate(line):
        if c.isnumeric():
            numbers_index.append([int(c), index])

    return numbers_index

def calibration_value(line):
    words = find_words(line)
    numbers = find_numbers(line)

    words_and_numbers = words + numbers
    words_and_numbers.sort(key = lambda x: x[1])

    if len(words_and_numbers) == 0:
        return 0
    elif len(words_and_numbers) == 1:
        return f"{words_and_numbers[0][0]}{words_and_numbers[0][0]}"
    else:
        return f"{words_and_numbers[0][0]}{words_and_numbers[-1][0]}"

def sum_document(content):
    lines = content.readlines()
    # lines = content.splitlines()
    values = []

    for line in lines:
        values.append(int(calibration_value(line)))
    
    return sum(values)

def main():
    path = "inputs/day1.txt"
    content = read_file(path)

    print(sum_document(content))
    
if __name__ == "__main__":
    main()




# part 1:
# def read_file(file_path):
#     content = open(file_path, 'r')

#     return content
#     # return "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"


# def calibration_value(line):
#     numbers = []
#     for c in line:
#         if c.isnumeric():
#             numbers.append(c)

#     if len(numbers) == 0:
#         return 0
#     elif len(numbers) == 1:
#         return f"{numbers[0]}{numbers[0]}"
#     else:
#         return f"{numbers[0]}{numbers[-1]}"

# def sum_document(content):
#     lines = content.readlines()
#     # lines = content.splitlines()
#     values = []

#     for line in lines:
#         values.append(int(calibration_value(line)))
    
#     return sum(values)

# def main():
#     path = "inputs/day1.txt"
#     content = read_file(path)

#     print(sum_document(content))
    
# if __name__ == "__main__":
#     main()