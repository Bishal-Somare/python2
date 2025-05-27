student = {
    'name':'Alice',
    'age':20,
    'grade':'A'
}
print(student['age']) #access the value of "age"

student['grade']="A+" #chamge the value of "grade" to "A+"
print(student)

student['city']="New York" #add a new key "city" with the value of "New York"
print(student)

student.pop("age") #remove the "age"
print(student)

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
dict1.update(dict2)
print(dict1)

#retrieve "london " and '25from the dictionary
data = {
    'person':{
        'name':'john',
    },
    'info':{
        'age':25,
        'city':'london'
    }
}
print(data['info']['city'])
print(data['info']['age'])