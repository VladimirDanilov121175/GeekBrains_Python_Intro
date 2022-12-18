"""
Написать программу, где будет создан класс Soup (для определения типа супа), принимающий 1 аргумент,
который отвечает за основной продукт к выбираемому супу.
В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»
"""


class Soup:
    def __init__(self, ingredient=''):
        self.ingredient = ingredient

    def show_my_soup(self):
        if self.ingredient:
            return print(f"Основной продукт - {self.ingredient}")
        else:
            return print(f"Пустой кипяток")


borsch = Soup()
borsch.ingredient = 'свекла'
borsch.show_my_soup()

pea_soup = Soup()
pea_soup.show_my_soup()

"""
Написать программу с использованием класса Student (), где указываем имя студента name, номер группы group
и список полученных оценок progress. В самой программе вводим список всех студентов.
В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки
"""


class Student:
    def __init__(self):
        self.name = ''
        self.group = ''
        self.marks = ''
        self.progress = 'good'

    def get_student(self):
        for mark in ['1', '2', '3']:
            if mark in self.marks:
                self.progress = 'poor'
                break
        return self.name, self.group, self.marks, self.progress


students = []
for i in range(1, 5):
    student = Student()
    student.name = input(f"Фамилия студента № {i} >>> ")
    student.group = input("Группа >>> ")
    student.marks = input("Оценки >>> ")
    students.append(student.get_student())

print(sorted(students))


def weak_students(li):
    for progress in li:
        if 'poor' in progress:
            return True


print('Список неуспевающих:')
print(list(filter(weak_students, students)))
