from random import randint, getrandbits

class Car():
    def __init__(self, brand:str) -> None:
        self.brand = brand
        self.speed = 0
    
    def __str__(self) -> str:
        return f"brand: {self.brand}, speed: {self.speed}"
    
    def accelerate_forward(self):
        if self.speed >= 0:
            self.speed += 3

    def accelerate_backward(self):
        if self.speed <= 0:
            self.speed -= 10
    
    def brake(self):
        if self.speed == 0:
            pass
        elif self.speed < 0:
            self.speed += 10

            if self.speed > 0:
                self.speed = 0

        elif self.speed > 0:
            self.speed -= 10

            if self.speed < 0:
                self.speed = 0

    def get_speed(self):
        return self.speed


if __name__ == "__main__":

    c1 = Car("Ford")
    c2 = Car("Volvo")
    c3 = Car("Nissan")

    cars = [c1, c2, c3]

    for car in cars:
        accelerate_forward = bool(getrandbits(1))

        for _ in range(randint(1, 20)):
            if accelerate_forward:
                car.accelerate_forward()
            else:
                car.accelerate_backward()

        print(car)

    print()

    for car in cars:
        for x in range(randint(0, 5)):
            car.brake()

        print(car)


