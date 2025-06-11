a = [
    "youtube.com",
    "facebook.com",
    "whatsapp.com"
]
a = [i.removesuffix(".com") for i in a] #extact hatauxa
print(a)

#decorator = function that takes another function argument and add some features and functionality(without changing structure)
#and return to a function
# code ko structure change nagari decorate garne, code reusability - 
# use for authentication like login logout , access control

#four points to remember
#1) Return type
def show():
    print("hello")
print(show()) # ans will be none cause return is not given

def show():
    print("hello")
    return 8
print(show())

#2) everything in the python is an object
def show():
    print("hello")
    #object
obj = show
obj()

#3) nested function
def outer():
    def inner():
        print("i am inner function")

    inner()
    print("i am outer function")
outer()

#4) a function can take another function as an argumrnt
def outer(a):
    def inner():
        print("i am inner function")
        a() #show()
    inner()
    print("i am outer")
def show():
    print("i am outside function")
outer(show) #here we pass function show as an actual arguments

#use method(@)
#@function ko nam jun ;ai call garni#extra features chaiyo vani
def outer(a):
    def inner():
        print("i am inner function")
        a()
    return inner
@outer
def show():
    print("i am outside function")
show()

#object oriented programming(OOP)
#part part ma break yesle simple banauxa , real world ma represents map
#class=blue print, layout, template, design
#object = instance of class , auta class ko multiple object banauna painxa
#regular expression = rezx