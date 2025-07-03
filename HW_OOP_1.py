class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.mean}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Заершенные курсы: {', '.join(self.finished_courses)}\n')

    def __eq__(self, other):
        return self.mean == other.mean

    def __lt__(self, other):
        return self.mean < other.mean

    def __le__(self, other):
        return self.mean <= other.mean

    def rate_lecture(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in lector.courses_attached
                and (course in self.courses_in_progress or course in self.finished_courses)):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def mean(self):
        if len(self.grades) != 0:
            result = float(sum(sum(value) for value in self.grades.values()) / sum(len(value) for value in self.grades.values()))
            return result
        else:
            return 'Оценок нет'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.mean}')

    def __eq__(self, other):
        return self.mean == other.mean

    def __lt__(self, other):
        return self.mean < other.mean

    def __le__(self, other):
        return self.mean <= other.mean

    @property
    def mean(self):
        if len(self.grades) != 0:
            result = float(sum(sum(value) for value in self.grades.values()) / sum(len(value) for value in self.grades.values()))
            return result
        else:
            return 'Оценок нет'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


students_1 = Student('Иванов', 'Иван', 'М')
students_2 = Student('Иванова','Анна', 'Ж')
lecturer_1 = Lecturer('Семенов','Семен')
lecturer_2 = Lecturer('Семенова','Евгения')
reviewer_1 = Reviewer('Смирнов', 'Олег')
reviewer_2 = Reviewer('Смирнова', 'Олеся')

lecturer_1.courses_attached = ['Python', 'Git']
lecturer_2.courses_attached = ['SQL', 'API']
reviewer_1.courses_attached = ['Python', 'Git']
reviewer_2.courses_attached = ['SQL', 'API']

students_1.courses_in_progress = ['Python', 'SQL']
students_1.finished_courses = ['Git']

students_2.courses_in_progress = ['API', 'Git']
students_2.finished_courses = ['SQL']




