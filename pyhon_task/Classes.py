#Create a new class
class Dog:
    species = "Jack Russel Therier"
    def __init__(self, name, age):#instance attributes
        self.name = name
        self.age = age
# __init__ initialize each new instance of the class ()
# self parameter is automatically added to the class instance (than others attribute can be used with current instance)   - the unique value of the attributes will be for every new instance


