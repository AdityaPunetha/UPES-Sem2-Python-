class vehicle:
    colour = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


veh1 = vehicle("vehicle no.1", 10, 24)
bus1 = Bus("bus no 1", 30, 12)
print(bus1.seating_capacity())
print(bus1.name, bus1.max_speed, bus1.mileage, bus1.colour, sep="\n")
