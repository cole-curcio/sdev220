class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        if doors == 2 or doors == 4:
            self.doors: int = doors
        else:
            raise ValueError("Door must be 2 or 4")
        if roof.lower() == 'solid' or roof.lower() == 'sun roof':
            self.roof: str = roof.lower()
        else:
            raise ValueError('Roof must be "solid" or "sun roof"')
    
    def __str__(self):
        return (f"Vehicle type: {self.vehicle_type}\n")


year: int = int(input())
make = input()
model = input()
doors: int = int(input())
roof = input()
car = Automobile('car', year, make, model, doors, roof)
print(car.vehicle_type, car.year, car.make, car.model, car.doors, car.roof)
print(car)