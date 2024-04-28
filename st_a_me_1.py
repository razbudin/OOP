class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # задание 1 наследование


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # задание 1 наследование


# создание объектов класса
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

cool_lectur = Lecturer('Some', 'Buddy')
cool_lectur.courses_attached += ['Python']
cool_lectur.courses_attached += ['Java']

cool_review = Reviewer('Wasija', 'Bugldy')
cool_review.courses_attached += ['Python']
cool_review.courses_attached += ['C++']

# проверочные принты
# print(cool_lectur.courses_attached)
# print(cool_review.courses_attached)
# print('students', best_student.courses_in_progress)
