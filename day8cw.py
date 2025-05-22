#set data type = set = collection of data, mutable(orginal data changeable),
#doesnot allow duplicate values
#unorder

a = {1} #empty rakhaypar dictonary & value halepar set
#or
# a = set()
print(type(a))

#position fixed hudaina & every time change
#no indexing and slicing
b = {32,"seema",45,"bipana",3+4j,23}
print(b)
#or
c = set({35,"seema",45,"bipana",3+4j,25})
print(c)

#dublicate value is not allowed
d = set({35,35,35,"seema",45,45,"seema","bipana",3+4j,25})
print(len(d))

#mutable
#set inbuilt methods
#adding methods
#1)add() = single data only add, if multiple error comes
# randomly bich ma basxa , last ma aaudaina, everytime change position
d.add(90)
print(d)

#update() = multiple data adding in set
#multiple data halda set ko {} hunu paryo
d.update({100,"bips","rana"})
print(d)

#deleting methods
#1)pop() = harek choti change huni print gareko agadi ko data remove garxa
data = set({"seema","bipana",22,33,44,"bips"})
print(data.pop())
print(data)

#2)remove() = particular data removes
# data.remove("seema") #navako data halda error
# print(data)

#discard() = particular data removes
data.discard(22) #navako data halda error dekhaudaina, set ja print garxa
print(data)

#clear() = all contain or data removes, empty set rakhxa
data.clear()
print(data)

#del it remove whole set
del data
print(data)
