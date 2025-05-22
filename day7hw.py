fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits[0])
print(fruits[-1])
print(fruits[2])

numbers = (10,20,30,40,50,60)
print(numbers[2])
print(numbers[-1])
print(numbers[1::1])

colors = ("red", "green", "blue", "yellow", "purple", "orange")
print(colors[0:3:1]) #Extract the first three elements.
print(colors[4::]) #Extract the last two elements.
print(colors[0:3:1]) #Extract every second element.
print(colors[::-1])

letters = ("a", "b", "c", "d", "e", "f", "g", "h")
print(letters[2:5:1]) #Extract ["c", "d", "e"]
print(letters[::2]) #Extract ["a", "c", "e", "g"]
print(letters[::-2]) #Extract ["h", "f", "d", "b"]

#tuple is immutable (not changeable)
# numbers = (1, 2, 3, 4, 5, 6)
# numbers[2] = 99
# print(numbers) #Change the third element to 99

words = ("Python", "is", "a", "great", "programming", "language")
print(words[1:4]) #Extract the words "is a great" using slicing.
print(words[::-1]) #Reverse the order of words