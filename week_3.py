class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"This is a {self.make} {self.model}."

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors 

    def describe(self):
        return f"This is a {self.make} {self.model} with {self.__num_doors} doors."
    
    def get_num_doors(self): 
        return self.__num_doors

class Bike(Vehicle):
    def __init__(self, make, model, has_gears):
        super().__init__(make, model)
        self.has_gears = has_gears

    def describe(self): 
        gear_info = "with gears" if self.has_gears else "without gears"
        return f"This is a {self.make} {self.model} {gear_info}."


def vehicle_info(vehicle):
    print(vehicle.describe())


car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha","w06", True)


vehicle_info(car)
vehicle_info(bike)


print(f"The car has {car.get_num_doors()} doors.")
