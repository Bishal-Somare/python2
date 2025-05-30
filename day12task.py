a = 9 #8 4 2 1 #1001
b = 11 #1011
#1001
#1011
#1 0 0 1 #9
print(a & b)

#for or
#1001
#1011
#1 0 1 1  #11
print(a | b)

#negation(~)
# 9 = -(9+1) = -10
#11 = -(11+1) = -(12)
print(~(a))
print(~(b))

#xor(^)exclusive or
#1001
#1011
#0 0 1 0 #2
print(a^b)

a=8 # 8 4 2 1 #1000
b=13 #1101
#1000
#1101
# 1 0 0 0 #8
print(a & b)

#for or
#1000
#1101
#1 1 0 1 #13
print(a |b)

#negation(~)
#8= -(8+1) = -(9)
#13 = -(13+1) = -14
print(~(a))
print(~(b))

#xor(^)exclusive or
#1000
#1101
#0 1 0 1 #5
print(a^b)

a=12 # 8 4 2 1 #1100
b=15 #1111
#1100
#1111
# 1 1 0 0 #12
print(a & b)

#for or
#1100
#1111
#1 1 1 1 #15
print(a | b)

#negation(~)
#12 = -(12+1) = -(13)
#15 = -(15+1) = -(16)
print(~(a))
print(~(b))

#xor(^)exclusive or
#1100
#1111
#0 0 1 1 #3
print(a^b)