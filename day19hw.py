# Create a list of odd numbers from 1 to 20 using list comprehension.
odd_num = [i for i in range(1,20) if i%2==1]
print(odd_num)

# Generate a list of squares of numbers from 1 to 10.
square = [x*x for x in range(1,11)]
print(square)

# Given a list [1, 2, 3, 4, 5], create a new list where each element is multiplied by 3.
list = [1, 2, 3, 4, 5]
b = []
[b.append(i*3)for i in list]
print(b)

# Given a list ["apple", "banana", "cherry"], create a new list with each word reversed.