class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Средняя оценка за домашние задания
    def homework_rating(self):
        values_grade = []
        for _, value in self.grades.items():
            values_grade.extend(value)
        if len(values_grade):
            return round(sum(values_grade) / len(values_grade), 1)
        return

    # Задание 2, метод для оценки студентами лекторов
    def evaluated(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание 3, __str__
    def __str__(self):
        study = str(self.courses_in_progress)
        finished = str(self.finished_courses)
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.homework_rating()}\n'
            f'Курсы в процессе изучения: {study}\n'
            f'Завершенные курсы: {finished}\n'
        )

    # Задание 3, сравнение через < >
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Объекты должны принадлежать классу Student')
            return
        if (self.homework_rating() is not None and
                other.homework_rating is not None):
            return (self.homework_rating() < other.homework_rating(),
                    self.name, other.name)
        else:
            return 'Невозможно выполнить сравнение'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    # задание 1 наследование
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Средняя оценка за лекции
    def lection_rating(self):
        values_grade = []
        for _, value in self.grades.items():
            values_grade.extend(value)
        if len(values_grade):
            return round(sum(values_grade) / len(values_grade), 1)

    # Задание 3, __str__
    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия:'
            f'{self.surname}\n'
            f'Средняя оценка за лекции: {self.lection_rating()}\n')

    # Задание 3, сравнение через < >
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Объекты должны принадлежать классу  Lecturer')
            return
        if (self.lection_rating() is not None and
                other.lection_rating() is not None):
            return (self.lection_rating() < other.lection_rating(),
                    self.name, other.name)
        else:
            return 'Невозможно выполнить сравнение'


class Reviewer(Mentor):

    # задание 1 наследование
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Задание 2, перемещение из class Mentor в class Reviewer
    # метода rate_hw
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание 3, __str__
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


# создание объектов класса
student1 = Student('Ruoy', 'Eman', 'man')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['C#']

student2 = Student('Peter', 'Parcker', 'man')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.finished_courses += ['C++']


lectur1 = Lecturer('Some', 'Buddy')
lectur1.courses_attached += ['Python']
lectur1.courses_attached += ['Java']

lectur2 = Lecturer('Ivan', 'Bronevoy')
lectur2.courses_attached += ['Python']
lectur2.courses_attached += ['C++']


review1 = Reviewer('Wasija', 'Bugldy')
review1.courses_attached += ['Python']
review1.courses_attached += ['C++']
review2 = Reviewer('Irina', 'Rusina')
review2.courses_attached += ['Python']
review2.courses_attached += ['Java']

review1.rate_hw(student1, 'Python', 10)
review1.rate_hw(student1, 'Python', 9)
review1.rate_hw(student1, 'C++', 10)
review1.rate_hw(student2, 'Python', 9)
review1.rate_hw(student2, 'Python', 8)
review2.rate_hw(student1, 'Python', 10)
review2.rate_hw(student1, 'Python', 9)
review2.rate_hw(student1, 'C++', 10)
review2.rate_hw(student2, 'Python', 9)
review2.rate_hw(student2, 'Java', 8)

student2.evaluated(lectur1, 'Python', 10)
student2.evaluated(lectur1, 'Java', 9)
student1.evaluated(lectur1, 'Python', 10)
student1.evaluated(lectur2, 'Java', 10)
student2.evaluated(lectur2, 'Python', 10)
student2.evaluated(lectur1, 'Java', 9)
student1.evaluated(lectur2, 'Python', 10)
student1.evaluated(lectur2, 'Java', 10)


# Задание 4, функции
student_list = [student1, student2]
lectur_list = [lectur1, lectur2]


def all_student_homework_rating(student_list, course):
    all_grade = []
    for student in student_list:
        if course in student.courses_in_progress:
            all_grade.extend(student.grades.get(course))
    if len(all_grade):
        return round(sum(all_grade) / len(all_grade), 1)


def all_lectur_courses_rating(lectur_list, course):
    all_grade = []
    for lectur in lectur_list:
        if course in lectur.courses_attached:
            all_grade.extend(lectur.grades.get(course))
    if len(all_grade):
        return round(sum(all_grade) / len(all_grade), 1)


# проверочные принты
print('Оценки студента', student1.grades)
print()
print('Лектор', lectur1.courses_attached)
print()
print('Ревьювер', review1.courses_attached)
print()
print('Изучаемые курсы', student1.courses_in_progress)
print()
print('Оценки лектора', lectur1.grades)
print()
print('student str', student2, sep='\n')
print('reviewer str', review1, sep='\n')
print('lectur str', lectur1, sep='\n')
print(student1 < student2)
print()
print(lectur1 < lectur2)
print()
print(lectur1 > lectur2)
print()
print('Средняя оценка успеваемости всех студентов: '
      f"{all_student_homework_rating(student_list, 'Python')}")
print('Средняя оценка преподавания лекций: '
      f"{all_lectur_courses_rating(lectur_list, 'Python')}")
