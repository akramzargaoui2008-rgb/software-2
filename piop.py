class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"  Author: {self.author}")
        print(f"  Pages: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"  Chief editor: {self.chief_editor}")


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment.print_information()

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.kilometers = 0

    def set_speed(self, speed):
        if speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = speed

    def drive(self, hours):
        self.kilometers += self.speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters


electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.set_speed(150)
gasoline.set_speed(120)

electric.drive(3)
gasoline.drive(3)

print(f"{electric.registration_number}: {electric.kilometers} km")
print(f"{gasoline.registration_number}: {gasoline.kilometers} km")

