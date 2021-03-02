#Create a new class
class Dog:
    species = "Jack Russel Therier"
    def __init__(self, name, age, cout_color):#instance attributes
        self.name = name
        self.age = age
        self.cout_color = cout_color
# __init__ initialize each new instance of the class ()
# self parameter is automatically added to the class instance (than others attribute can be used with current instance)   - the unique value of the attributes will be for every new instance

    def __str__(self):
        return f"The dog name is {self.name} he is {self.age} years old"

    def dog_speak(self, sound):
        return f"The {self.name} sound is {sound}"


Buddy_dog = Dog("Buddy",4,"Brown")
Jessy_dog = Dog("Jessy",2,"Red")



#Ex 2 

class Car():

    def __init__(self,color,mileage):
        self.color =color
        self.mileage = mileage

    def __str__(self):
        return f"The car color is {self.color} and the driven miles is {self.mileage}"
    



#Ex 3

class Car():

    def __init__(self,color,mileage):
        self.color =color
        self.mileage = mileage


    def drive(self, additional_distance):
        self.additional_distance = additional_distance


    def __str__(self):
        return f"The car color is {self.color} and the driven miles is {self.mileage + self.additional_distance} "
        