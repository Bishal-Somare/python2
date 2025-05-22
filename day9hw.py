#Create a set with the following elements: 10, 20, 30, 40, 50.
#Add the element 60 to the set.
set = {10, 20, 30, 40, 50}
set.add(60)
print(set)

#Remove the element 20 from the set.
set.remove(20)
print(set)

#Find the length of the set  
print(len(set))

# Create two sets: a = {1, 2, 3, 4} and b = {3, 4, 5, 6}.
a = {1, 2, 3, 4} 
b = {3, 4, 5, 6}
#Perform the following operations:
#Find the union of both sets.
var = a.union(b)
print(var)

#Find the intersection of both sets.
var1 = a.intersection(b)
print(var1)

#Find the difference between  
var2 = a.difference(b)
print(var2)

#    find the symettrical differnce check if the set is subset,superset and disjoint
var3 = a.symmetric_difference(b)
print(var3) #false

var4 = a.issubset(b)
print(var4) #false

var5 = a.issuperset(b)
print(var5) #false

var6 = a.isdisjoint(b)
print(var6)

# 16)Determine if set1 = {1, 2, 3} is a subset of set2 = {1, 2, 3, 4, 5}.
set1 = {1, 2, 3} 
set2 = {1, 2, 3, 4, 5}
check = set1.issubset(set2)
print(check) #true

#17)Given set1 = {1, 2, 3} and set2 = {3, 4, 5}, find the elements that are in set1 but not in set2.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
diff = set1-set2
print(diff)

#18)Combine the unique elements from set1 = {1, 2, 3} and set2 = {2, 3, 4} into a new set.
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# new = set1.union(b)
# print(new)

#20)Remove the element 3 from the set s = {1, 2, 3, 4}
s = {1, 2, 3, 4}
s.remove(3)
print(s)

 #1. Create a dictionary with the following details:
  # python
   #student = {"name": "Alice", "age": 20, "grade": "A"}
student = {
    'name':"Alice",
    'age': 20,
    'grade': "A"
}
print(student)

   #1) Access the value of "age".
print(student['age'])

#2)access the value of grade
print(student['grade'])