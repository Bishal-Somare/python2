#loop = repeating something over and over
#until particular condition is statisfied
#two types of  loop
#for loop
#while loop

#for loop = repeating something over and over
#until particular condition is statisfied
#condition satisfy nahuda samma chalxa

#range()=sequence data
#syntax:range(start,end,step)
# a=range(10)  #end=10 default stat=0 and default step=1
# print(a)

#for loop syntax:
#for index in variable(condition):
    #block of code

    #vertically
# for a in range(10):
#     print(a)

# #for horizontally
# for a in range(10):
#     print(a, end=" ") #space

for a in range(10):
    print(a)
if a==4: #print after 4
    print("hello")

for i in range(7,0,-1):
    print(i) #7 6 5 4 3 2 1

a = ["sita","hari","gita","ram"] #nested loop
for i in a:
    print(i)
    for j in i:
        print(j) # s i t a   h a r i   g i t a   r a m  