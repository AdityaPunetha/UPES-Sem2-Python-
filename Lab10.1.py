class employee:
    def __init__(self, first_name, last_name, pay):
        self.email = first_name + "." + last_name + "@company.com"
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def info(self):
        print(self.first_name, self.last_name, self.pay, self.email, sep="\n")


n = input("First Name is: ")
l = input("Last Name is: ")
p = input("Pay is: ")
employee1 = employee(n, l, p)
employee1.info()
