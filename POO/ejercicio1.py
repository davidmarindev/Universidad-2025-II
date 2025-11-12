class Car:
    def __init__(self, make, model, year, color, price_per_day = 100):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_rented = False
        self.price_per_day = price_per_day
        
    def __str__(self):
        return f"{self.year} - {self.make} - {self.model} - ({self.color}) - ${self.price_per_day}/day"

class Customer:
    def __init__(self, name, driver_license):
        self.name = name
        self.driver_license = driver_license
        
    def __str__(self):
        return f"Customer: {self.name}, License: {self.driver_license}"

class Rental:
    def __init__(self, customer, car, rental_days):
        self.customer = customer
        self.car = car
        self.rental_days = rental_days
        self.total_cost = car.price_per_day * rental_days
        
    def __str__(self):
        return f"Rental: {self.customer.name} has rented {self.car} for {self.rental_days} days. Total cost: ${self.total_cost}"

class CarRentalService:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []
        self.customers = []
        self.rentals = []
        
    def add_car(self, car):
        self.cars.append(car)
        
    def add_customer(self, customer):
        if (customer.driver_license):
            self.customers.append(customer)
        else:
            print("Invalid customer. Driver license is required.")

    def rent_car(self, car, customer, rental_days):
        if car in self.cars and not car.is_rented:
            car.is_rented = True
            rental = Rental(customer, car, rental_days)
            self.rentals.append(rental)
            print(f"You have rented the {car}.")
        else:
            print(f"Sorry, the {car} is not available for rent.")
            
    def return_car(self, car):
        if car in self.cars and car.is_rented:
            car.is_rented = False
            print(f"You have returned the {car}.")
        else:
            print(f"The {car} was not rented from us.")
            
# Example usage:

rental_service = CarRentalService("City Car Rentals", "Downtown")

car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Civic", 2019, "Red")

rental_service.add_car(car1)
rental_service.add_car(car2)

customer1 = Customer("John Doe", "D1234567")
customer2 = Customer("Jane Smith", "D7654321")

rental_service.add_customer(customer1)
rental_service.add_customer(customer2)
rental_service.rent_car(car1, customer1, 3)
rental_service.rent_car(car2, customer2, 5)

rental_service.return_car(car1)