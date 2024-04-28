class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        values_grade = []
        for _, value in self.grades.items():
            values_grade.extend(value)

        if len(values_grade):
            avg_grade = round(sum(values_grade) / len(values_grade), 1)
        else:
            avg_grade = ''

        study = str(self.courses_in_progress)
        finished = str(self.finished_courses)
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {avg_grade}\n'
            f'Курсы в процессе изучения: {study}\n'
            f'Завершенные курсы: {finished}'
        )


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

    # Задание 3, __str__
    def __str__(self):
        values_grade = []
        for _, value in self.grades.items():
            values_grade.extend(value)
        grade = round(sum(values_grade) / len(values_grade), 1)
        return (
            f'Имя: {self.name}\nФамилия:'
            f'{self.surname}\nСредняя оценка за лекции: {grade}')


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# создание объектов класса
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

student2 = Student('Peter', 'Parcker', 'man')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.finished_courses += ['C++']

cool_lectur = Lecturer('Some', 'Buddy')
cool_lectur.courses_attached += ['Python']
cool_lectur.courses_attached += ['Java']

cool_review = Reviewer('Wasija', 'Bugldy')
cool_review.courses_attached += ['Python']
cool_review.courses_attached += ['C++']

cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Python', 9)
cool_review.rate_hw(best_student, 'C++', 10)
cool_review.rate_hw(student2, 'Python', 9)
cool_review.rate_hw(student2, 'Python', 8)


student2.evaluated(cool_lectur, 'Python', 10)
student2.evaluated(cool_lectur, 'Java', 9)
best_student.evaluated(cool_lectur, 'Python', 10)
best_student.evaluated(cool_lectur, 'Java', 10)


# проверочные принты
# print('Оценки студента', best_student.grades)
# print('Лектор', cool_lectur.courses_attached)
# print('Ревьювер', cool_review.courses_attached)
# print('Изучаемые курсы', best_student.courses_in_progress)
# print('Оценки лектора', cool_lectur.grades)
print('student str', student2, sep='\n')
print('reviewer str', cool_review, sep='\n')
print('lectur str', cool_lectur, sep='\n')
