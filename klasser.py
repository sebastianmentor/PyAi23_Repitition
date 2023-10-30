from __future__ import annotations

class Person:
    def __init__(self,name:str, age:int) -> None:
        self.age = age
        self.name = name


class Employee(Person):
    def __init__(self, name: str, age: int, salary:int) -> None:
        super().__init__(name, age)

        self.salary = salary

    def print_emplyee(self) -> None:
        print(self.name)

    def compare_two_persons(self, another_person:Employee) -> bool:
        is_the_same = True
        if not self.name == another_person.name:
            is_the_same = False
        elif not self.age == another_person.age:
            is_the_same = False
        elif not self.salary == another_person.salary:
            is_the_same = False

        return is_the_same

    def __eq__(self, other:Employee) -> bool:
        if not isinstance(other, Employee): return False
        
        return self.name == other.name and self.age == other.age and self.salary == other.salary

class Manager(Employee):
    def __init__(self, name: str, age: int, salary: int, team:list[Employee]) -> None:
        super().__init__(name, age, salary)

        self.team = team


slave1 = Employee('Kalle Anka', 44, 20000)
slave2 = Employee('Musse Pig', 33, 24500)
slave3 = Employee('Janne Långben', 23, 50000)
slave4 = Employee('Kalle Anka', 44, 20000)


joakim = Manager('Joakim Von Anka', 80, 100_000_000, [slave1,slave2,slave3])

for emp in joakim.team:
    emp.print_emplyee()

print(slave1.compare_two_persons(slave4))
print(slave1.compare_two_persons(slave2))

print(f'{slave1 == slave2 =}')