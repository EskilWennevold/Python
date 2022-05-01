class PythonStudents:

    def __init__(self):
        self.students = []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        temp = self.index
        self.index += 1
        if self.index > len(self.students):
            raise StopIteration()
        return self.students[temp]


class Student:
    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
        return f'{self.__dict__}'