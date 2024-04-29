class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, grade, favorite_subject, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grade = grade
        self.favorite_subject = favorite_subject


class Teacher(Person):
    def __init__(self, subject, experience, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = subject
        self.experience = experience
        self.salary = salary
