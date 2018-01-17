numbers = [1, 2, 3]

file = open("numbers.txt", 'w')

for value in numbers:
    file.write(str(value) + "\n")

file.close()
