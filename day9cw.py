#union()
a = {1,2,3,4}
b = {2,4,5,6,7}
var = a.union(b)
print(var)

#intersection
var1 = a.intersection(b)
print(var1)

#difference
var2 = a.difference(b)
print(var2)

var3 = b.difference(a)
print(var3)

var4 = a.symmetric_difference(b)
print(var4)

a = {1,2,3,4}
b = {2,4,6}
var5 = a.issuperset(b)
print(var5)

var5 = a.isdisjoint(b)
print(var5)

#frozen set = frezee change nahuni
#immutable = orginal data not changeable
a = frozenset({1,2,3,4})
print(type(a))
print(a)

# a.add(23)
# print(a) #no method error

b = a.union({4,5,6,7,8})
print(b)

c = a.intersection({2,4,6,8})
print(c)

#map data type: dictionary = key value pair, mutable (orginal data change)
# single haina multiple pair ma
#dublicate key is not allowed
#order
#jati ota pair teti length
#syntax: dict_name{'key':'value'} key ma compolsory quation, value ma string anusar
#dict_name{
    #'key':'value',
   # 'key1': 'value2'
    #}

a = {
    'name': "seema",
    'age': 89
}
print(a)
print(len(a))
#or
a = dict(name = "seema", age = 34)
print(a)

# a = {}
#or
# a = dict()
# print(type(a))

#accessing value through key
#indexing
print(a['age']) #wrong halaypar error display

#get
print(a.get('age')) #invalid halda error dekhaudaina j lekhayxam tei dekhauxa

print(a.get('address'))


