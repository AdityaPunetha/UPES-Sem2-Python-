class vehicle:
    colour = "white"

    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


v1 = vehicle("v1", 10, 24)
b1 = Bus("bus1", 30, 12)
print(b1.seating_capacity())
print(b1.name, b1.max_speed, b1.mileage, b1.colour, sep="\n")
