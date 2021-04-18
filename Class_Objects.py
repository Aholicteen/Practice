# CREATING A CLASS
# ---------------------------------
# This is done when the class is doing nothing. To ensure no errors.
# You cant create a class without putting a block of code under.

class Toy:
    def __init__(self):
        pass


# CREATING AN OBJECT OF A CLASS
# ---------------------------------
# The variable doll has been assigned to the Toy class. It is an object of the class Toy.
doll = Toy()


# SETTING PROPERTIES AND ATTRIBUTES OF A CLASS
# ---------------------------------
# class Vehicle:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# self.car_name = name
# self.car_color = color
# print(car.car_name)
# car_name and car_color are the attribute names attached to the object
# 'Self' in the bracket signifies the OBJECT itself. The object you are taking in.
# Whenever you call a class, it takes in the object you are assigning it to.
# The first 'name' (self.name) is the attribute specified with the self keyword, i.e the object.
# It is the attribute attached to the object. Attributes are properties of the object.
# The second name is the parameter parsed.
# ---------------------------------
# CREATING A METHOD FOR THE CLASS
# ---------------------------------
# A method is a function which describes an action the function can carry out.
# Once you define a method in a class, it has to take in the 'self' keyword.
# This is so it can have access to the attributes relating to that object.

class Vehicle:
    """
    This is a Vehicle class
    """

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # def accel(self):
    #     print(f'The {self.color} {self.name} accelerates at 100mph')
    #     # print('The', self.color, self.name, 'accelerates at 100mph')


car = Vehicle("Mercedes", "Black")
bus = Vehicle("Toyota", "White")


# car.accel()
# bus.accel()
# print(help(car))


# print(car.name)
# Setting the attribute directly is done this way.
# Object_name.attribute = corresponding value
# This defeats the purpose of a class because it has to be done everytime you create an instance of that class.
# car.name = "Mercedes"
# car.color = "Black"

class Animal:
    animal_type = 'mammal'
    count = 0

    def __init__(self, name, legNumber):
        self.name = name
        self.legNumber = legNumber
        Animal.count += 1

    def canRun(self):
        print(f"Animal {self.name} runs with {self.legNumber} legs")

    @classmethod    # Class methods are used to modify the state of the class.
    def canSee(cls):
        print("Animal can see!!")

    @staticmethod   # Static methods have no attachment to the class
    def tailWiggle():
        print("Animal can wiggle it's tail!")
        

animal_one = Animal('hen', 2)
animal_two = Animal('cat', 4)

animal_one.canRun()
animal_two.canRun()

print("-" * 30)

print(animal_one.name)
print(animal_two.name)

print("-" * 30)

animal_one.canSee()
animal_two.canSee()

print(Animal.count)  # the count is two because that's the number of times the object is being instantiated.
