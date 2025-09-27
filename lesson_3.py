class Human:
    def __init__(self, name = 'Human'):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []
    def add_passanger(self, *args):
        for passanger in args:
            self.passangers.append(passanger)
    def print_passangers_names(self):
        if self.passangers != []:
            print(f'Names of {self.brand} passangers: ')
            for passanger in self.passangers:
                print(passanger.name)
        else:
            print(f'There are no passangers in {self.brand}')

bogdan = Human('Bogdan')
vika = Human('Vika')
car = Auto('Toyota')
car.add_passanger(bogdan, vika)
car.print_passangers_names()