#Write a program that keeps taking input from the user and stops only when the user types "stop".
# running = True
# while running:
#     user_input = input("Enter something (type 'stop' to end): ")
#     print(f"You entered: {user_input}")
#     if user_input == "stop":
#         print("Program stopped.")
#         running = False

#Write a program to print the multiplication table of 5 using a while loop.
# num = 5
# i = 1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i+=1

#Write a program to print the square of numbers from 1 to 10 using a while loop.
# sqr = 1
# while sqr <=10:
#     print(f"square of: {sqr}={sqr**2}")
#     sqr+=1

#Write a program to calculate the sum of all odd numbers between 1 and 30 using a while loop.
# num = 1
# total = 0

# while num <= 30:
#     if num % 2 != 0:
#         total += num
#     num += 1

# print("Sum of all odd numbers from 1 to 30 is:", total)

#Print the characters in the string "Python" one by one.
word = "python"
vowels = "aeiouAEIOU"
count = 0
i = 0
while i< len(word):
    print(word[i])
    if word[i] in vowels:
        count += 1
    i+=1
print(count)
#Count vowels in a given string.