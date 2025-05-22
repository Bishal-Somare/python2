#first 5 character
a = "HelloWorld"
print(a[:5])

#slice & extract the last 4 character
a = "PythonProgramming"
print(a[13::])

#every 2nd character
a = "abcdefg"
print(a[0::2])

#reverse
a = "Palindrome"
print(a[::-1])

#result check
a = "DataSCience"
print(a[3:]) #aScience

#reverse  and extract every 2nd character
a = "abcdefgh"
print(a[::-2])

#extract subString "Intelli"
a = "ArtificialIntelligence"
print(a[10:17:1])

#concatenate
str1 = "Hello"
str2 = "World"
result = str1 + str2
print(result)