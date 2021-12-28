class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 < grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Введите оценку от 1 до 10'
        else:
            return 'Ошибка'

    def average_grade(self):
        if len(self.grades) == 0:
            return 'нет оценок'
        else:
            sum = 0
            count = 0
            for grade in self.grades.values():
                if len(grade) > 1:
                    for i in grade:
                        sum += i
                        count += 1
                else:
                    sum += grade[0]
                    count += 1
            return sum / count

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {(", ").join(self.courses_in_progress)} \nЗавершенные курсы: {(", ").join(self.finished_courses)}'
        return res

    def __gt__(self, other):
        if self.average_grade() > other.average_grade():
            return f'Средняя оценка за домашние задания у {self.name} {self.surname} выше, чем у {other.name} {other.surname}'
        elif self.average_grade() < other.average_grade():
            return f'Средняя оценка за домашние задания у {self.name} {self.surname} ниже, чем у {other.name} {other.surname}'
        else:
            return 'Средние оценки за домашние задания равны'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if len(self.grades) == 0:
            return 'нет оценок'
        else:
            sum = 0
            count = 0
            for grade in self.grades.values():
                if len(grade) > 1:
                    for i in grade:
                        sum += i
                        count += 1
                else:
                    sum += grade[0]
                    count += 1
            return sum / count

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


first_student = Student('First', 'Student', 'male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']
print(first_student.__dict__)

second_student = Student('Second', 'Student', 'female')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
print(second_student.__dict__)

first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Java']
print(first_lecturer.__dict__)

second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached = 'Java'
print(second_lecturer.__dict__)

first_reviewer = Reviewer('First', 'Reviewer')
first_reviewer.courses_attached = 'Python'
print(first_reviewer.__dict__)

second_reviewer = Reviewer('Second', 'Reviewer')
second_reviewer.courses_attached = 'Java'
print(second_reviewer.__dict__)

first_student.grade_lecturer(first_lecturer, 'Python', 8)
second_student.grade_lecturer(first_lecturer, 'Python', 10)

first_student.grade_lecturer(first_lecturer, 'Java', 6)
second_student.grade_lecturer(second_lecturer, 'Java', 8)
first_student.grade_lecturer(first_lecturer, 'Python', 1)

first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Java', 8)

students_list = [first_student, second_student]


def average_hw_rate(students_list, course_name):
    sum = 0
    count = 0
    for student in students_list:
        if student.grades.get(course_name):
            student_grade = student.grades.get(course_name)
            if len(student_grade) > 1:
                for one_grade in student_grade:
                    sum += one_grade
                    count += 1
            else:
                sum += student_grade[0]
                count += 1
    print(
        f'Средняя оценка за домашние задания по всем студентам в рамках курса {course_name} равна: {sum / count}')
    return sum / count


average_hw_rate(students_list, 'Java')

lecturers_list = [first_lecturer, second_lecturer]


def average_lecturer_grade(lecturers_list, course_name):
    sum = 0
    count = 0
    for lecturer in lecturers_list:
        if lecturer.grades.get(course_name):
            lecturer_grade = lecturer.grades.get(course_name)
            if len(lecturer_grade) > 1:
                for one_grade in lecturer_grade:
                    sum += one_grade
                    count += 1
            else:
                sum += lecturer_grade[0]
                count += 1
    print(
        f'Средняя оценка за лекции всех лекторов в рамках курса {course_name} равна: {sum / count}')
    return sum / count


print('first_lecturer', first_lecturer.__dict__)
print('second_lecturer', second_lecturer.__dict__)
average_lecturer_grade(lecturers_list, 'Python')
