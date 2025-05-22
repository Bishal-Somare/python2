#list in builts method
#append() = adding methods, single data add garni
a = [12,90,88,"hello","world"]
a.append(56)
print(a)

# a.append([45,67,"tina"])
# print(a)

#extend() = multiple data adding in list
a.extend({57, "world","sita","hari"})
print(a)

#insert()
a.insert(1, "jeet")
print(a)

#deleting methods
#1)pop() #stack (LIFO)
a.pop(2) #khali huda last ma jun cha teslai suru ma delete garxa, index rakhaysi tei anusar delete
# print(a.pop())
print(a)

#remove() = particular data removes
a.remove("world") #jun delete garni tei data lekhni
print(a)

#clear() #all clear
a.clear()
print(a)

# del a   #all clear
# print(a)

#sorting = accending & decending
#inbuilt method sort() inbuilt function sorted()
c = [4,3,7,9,8,6,5,2] #decending
c.sort(reverse=True)
print(c)

a = [6,7,2,1,3,4,5]
b = sorted(a, reverse=True)
print(b)

#string sort
a =["apple","pea","orangesss","pineapplesss"]
a.sort (key = len, reverse=True) #decending order 
print(a)

b = sorted (a, key=len,reverse = True)
print(b)

#tuple = sequence data type, collection of data, data is separated by comma
#data structure and data format, order, immutable(orginal) data not changeable
#allow dublicate values
#position fixed
a = (122,23.4,"seema","bips")
print(type(a))
print(a)
print(len(a))

#immutable
#methods - donot have methods
#performance faster than list - data change & update garna mildaina

#sequence data type = range() = it generates sequence of number, order
#syntax: range(start,end,step)

a = range(10) #end = 10 default start = 0 default step = 1 = 0 1 2 3 4 5 6 7 8 9 ans
print(type(a))
print(a)

b = range(2,11,3) #2 5 8
print(b)

c = range(5,0,-1) #5 4 3 2 1
print(c)

#indexing 
a = range(10)
print(a[-1])

#slicing: variable_name[start:end:step]
print(a[2:6:1])
print(a[-4::])
