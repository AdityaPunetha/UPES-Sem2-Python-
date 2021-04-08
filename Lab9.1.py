for i in range(int(input())):
    a, b = (k for k in input().split())
    try:
        print(int(a) / int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: " + str(b))
      