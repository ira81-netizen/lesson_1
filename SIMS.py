class Human:
    def __init__(self, name = 'Human'):
        self.name = name
class School:
    def __init__(self, group):
        self.group = group
        self.people = []
    def add_person(self, *args):
        for person in args:
            self.people.append(person)
    def print_people_names(self):
        if self.people != []:
            print(f'Names of {self.group} people: ')
            for person in self.people:
                print(person.name)
        else:
            print(f'There are no people in {self.group}')

class School1:
    def __init__(self, group):
        self.group = group
        self.people = []
    def add_person(self, human):
        self.people.append(human)
    def print_people_names(self):
        if self.people != []:
            print(f'Names of {self.group} people: ')
            for person in self.people:
                print(person.name)
        else:
            print(f'There are no people in {self.group}')

bogdan = Human('Bogdan')
vika = Human('Vika')

school1 = School('Group1')
school2 = School1('Group2')
school2.add_person(bogdan)
school2.add_person(vika)
school1.add_person(bogdan, vika)
school1.print_people_names()
school2.print_people_names()