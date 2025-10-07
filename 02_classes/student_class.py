from random import randint

class Student():
    def __init__(self, name: str, points: int = 0) -> None:
        self.name = name
        self.points = points

    def __str__(self) -> str:
        return f"{self.name}, {self.points}"

    def add_points(self, qty):
        self.points += qty

    def has_passed(self) -> bool:
        return self.points >= 50

if __name__ == "__main__":
    students = []

    for i in range(100):
        students.append(
            Student(
                f"student{i}", 
                randint(0,100)
            ))

    for student in students:
        student.add_points(5)

        passed = "p" if student.has_passed() else "-"

        print(f"{passed} - {student}")
