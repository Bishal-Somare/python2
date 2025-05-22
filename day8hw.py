#Given t = (5, 10, 15, 20, 25), what is t[2]?
# What is the output of t[-1]?
t = (5, 10, 15, 20, 25)
print(t[2]) #15
print(t[-1]) #25

#Extract the first element using indexing.
#Extract the last element using negative indexing.
print(t[0])
print(t[-1])

#Given t = (1, 2, 3, 4, 5, 6, 7, 8, 9), extract the first 4 elements.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[0:4:1])

#Extract all elements except the last 3.
print(t[0:6:1])

#Get elements at even indices from t.
print(t[1::2])

#Reverse the tuple using slicing.
print(t[::-1])

#Extract every third element from t.
print(t[::3])

#Extract elements from index 3 to 7 (excluding 7).
print(t[2:6:1])

#Given two tuples tuple1  and tuple2 , concatenate them to form a new tuple.
tuple1 = ("seema", 10)
tuple2 = ("bipana", 20)
c = tuple1 + tuple2
print(c)

#Given the tuple my_tuple = (10, 20, 30, 40, 50), slice the tuple to get the last three elements.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[-3::])

#Find the length of the tuple my_tuple = ('a', 'b', 'c', 'd').
my_tuple = ('a','b','c','d')
print(len(my_tuple))
            
#Given s = {10, 20, 30, 40}, add the element 50 to the set.
s = {10, 20, 30, 40}
s.add(50)
print(s)

#Remove the element 20 from the set s = {10, 20, 30, 40}.
s.remove(20)
print(s)

#What happens when you try to remove an element that is not in the set? Try removing 100 from s = {10, 20, 30}.
#s = {10, 20, 30}
#s.remove(90)
#print(s) #keyError

#Create an empty set and add multiple elements {5, 10, 15} to it.
hello = set({})
hello.update({"seema",10})
print(hello)
