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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # задание 1 наследование
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # задание 1 наследование

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


# создание объектов класса
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

student2 = Student('Peter', 'Parcker', 'man')
student2.courses_in_progress += ['C++']
student2.courses_in_progress += ['Java']

cool_lectur = Lecturer('Some', 'Buddy')
cool_lectur.courses_attached += ['Python']
cool_lectur.courses_attached += ['Java']

cool_review = Reviewer('Wasija', 'Bugldy')
cool_review.courses_attached += ['Python']
cool_review.courses_attached += ['C++']

cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'Python', 9)
cool_review.rate_hw(best_student, 'C++', 10)

# Студент не изучает данный курс оценка не учтена
student2.evaluated(cool_lectur, 'Python', 10)
# Оценки учтены, студенты посещают данные курсы
student2.evaluated(cool_lectur, 'Java', 9)
best_student.evaluated(cool_lectur, 'Python', 10)
best_student.evaluated(cool_lectur, 'Java', 10)


# проверочные принты
print(best_student.grades)
print(cool_lectur.courses_attached)
print(cool_review.courses_attached)
print('Оценки студента', best_student.courses_in_progress)
print('Оценки лектора', cool_lectur.grades)
