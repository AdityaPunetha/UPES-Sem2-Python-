try:
    file = open('Test file 1.txt', 'r')
    file2 = open('Test file 2.txt', 'w')
    data = file.read()
    file2.write(data.replace('\"', '\\"'))
    file.close()
    file2.close()
    file2 = open('Test file 2.txt', 'r')
    for v in file2:
        print(v)

except FileNotFoundError:
    print("no such file exits in system")
finally:
    file2.close()