class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"


n = input("First Name is: ")
l = input("Last Name is: ")
p = input("Pay is: ")
employee1 = Employee(n, l, p)
print(employee1.first_name, employee1.last_name, employee1.pay, employee1.email, sep="\n")
