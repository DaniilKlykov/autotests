# 1
numbers = list(range(1, 8))

for i in numbers:
    if i == 5:
        break
print(i)


# 2
words = [f"str{i}" for i in range(10)]
print(words)


# 3
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


# 4
class Lead:
    def __init__(self, name):
        self.name = name


def change_name(lead: Lead, new_name: str) -> None:
    lead.name = new_name


if __name__ == "__main__":
    original_lead = Lead("Иван")
    print(f"До вызова функции: {original_lead.name}")

    change_name(original_lead, "Пётр")
    print(f"После вызова функции: {original_lead.name}")


# 5
class Student:
    def __init__(self, name: str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


students = [
    Student("Анна", 20, [4.5, 5.0, 4.8]),
    Student("Борис", 21, [3.2, 4.0, 3.8]),
    Student("Вера", 19, [4.9, 5.0, 4.7]),
]


good_students = [s for s in students if s.get_avg_grade() > 4.1]

for student in good_students:
    print(f"{student.name}: {student.get_avg_grade():.2f}")
