#sequence data type - list
#data structure and data format, collection of data
#mutable(orginal data changeable), allow dublicate value
#values, oder, data separated by comma
a= [12,32, 35, "seema", 20.5, "bipana"]
print(a)
print(type(a))
print(len(a))

#indexing: position
#variable_name[index]
print (a[1]) #32
print(a[-1])
print(a[3][0])#s

#slicing = acessing the part of the list
#syntax: variable_name[start:end:step]
print(a[0:4:1]) 
print(a[::]) #to print all
print(a[::-1]) #reverse
print(a[::3]) #increase steps
print(a[3][0:3]) #see

#allow dublicate values
b = [12,12,12,12,"hello","hello",78,78,78,78]
print(b)
print(len(b))

#mutable = orginal data change
b[0] = 34
print(b)

b[5] = 34
print(b)

b[-2] = "mam ji"
print(b)

#split()
a = "apple banana orange"
b = a.split()
print(b)