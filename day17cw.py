#function = block of code that is executed whenever it is called
#code reusable
#code maintaibility

##two types of function
#1)inbuilt function
#2)user defined function

#inbuilt function = pre code or predefined
#print(),type(),len(),set(),list(),sum(),max(),min()

print(max(1,0,1))

print(min([True,2,3,8]))

print(min([1,2,False]))

#user defined = user leyh define garni function

#def function_name():    #snake case
    #block of code
#function baira call garni balla execute huncha

def show():
    print("hello")
show()

def my_function():
    a = 9
    b = 5
    #argument or parameter ma
    print(a+b)
my_function()

#two types of argument
# def show(argument-formal argument):
    #block of code
#formal vanni bitikai variable and actal ma call garda argumnet bhitra assign 
def show(a,b):
    print(a+b)
show(2,5)

def display(name,age):
    print(f"my name is {name}")
    print(F"my age is {age}")
display("seema",25)

#input from user
name = input("enter your name: ") #function bhitrw call garni haina,function call garna vanda aghi input liney
age = input("enter your age")

def display(name,age):
    print(f"my name is {name}")
    print(F"my age is {age}")
display(name,age) #
# diplay("seema,29") yo call huncha

#positional argument - position kyal garnu paro
#keyword argument - key sanga value pani diney, position farak pardaina key through lekhayra
#default argument - last ko argument lai diney, ek value kam
#Arbitary argument/variable 

#positional argument
def show(name,age):
    print(f"my name is {name}")
    print(F"my age is {age}")
show(56,"sita")

##keyword argument
def show(name,age):
    print(f"my name is {name}")
    print(F"my age is {age}")
show(age = 78, name="seema")

#default argument 
def show(name,age=80):
    print(f"my name is {name}")
    print(F"my age is {age}")
show(name="sita")

#Arbitary argument/variable 
#paila single *, balla double ** 
#1) arbitary position - * - select all , multiple value select
def show(*n):
    print(n)
show(1,2,3,"hello",80)

#2) arbitary keyword - ** - key ra value pair lina ko lagi use
def show(*a,**n): #args
    print(a)
    for i,j in n.items():
        print(i,j)
    show(1,2,3,4,"hello",name="sita",age=50)
