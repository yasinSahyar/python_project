"""
class Dog:
    pass
dog = Dog()
dog.name = "Bubbles"
dog.birth_year = 2022

print(f"{dog.name:s} was born in {dog.birth_year:d}.")                 # Bubbles was born in 2022.

"""

class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

dog = Dog("Bubbles", 2022)

print(f"{dog.name:s} was born in {dog.birth_year:d}." )                #Bubbles was born in 2022.



