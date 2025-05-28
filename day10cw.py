a = {
    'name':'rita',
    'age': 89
}
# # print(a)

# #mutable(orginal data changeable) 
# #key through change
# a['name'] = "sita"
# a['age']=45
# print(a)

# #order 
# # pair add = key and value last ma add, single single value add
# a['address'] = 'butwal'
# a['email'] = 'seema@gmail.com'
# print(a)

#update
#multiple pair together add
b ={
    'email':'seema@gmail.com',
    'subject':'computer',
    'age':90,
    'address':'ktm'
}
a.update(b)
print(a)

#deleting method = key through
#del = single single pair delete garxa palai palo
del a['address']
del a ['age']
print(a)

#pop()
a.pop('name')
print(a)

#popitem() = last ko item delete
a.popitem()
print(a)

# keys method le keys matra output
#value method le value matra dinxa
#items method key value pair duitai dinxa
s = {
    'name':'seema',
    'age': 9
}
print(s)
print(s.keys())
print(s.values())
print(s.items())

#make a dictionaary that takes
#student marks in diffrent
#subject and print their average percentage
info = {
    'account':90,
    'economics':80,
    'math':70,
    'nepali':80,
    'english': 85,
    'finance': 95
}
c = sum(info.values())
print(c)
d = len(info)
average = c / d #total divide by len
print(average)

#nested dictionary
y = {
    'emp1':{
        'name':'seema',
        'age':90
    },
    'emp2':{
        'name':'bipana',
        'age':90
    }
}
print(y)
#change
y['emp1']['name']='hari'
print(y)

y['emp1']['address'] ='pokhara'
print(y)

#value access
print(y['emp1']['address'])