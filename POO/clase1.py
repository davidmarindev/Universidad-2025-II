class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
    
    def __str__(self):
        return f"{self.year} - {self.make} - {self.model} - ({self.color})"

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} has started.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

    def honk(self):
        print(f"The {self.year} {self.make} {self.model} goes 'Beep Beep!'")
        
    def change_color(self, new_color):
        old_color = self.color
        self.color = new_color
        print(f"The {self.year} {self.make} {self.model} has changed color from {old_color} to {new_color}.")

class CarFactory:
    def __init__(self, name, make, models):
        self.name = name
        self.make = make
        self.models = models
        self.cars = []

    def create_car(self, model, year, color):
        new_model_available = self.is_model_available(model)
        if not new_model_available:
            print(f"Model {model} is not available in the factory.")
            return None

        car = Car(self.make, model, year, color)
        self.cars.append(car)
        return car
    
    def is_model_available(self, model):
        return model.lower() in self.models


# mustang = Car("Ford", "Mustang", 2021, "Red")
# camaro = Car("Chevrolet", "Camaro", 2020, "Blue")

# print(f"Mustang is running?: {mustang.is_running}")

# mustang.start()
# camaro.start()

# print(f"Mustang is running?: {mustang.is_running}")

# mustang.change_color("Black")

# print(f"Camaro color: {camaro.color}")
# print(f"Mustang color: {mustang.color}")

fabrica_ford = CarFactory("Super Cars", "Ford", ["mustang", "focus", "explorer"])
fabrica_chevrolet = CarFactory("Auto World", "Chevrolet", ["camaro", "malibu", "impala"])
fabrica_jeep = CarFactory("4x4 Masters", "Jeep", ["wrangler", "cherokee", "compass"])

focus = fabrica_ford.create_car("Focus", 2022, "White")
mustang = fabrica_ford.create_car("Mustang", 2021, "Gray")
mustang2 = fabrica_ford.create_car("Mustang", 2023, "Blue")
explorer = fabrica_ford.create_car("Explorer", 2020, "Black")

# print("Mustang:", mustang)

# print("Focus:", focus)
# print("Focus Make:", focus.make)
# print("Focus Model:", focus.model)

for car in fabrica_ford.cars:
    print(car)