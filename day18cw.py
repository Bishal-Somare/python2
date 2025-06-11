#lambda function = anynoumuous fumction that doesnot have identity
#identity hudaina so def use hudaina
#memory space kam , argument ra function same line ma huncha def ma xuta xutai
#similar to def function

#syntax: lambda argument:expression
a = lambda x,y,z:(x+y+z)/3
print(a(2,5,2))

#def show(x:
   #if x%2==0
#lambda takes less memory space
#fast performance
#it takes less time

#recurion function = a function calling again and again is called
#recursion limit 1000 provided by python
#recursion function

#function bhitra function lai call garda 1000 choti call huncha
# def show():
#     print("hello")
# show()

import sys #module sys= recursion limit check
print(sys.setrecursionlimit(3000)) #set recursion limit
print(sys.getrecursionlimit())

#two cases recursion
#1)base case(stopping case)
#2)recursion case

def show(n):
    if n == 30:
        return
    print("hello",n)
    show(n+1) #recursion case
show(0)

#factorial=n*(n-1)!
#5!=5*4*3*2*1
#1!=1
#0!=1

#return ma last ma print

def show(n):
    if n==0 or n==1:
        return 1
    return n*show(n-1) #5*4*3*2*1
print(show(5))

#0,1,1,2,3,5,8,13 n-1+n-2


def show(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return show(n-1)+show(n-2)
print(show(6))

#iterator = object that contain countable numbers of value eg list tuple set
#normal function not usable in iterator
#map() = inbuilt function, that takes function and iterator, simple location address garcha
#it applies function to each element
#syntax: map(function, iterator)

# def show(n):
#     return n
# n=2
# print(show(n))

def show(n):
    return n+2
n=[1,2,3,4]
a = map(show,n) #inbuilt function
print(list(a))

#lanbda ma use 
b = lambda x:x+2
n = [1,2,3,4]
a= map(b,n)
print(list(a))

#filter() = inbuilt function, takes function and iterator
#it process according to condition, chaini rakhxa nachaini filtero out
#filter(function, iterator)

# def show(n):
#     if n%2==0: #[2,4]
#         return n
# n=[1,2,3,4]
# a=filter(show,n)
# print(list(a))


#reduce() - inbuilt function that takes function and iterator
#2 argument takes
#iterator obj aauda use huncha
# from functools import reduce
# n  = [1,2,3,4,5]
# def sum(x,y):
#     return x + y
# a = reduce(sum,n)
# print(a)
