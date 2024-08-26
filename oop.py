
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old and I identify as a {self.gender}")

person = Person(name = 'Asiphe Masoka', age=30, gender='Female')  

person.introduce()