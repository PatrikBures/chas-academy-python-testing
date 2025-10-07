class Person():
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

    def greet(self):
        print(f"Hi my name is {self.name} and i am {self.age} years old.")

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

p1 = Person("test", 10)
p2 = Person("asdf", 20)
p3 = Person("dkdkd", 30)


people = [p1, p2, p3]

for person in people:
    print(person)
