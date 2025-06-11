# Write a program thagrade = int(input("Enter your grade: "))
# if grade >= 90:
#     print("Grade A")
# elif grade >= 80 and grade <=89:
#     print("Grade B")
# elif grade >= 70 and grade <=79:
#     print("Grade C")
# else:
#     print("Grade")

# t asks the user to enter a number and checks whether the number is odd or even

# a = int(input("Enter a number: "))
# if a%2==0:
#     print("It is a even number")
# else:
#     print("It is a odd number: ")

# Write a program that takes a score as input and assigns a grade based on the following criteria:
# 90 and above: Grade A
# 80–89: Grade B
# 70–79: Grade C
# Below 70: Grade 

# 

# Write a program to check if a person is eligible to vote. The eligibility age is 18 or above.

# age = int(input("Enter your age: "))
# if(age >= 18):
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
#or
#print("Eligible to vote ") if age >=18 else print("Not eligible to vote")

# Write a program that takes three numbers as input and prints the largest among them.

# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a second number: "))
# num3 = int(input("Enter a third number: "))
# if(num1>num2 & num1>num3):
#     print("num1 is greatest")
# elif(num2>num1 & num2>num3):
#     print("Num2 is greatest")
# else:
#     print("Num3 is greatest")

# Write a program to check if a given year is a leap year or not. A year is a leap year if:

# year=int(input("Enter a year: "))
# if(year%4 == 0 and year%100 != 0) or (year%40 == 0):
#     print("Year is a leap year")
# else:
#     print("Year is not a leap year")

# It is divisible by 4 but not divisible by 100, OR
# It is divisible by 40

# Write a program to implement a simple calculator. The program should:
# Ask the user for two numbers.
# Ask the user to choose an operation (add, subtract, multiply, divide).
# Perform the chosen operation and print the result

# string= "Calculator"
# print(string.center(70,"!"))
# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a second number: "))
# print("Choose Addition,Subtraction,Multiplication,Divide")
# s_choice = str(input("Choose:Add/Sub/Multipli/Divide: "))
# if(s_choice == "Add"):
#     print("Sum is:",num1+num2)
# elif(s_choice== "Sub"):
#     print("Subtraction is:",num1-num2)
# elif(s_choice== "Multi"):
#     print("Multiplication is:",num1*num2)
# else:
#     print("Divide is:",num1/num2)

# Write a program to print numbers from 1 to 100.

# a = range(1,100)
# print(a)

# If a number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# Otherwise, print the number itself

num = int(input("Enter a number"))
if num%3 == 0 and num%5==0:
    print("fizzBuzz")
elif num%5==0:
    print("Buzz")
elif num%3 == 0:
    print("Fizz")
else:
    print("Number")

# Given two variables x = 15 and y = 20, use conditional statements to print which variable is larger, or if they are equal.
# x = 15
# y = 20
# if(x>=y):print("")


#  Given a variable num = 7, use a conditional statement to check if the number is even or odd and print the result. 
# num = 7
# if(num%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")

# Write a Python Program to Check weather a candidate Eligible for Vote or not. 
# Write a Python program to check weather Given Number is Divisible by 7 or Not.
# num = int(input("Enter a number "))
# if(num%7==0):
#     print("Number is divisible by 7")
# else:
#     print("Number is not divisible by 7")

# Check if the value 10 is not present in the tuple t = (5, 15, 20, 25).

# t = (5,15,20,25)
# print(10 is not t)

# Determine if the value 25 is present in the list lst = [10, 20, 30, 40, 50] using a simple conditional statement

# lst = [10,20,30,40,50]
# print(25 is lst)

# Check if the value 100 exists in the set s = {50, 75, 100, 125}.
# s = {50,75,100,125}
# print(100 in s)