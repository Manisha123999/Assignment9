class Car:
    def __init__(self, distance=0, speed=0):
        self.distance = distance
        self.speed = speed

    def drive(self, hours):
        self.distance += self.speed * hours

    def get_distance(self):
        return self.distance

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
car = Car(distance=2000, speed=60)
print("Initial Distance:", car.get_distance())
car.drive(1.5)
print("Distance after driving for 1.5 hours at constant speed:", car.get_distance())

