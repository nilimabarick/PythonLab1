# demonstrate single inheritance
class Vehicle:
     def start(self):
         print("Vehicle Started")


class Bike(Vehicle):
     def helmet(self):
          print("always wear helmet while riding")

b = Bike()
b.start()
b.helmet()


# program for multilevel inheritance

class Animal:
     def Eat(self):
         print("Animal can eat")
    
class Dog(Animal):
     def bark(self):
         print("dog can bark")

class Puppy(Dog):
     def weep(self):
         print("puppy can weep")

p = Puppy()
p.Eat()
p.bark()
p.weep()

# Example of method overloading

class A:
     def show(self):
         print("welcome")

     def show(self,firstname=''):
         print("welcome",firstname)

     def show(self,firstname='',lastname=''):
         print("welcome",firstname,lastname)

obj= A()
obj.show()
obj.show('Nilima')
obj.show("Nilima","Barick")


# Program demonstrating polymorphism


class Shape:
     def area(self):
         print("area not defines")

class Rectangle(Shape):
     def __init__(self, length,width):
         self.length = length
         self.width = width
     def area(self):
         print("Rectangle Aera: ", self.length * self.width)

class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius

     def area(self):
         print("Circle Area: ", 3.14 * self.radius * self.radius)


shapes = [     Rectangle(5,3),
     Circle(4)
 ]
for shape in shapes:
     shape.area()


# Implement Encapsulation Using Getter And Setter

class Student:
    def __init__(self, name, marks):
        self.__name = name   # Private variable
        self.__marks = marks  # Private variable

    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def set_name(self, name):
        self.__name = name
        
    
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")
    
s1 = Student("Rahul", 85)
print("Name: ", s1.get_name())
print("Marks: ", s1.get_marks())

# Modifying data using setter
s1.set_name("Avijit")
s1.set_marks(95)

print("Update Name: ", s1.get_name())
print("Update Marks: ", s1.get_marks())


