#text data type = string-collection of one or more characters
#escape methods
intro = "python"
#even: (mid - 1/mid + 1)
print(len(intro))
mid = len(intro)//2-1
mid1 = len(intro)//2+1
print(intro[mid]) #t
print(intro[mid:mid1])

#slicing-accessing the part of the string
#syntax: variable_name[start:end:stop] - rule-end value ma +1
a = "my name is seema"
print(a[3:7:1]) #name
#eman
print(a[6:2:-1])
print(a[::]) #using slicing
print(a[::-1]) #reverse

print(a[2:]) #name is seema
print(a[:7]) #my name
print(a[::1]) #normal

