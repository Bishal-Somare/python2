#6) binary data type =
#i)bytes - memory management
#ii)bytearray

#bytes = it generates sequence of number, range(0,256)start & end value
# immutable(orginal data not changeable)
a = bytes([1,2,3,4,5,6,7,8,9,10,255])
print(type(a))
print(a)

print(a[-5]) #indexing
print(a[0:4]) #slicing

# a[0]=3
# print(a) #error deu to immutable
#bytearray = it generates sequence of numbers, range(0,256)
#mutable
a = bytearray([1,2,3,4,8,9,10,200])
print(type(a))
print(a)

a[0]=20
print(a)
#indexing and slicing same 

#boolean data type = True False
#True = 1,  False = 0
a = True
print(type(a))

a = False
print(type(a))

#None Type = absence of value
name = None
print(name)
print(type(name))

#Type casting and Type conversion(data conversion)
#data conversion = python interpeter
#converts one data type to another

a = 12
b = 67.78
c = a+b
print(type(c)) #float
print(c)

#type casting = developer converts one data type to another
a = 34
b = 56.67
c = int(a+b)
print(c)
print(type(c))

#string to int
a = int("20")
b = int("10")
c = (a+b)
print(c)
print(type(c))

a =[1,2,3]
b =[4,5,6]
d = tuple(a+b)
print(d)
print(type(d))

a =bool(1)
print(type(a))
print(a)

#data from user
#input() - inbuilt function
#asking data from user
hii=int(input("Enter your number: ")) 
print(hii)
print(type(hii))