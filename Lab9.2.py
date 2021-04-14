mylist = [1, 2, 3, '4', 5]
sum = 0
for i in mylist:
    try:
        sum = sum + i
    except TypeError:
        print("unsupported operand type(s) for +: 'int' and 'str'")
print(sum)
try:
    print(mylist[5])
except IndexError:
    print("list index out of range")
