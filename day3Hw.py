#1st char using -ve indexing
name = "HelloWorld"
print(name[-1])

#5th char - index 4
name = "HelloWorld"
print(name[4])

#2nd last character
name = "HelloWorld"
print(name[-2])

#middle character
a = "Python"
print(len(a))
mid = len(a)//2
print(a[mid])

#1st 5 character
s = "Programming"
print(s[:5:])

#1st r character
s = "Programming"
print(s[:4:])

#get char from index 2 t0 6(inclusive of index by 2, exclusive of 6)
s = "Programming"
print(s[2:7]) #inclusive
print(s[3:6])

#every 2nd char
s = "abcdefghij"
print(s[::2])

#reverse using slicing
s = "abcdefghij"
print(s[::-1])

#all char except the 1st & last
s = "abcdefghij"
print(s[1:-1])

#every 3rd char
index = "abcdefghij"
print(index[1:9:3])

#extract "gram" 
s = "Programming"
print(s[3:7])

#extract the substring
s = "DataScience"
print(s[4:7])

#extract "dfh" using step slicing
s = "abcdefghij"
print(s[3:8:2])