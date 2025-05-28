#Create a dictionary named employee with keys "name", "id", and "salary" and assign values to them.
dict1 = {
    'name':'seema',
    'id':123,
    'salary': 10000
}
print(dict1)

#Print the "brand" of the product.
product = {"name": "Laptop", "price": 800, "brand": "Dell"}
print(product['brand'])

#Modify an existing value
#Change the "price" of product to 900.
product['price'] = 900
print(product)

#Add a new key-value pair
#Add "stock": 50 to the product dictionary.
product['stock'] = 50
print(product)

#Remove a key-value pair
#Remove "brand" from the product dictionary.
del product['brand']
print(product)

#Get the length of a dictionary
#Find the total number of key-value pairs in product.
print(len(product))

#Merge two dictionaries
#Given two dictionaries:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

#Convert dictionary keys to a list
#Convert the keys of product into a list.
dict1 = {
    'name':'seema',
    'id':123,
    'salary': 10000
}
print(list(dict1.keys()))
# print(dict1)

#Type Casting Questions:
#Convert a list of lists into a dictionary
var = [[1,2],[5,6]]
print(dict(var))

data = [["name", "Alice"], ["age", 25], ["city", "Paris"]]

#Convert data into a dictionary.
print(list(data))

#Convert a tuple of key-value pairs into a dictionary
data = (("name", "Bob"), ("age", 30), ("country", "USA"))
print(dict(data))
#Convert data into a dictionary.

#Convert a dictionary to a tuple of key-value pairs
print(tuple(data))
#Convert product into a tuple of key-value pairs.
print(tuple(product))

