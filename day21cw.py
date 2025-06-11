#OOP=object oriented programming
#it breaks complex structure or complex program unto simpler program
#it is used to map real world concept or entity
#oop uses class and object
#class=blueprint of object or templates of creating object
#class has attributes and methods
#pascal case
#syntax:
# class ClassName:
    #attributes and methods
#object = instance of class
#syntax:
#object_name=ClassName()
#attributes it represents variable that stores data or value
#methods = similar to function that perform task
#class bhitra vayera function lai method bhaninxa
#object through call
#default parameter=self it contains current object

class Students:
    def show(self): #class bhitra ko method ma self hunai parxa
        print("hello")
ram = Students() #object
ram.show()


# __init__=dunder function or magic function
#it is a constructor it is automatically called when object of class is created
#it initalize variables

class Person:
    def __init__(self):
        print("hiii")
a=Person()

#variable lai initialize garna laibself use garnu parxa
# class Person:
#     def __init__(self):
#         self.name="seema"
#         self.age=90
#     def show(self):
#             print(f"my name is{self.name} and my age is {self.age}")

# a = Person()
# a.show()


class Person:
    def __init__(self,name,age): #parameters methods
        self.nm=name #attributes
        self.ag=age
    def show(self):
        print(f"my name is{self.nm} and my age is {self.ag}")
a = Person("seema",90) #value declare garnu vaxa vani class ko nam ma pass
# # print(a.nm) #class bitrw methods throuh, bahira obj through
# print(a.ag)
a.show()
# obj=Person()
# obj.show()

# obj1=Person()
# obj1.show()

#accessing attributes outside the class
#object_name.Variable_name

#attributes
#types
#instance variable class variable static variable
#methods types
#instance method class method static method

#instance method= each object has its own variable file, if we change variable in one object 
# it is applied for that object only
#it is define and initialize using self parameter

class Students:
     def __init__(self):
          self.name="bips"
          self.age=90
#class bhitra access garna ko lagi auta method banauni
     def show(self):
          print(f"my name is {self.name} and my age is {self.age}")
obj=Students()
obj.name="phibs"
obj.show()

obj1=Students()
obj1.show()

obj2=Students()
obj2.age=50
obj2.show()


