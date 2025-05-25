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