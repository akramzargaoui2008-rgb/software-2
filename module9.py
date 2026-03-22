# Exercise 1
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

car = Car("ABC-123", 142)
print(f"Registration: {car.registration_number}")
print(f"Max speed:    {car.max_speed} km/h")
print(f"Speed:        {car.speed} km/h")
print(f"Distance:     {car.distance} km")

# Exercise 2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Speed after +30, +70, +50: {car.speed} km/h")

car.accelerate(-200)
print(f"Speed after emergency brake (-200): {car.speed} km/h")

# Exercise 3
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours

car = Car("ABC-123", 142)
car.distance = 2000
car.speed = 60

car.drive(1.5)
print(f"Distance after driving 1.5h at 60 km/h: {car.distance} km")

# Exercise 4
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours

cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

hour = 0
while True:
    hour += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
    if any(car.distance >= 10000 for car in cars):
        break

print(f"Race finished after {hour} hours!\n")
print(f"{'Reg':<10} {'Max speed':>10} {'Speed':>8} {'Distance':>12}")

for car in cars:
 print(f"{car.registration_number:<10} {car.max_speed:>7} km/h {car.speed:>5} km/h {car.distance:>9.1f} km")