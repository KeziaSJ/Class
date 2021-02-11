class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print("maximum speed of vehicle is",modelX.max_speed,"with mileage", modelX.mileage)
