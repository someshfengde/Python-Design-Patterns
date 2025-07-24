"""
we can use inheritance to build the object step by step.

the top level builder is the PersonBuilder and the bottom level builder is the PersonBirthDateBuilder.

after initializing the PersonBuilder, we can call the methods in an order to build the object.

the build method is called at the end to return the object.
"""

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb\
        .works_as_a('quant')\
        .born('1/1/1980')\
        .called('Dmitri')\
        .build()  # this does NOT work in C#/C++/Java/...
    print(me)
