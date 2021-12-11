# TODO здесь писать код

from random import randint, choice

NAMES = ['Лиам', 'Оливия', 'Артем', 'София', 'Шарлота', 'Пол', 'Анна', 'Артур']
SURNAMES = ['Андро', 'Ариньяк', 'Сименс', 'Тейлор', 'Мальро', 'Брук']

def generate_person():
    name = choice(NAMES)
    surname = choice(SURNAMES)
    age = randint(20, 50)
    return name, surname, age

class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'{self.__name} {self.__surname}. Возраст {self.__age} года'


class Employee(Person):
    def calc_salary(self):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f'\nЗарплата {self.calc_salary()}'


class Manager(Employee):
    def calc_salary(self):
        return 12000

class Agent(Employee):
    sales: int

    def calc_salary(self):
        return 4000 + 0.1 * self.sales

class Worker(Employee):
    hours: int

    def calc_salary(self):
        return 120 * self.hours


if __name__ == '__main__':
    employees = list()

    for _ in range(3):
        employees.append(Manager(*generate_person()))

    for _ in range(3):
        agent = Agent(*generate_person())
        agent.sales = randint(2000, 10000)
        employees.append(agent)

    for _ in range(3):
        worker = Worker(*generate_person())
        worker.hours = randint(20, 50)
        employees.append(worker)

    for emp in employees:
        print(emp)