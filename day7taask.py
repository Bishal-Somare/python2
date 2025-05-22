my_list = [10, 20, 30, 40, 50]
b = my_list[2]
print(b)

new_list = [10,20,30,40,50]
b = new_list[0:3]
print(b)

str = "apple,banana,cherry"
b = str.split(",")
print(b)

my_list = [1,2,3]
b = my_list*3
print(b)

list = ["hello",45,67,89.90,45,45,"apple","orange"]
list.append(34)
print(list)

list.extend([20,30,40]) # adding multiple value
print(list)

print(list[6][0:3]) #app extract

list.remove("orange")
print(list)

list.clear()
print(list)

a = [33,"seema",66]
b = [34,"bipana",55]
c = a+b
print(c)

#for int
z = [33,32,31,30,]
z.sort()
print(z)

b = sorted(z, reverse=True)
print(b)

#for string
name = ["seema","bipana","reeeenaa","bips"]
name.sort(key = len, reverse=True)
print(name)

c = sorted(name,key = len)
print(c)