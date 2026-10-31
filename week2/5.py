class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"brand: {self.brand}, model: {self.model}, year: {self.year}")


car1 = Car("Lada", "Granta", "2014")
car2 = Car("Toyota", "Land Crusier", "2006")
car3 = Car("Haval", "x6", "2022")

car1.print_car_info()
car2.print_car_info()
car3.print_car_info()
