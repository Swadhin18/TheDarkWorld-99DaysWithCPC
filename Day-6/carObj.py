class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)

    def honk(self):
        return "Beep beep!"

    def repaint(self, new_color):
        self.color = new_color

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model} traveling at {self.speed} mph"


my_car = Car("Toyota", "Corolla", 2020, "blue")
my_car.accelerate(30)
my_car.brake(10)
print(my_car.honk())
my_car.repaint("red")
print(my_car)
