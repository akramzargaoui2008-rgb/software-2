import random

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"Running elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm! All elevators going to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


class Car:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed
        self.distance_driven = 0

    def drive(self, hours):
        self.distance_driven += self.speed * hours

    def __str__(self):
        return f"{self.make} {self.model}"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = max(1, car.speed + change)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"{car} speed: {car.speed} km/h, distance driven: {car.distance_driven} km")

    def race_finished(self):
        for car in self.cars:
            if car.distance_driven >= self.distance:
                return True
        return False


print("Elevator test")
h = Elevator(0, 10)
h.go_to_floor(5)
h.go_to_floor(0)

print("Building test")
b = Building(0, 20, 3)
b.run_elevator(0, 7)
b.run_elevator(1, 15)
b.run_elevator(2, 3)

print("Fire alarm test")
b.fire_alarm()

print("Grand Demolition Derby")
cars = [
    Car("Toyota", "Supra", 120),
    Car("Ford", "Mustang", 130),
    Car("Chevrolet", "Camaro", 125),
    Car("Dodge", "Challenger", 115),
    Car("BMW", "M3", 140),
    Car("Audi", "RS6", 135),
    Car("Honda", "Civic", 110),
    Car("Subaru", "Impreza", 118),
    Car("Nissan", "GT-R", 145),
    Car("Porsche", "911", 150),
]

race = Race("Grand Demolition Derby", 8000, cars)
hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"Status after {hours} hours:")
        race.print_status()

print(f"Race finished after {hours} hours!")
race.print_status()

