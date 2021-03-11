str = input().upper()
letters = set(str)
for i in letters:
    print(str.count(i), i)
