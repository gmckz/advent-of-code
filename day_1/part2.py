
digits_as_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits_array = []

file = open('input.txt', 'r')

while True:
    line = file.readline()
    if not line:
        break
    
    text_to_digits = line.replace("one", "o1e")
    text_to_digits = text_to_digits.replace("two", "t2o")
    text_to_digits = text_to_digits.replace("three", "t3e")
    text_to_digits = text_to_digits.replace("four", "f4r")
    text_to_digits = text_to_digits.replace("five", "f5e")
    text_to_digits = text_to_digits.replace("six", "s6x")
    text_to_digits = text_to_digits.replace("seven", "s7n")
    text_to_digits = text_to_digits.replace("eight", "e8t")
    text_to_digits = text_to_digits.replace("nine", "n9e")


    digits = ""
    for char in text_to_digits:
        if char.isdigit():
            digits += char
    if len(digits) > 2:
        digits = digits[0] + digits[-1]
    elif len(digits) == 1:
        digits += digits
    digits_array.append(int(digits))

file.close()
print(sum(digits_array))
