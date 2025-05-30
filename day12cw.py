#operator = symbol that perform operation betweenoperands
#a+b
#there are 7 types of operator in python
#1)Arithemetic operator
#addition,subtraction,multiplication,divison,modulus(%)-remainder
#power,floor(//) first divide but donot take decimal value
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #2%4=numenator small denomenator thulo numenator will come
print(a**b) #power
print(a/b) #floor(it doesnot take decimal value)

#relation operator and comparision operator(<,>,==,<=,>=,!=)
a=34
b=56
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)

#assignment operation(=), single euals to vaneko assign
a = 56
a = a+1
#or
a+=1 #a=a+1
a-=3 #a=a-3
a*=4 #a=a*4
print(a)

#logical operator(and or not)
#and = both operand should be true to return true in the output
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

#membership operator(in, not in), cha xaina
a = "My name is Seema"
print("my" in a) #false
print("My" in a) #true

print("my" not in a) #true
print("My" not in a) #false

#identity operator(is, is not), is le momory location herxa, == le value
a=[1,2,3]
b=[1,2,3]
print(id(a)) 
print(id(b))
print(a is b) #false , #memory location tracker
#difference
print(a==b) #true ,extact value

#bitwise operator(&,|,~,^)
#it takes integer and convert integer into binary
#and perform operation in bit
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