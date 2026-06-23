class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car(self):
        print(f'{self.make} {self.model} {self.year} ')



car1 = Car(make='Ford',model='Mustang',year=21)
car1.display_car()