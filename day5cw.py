#string inbuilt methods
#string is immutable beacause change garna mildaina 
# method lai call garna . garinxa
#pthon is case sensative
#upper() = it chance string into uppercase
a = "my name is SEEMA"
b = a.upper()
print(b)

#lower() = lower case
c = b.lower()
print(c)

#swapcase() = covert lower to upper and upper to lower
b = a.swapcase()
print(b)

#capitalize = covert all the char into lower but first letter capital
b = a.capitalize()
print(b)

#startswith()
a = "welcome to name education"
b = a.startswith("w") #true
b = a.startswith("ff") #false
print(b)

#endswitch()
b = a.endswith("hh") #false
b = a.endswith("tion") #true
print(b)

#count() it count the number of character in the given string
hello = "my name name name is seema"
b = hello.count("name") #3
b = hello.count("bips") #0
print(b)

#find() = it finds index
d = "my name is seema"
e = d.find("m") #0
e = d.find("m", d.find("name")) #5
print(e)

#index()
# b = a.index("z")
# print(b)

#replace()
var = "welcome to nepal"
b = var.replace("nepal", "ktm")
print(b)

#strip() = head ra tail ko matra space hatauxa, bich ko hatauna
a = "!!wel! come!!"
b = a.strip("!") #wel! come
# b = a.removesuffix("!!") #!!wel! come
# b = a.removeprefix("!!") #wel! come!!
print(b)

#center() = center ma leuni
var = "welcome to name education"
print(var)
print(len(var))
b = var.center(60, "'") #25 char bich ma aru divide huncha aru side ma
print(b)