#Write an expression using arithmetic operators (+, -, *, /, %, //, **) with different numbers.
# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

#Use the assignment operator (+=, -=, *=, /=, %=, //=, **=) to modify a variable.
# c = 2
# print(c)
# c+=3
# print(c)
# c-=4
# print(c)
# c*=5
# print(c)
# c/=6
# print(c)
# c%=7
# print(c)
# c//=8
# print(c)
# c**=9
# print(c)

#Use a comparison operator (>, <, >=, <=, ==, !=) between two numbers.
# a=30
# b=50
# print(a<b)
# print(a>b)
# print(a==b)
# print(a<=b)
# print(a>=b)
# print(a!=b)

#Use logical operators (and, or, not) with boolean values.
a = True
b = False
print(a and b) #false

a = True
b = True
print(a and b) #true

#or = it return true whenever one operand it true
a = True
b = False
print(a or b) #true

a = False
b = False
print(a or b) #false

#not = reverse true = false false=true
print(not(a))
print(not(b))

#Apply the is and == operators on two variables with the same value.
a=[1,2,3]
b=[1,2,3]
print(id(a)) 
print(id(b))
print(a is b) #false , #memory location tracker
#difference
print(a==b) #true ,extact value

#Perform a bitwise AND (&), OR (|), XOR (^), NOT (~), operation on two numbers.
a=12 #1100
b=13  #1101
#& (and)
#1100
#1101
#pr
print(a & b)

# | (or) (8 4 2 1)rule
x = 11 #1 0 1 1
y=14 #1 1 1 0
#1011
#1110
#1 1 1 1
print(x |y)

#negation(~)
#~n= -(n+1) #1's -(14+1) -(-13)
#~n= (n+1) #2's complement
print(~(x))
print(~(y))

#xor(^)exclusive or
#it returns true when both operand diffent and return false
#when both operand is same
a =12
b=13
#1100
#1101
#0 0 0 1
print(a^b)

#Create an expression using a combination of arithmetic, comparison, and logical operators.
x = 6
y = 9
print(x*y>45 and x+y<23)#true

#Use the identity operator (is not) and membership operator (in, not in) in a single line
a = "My name is Seema"
b = "My name is"
print("My name is" in b and b is a ) #false

#Convert an integer into a float and a string.
a = 12
print(float(a))
#print(string(a))

b = 12.3
print(float(b))
#print(string(b))

#Convert a float into an integer and a string.
b = 3.5
print(int(b))        # Convert float to integer
print(str(b))        # Convert float to string

#Convert a string into an integer (if possible).
c = "123"
print(int(c)) 

#Convert a boolean (True or False) into an integer and a float.
d = True
print(int(d))        # Convert boolean to integer
print(float(d))      # Convert boolean to float

#Convert an integer into a boolean and explain the result
e = 0
print(bool(e))    
# Explanation: 0 → False, non-zero → True