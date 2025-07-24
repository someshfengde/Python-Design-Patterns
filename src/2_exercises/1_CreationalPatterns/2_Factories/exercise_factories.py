class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def __init__(self):
        self._current_id = 0

    def create_person(self, name):
        person = Person(self._current_id, name)
        self._current_id += 1
        return person