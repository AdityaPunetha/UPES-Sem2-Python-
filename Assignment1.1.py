file = open("test.txt",'r')
number_of_lines = int(input("No. of lines you want to read: "))
for i in range(number_of_lines):
    line = file.readline()
    print(line)
