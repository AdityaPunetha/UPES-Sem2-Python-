count = 0
with open("test.txt", 'r') as file:
    for lines in file:
        count = count + 1
print("Total number of lines : ", count)
