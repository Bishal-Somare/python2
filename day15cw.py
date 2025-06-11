#multiplication
# num = 2 #2fixed, constant

# a = int(input("Enter a number: "))
# for i in range(1,11,1):
#     print(f"{a}*{i}={a*i}")

#squares of number
# for sqr in range(1,11,1):
#     print(f"{sqr}^2={sqr**2}") #power ko lagi python ma double (**)

#all even number
# for eve in range(2,20,2):
#     print(eve)

#sum of numbers
s = 0
for sum in range(1,51,1):
    s +=sum
    # print(s) #bhitrw garda aauta aauta aauxa
print(s)

# sum of all odd numbers between 1 and 100 using a for loop.
sum = 0
for i in range(1,101,2):
    sum+=i #sum=sum+1 #1+3=4+5
print(sum)

#find the largest number in a list [2, 8, 1, 16, 5, 23, 7] using a for loop
list = [2, 8, 1, 16, 5, 23, 7]
largest=list[0]
for i in list:
    if largest<i: #2<2 #2<8<1 8<16<5 16<23<7
        largest=i #2 8 16 23
print(largest)



#while loop =  it execute the block of code as long as condition is true
#and terminates whenever condition is false
#true huda samma chalxa, range use hudaina
#syntax:

# while condition:
    #block of code

# while True:
#     print("hello")

#iteration\
# i = 0 #first iteration
# while i<8:
#     print(i)
#     if i==4:
#         print("welcome")
#     i+=1 #step iterartion

#multiplication table
# num = int(input("Enter a number"))
# i = 1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i+=1

# Write a program to print the squares of numbers from 1 to 10 using a whhile loop
# i=0
# while i<=10:
#     print(i)
#     i+=1

# Write a program to calculate the sum of numbers from 1 to 50 using a while loop
# i = 1
# sum=0
# while i<51:
#     sum+=i
#     i+=1
# print(sum)

# Write a program to calculate the sum of all even numbers between 1 and 20 using a while loop.
i =2
sum=0
while i<=20:
    if(i%2==0):
        print(i)
        sum+=i
    i+=1
print(sum)


#reverse
i = 10
while i>0:
    print(i)
    i-=1
