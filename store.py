from people import Person

class Store:

    def __init__(self, name: str):
        self.name: str = name
        self.employees: list[Person]


    def printname(self):
        print(self.name)