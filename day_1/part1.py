digits_array = []
file = open('input.txt', 'r')

while True:
    line = file.readline()
    if not line:
        break
    digits = ""
    for char in line:
        if char.isdigit():
            digits += char
    if len(digits) > 2:
        digits = digits[0] + digits[-1]
    elif len(digits) == 1:
        digits += digits
    digits_array.append(int(digits))

file.close()
# print(digits_array)
print(sum(digits_array))
    