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
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершённые курсы: {", ".join(self.finished_courses)}\n')

    def __eq__(self, other):
        return False if self.mean is None or other.mean is None else self.mean == other.mean

    def __lt__(self, other):
        return False if self.mean is None or other.mean is None else self.mean < other.mean

    def __le__(self, other):
        return False if self.mean is None or other.mean is None else self.mean <= other.mean

    # Grade lecturer add
    def rate_lecture(self, lector, course, grade):
        if (
                isinstance(lector, Lecturer)
                and course in lector.courses_attached
                and (course in self.courses_in_progress or course in self.finished_courses)
                and 0 <= grade <= 10
        ):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return None

    # Calculation mean grade
    @property
    def mean(self):
        if self.grades:
            result = sum(sum(value) for value in self.grades.values()) / sum(len(value) for value in self.grades.values())
            return round(result, 2)
        return None


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
        return False if self.mean is None or other.mean is None else self.mean == other.mean

    def __lt__(self, other):
        return False if self.mean is None or other.mean is None else self.mean < other.mean

    def __le__(self, other):
        return False if self.mean is None or other.mean is None else self.mean <= other.mean

    # Calculation mean grade
    @property
    def mean(self):
        if self.grades:
            result = sum(sum(value) for value in self.grades.values()) / sum(len(value) for value in self.grades.values())
            return round(result, 2)
        return None


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

    # Grade homework add
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
            and 0 <= grade <= 10
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return None

# Calculation average grade students
def overall_average_students(course, student_list):
    all_grades = 0
    count_grades = 0
    for student in student_list:
        if (
            isinstance(student, Student)
            and (course in student.courses_in_progress or course in student.finished_courses)
            and course in student.grades
        ):
            all_grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
    if count_grades:
        return round(all_grades / count_grades, 2)
    return 0.0

# Calculation average grade lecturer
def overall_average_lecturer(course, lecturer_list):
    all_grades = 0
    count_grades = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.grades:
            all_grades += sum(lecturer.grades[course])
            count_grades += len(lecturer.grades[course])
    if count_grades:
        return round(all_grades / count_grades, 2)
    return 0.0


# Creating students
student1 = Student('Иван', 'Иванов', 'муж')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Мария', 'Петрова', 'жен')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

# Creating Lecturers
lector1 = Lecturer('Сергей', 'Сергеев')
lector1.courses_attached += ['Python']

lector2 = Lecturer('Анна', 'Андреева')
lector2.courses_attached += ['Git']

# Creating reviewer
reviewer1 = Reviewer('Алексей', 'Алексеев')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Ольга', 'Ольгина')
reviewer2.courses_attached += ['Python']

# The reviewer give grades to the students
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer1.rate_hw(student2, 'Python', 7)

reviewer2.rate_hw(student2, 'Python', 10)

# Students rate lecturers
student1.rate_lecture(lector1, 'Python', 10)
student2.rate_lecture(lector1, 'Python', 9)
student1.rate_lecture(lector2, 'Git', 7)

# Print information about students
print('--- Студенты ---')
print(student1)
print(student2)

# Print information about lecturer
print('--- Лекторы ---')
print(lector1)
print(lector2)

# Print information about reviewer
print('--- Проверяющие ---')
print(reviewer1)
print(reviewer2)

# Comparison of students
print('--- Сравнение студентов ---')
print(f'student1 == student2: {student1 == student2}')
print(f'student1 < student2: {student1 < student2}')
print(f'student1 <= student2: {student1 <= student2}')

# Comparison of lecturer
print('--- Сравнение лекторов ---')
print(f'lector1 == lector2: {lector1 == lector2}')
print(f'lector1 < lector2: {lector1 < lector2}')
print(f'lector1 <= lector2: {lector1 <= lector2}')

# Calculating average grades for courses
students_list = [student1, student2]
lecturers_list = [lector1, lector2]

print('--- Средние оценки ---')
print(f'Средний балл студентов по Python: {overall_average_students("Python", students_list)}')
print(f'Средний балл студентов по Git: {overall_average_students("Git", students_list)}')
print(f'Средний балл лекторов по Python: {overall_average_lecturer("Python", lecturers_list)}')
print(f'Средний балл лекторов по Git: {overall_average_lecturer("Git", lecturers_list)}')