class S:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'The variable {self.name}'

