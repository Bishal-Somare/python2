#conditional_statement = making decision based on the value of variable
price = 45
#syntax:
#if condition: #comparison or relation operator
    #block of code
    #else: = condition didainam, jaba if ko part false huda else ko execute huncha
    #elif = condition add garna lai
    #if, else aauta use garni ani elif multiple times allow
if price > 50:
    print("price is greater")
else:
    print("price is smaller")


    #ticket system
# a = "welcome to our bus"
# print(a.center(70,"'"))

# age = int(input("Enter your age:"))
# if age <=12:
#     print("you have to pay rs200")
# elif age<=18 and age>12:
#     print("you have to pay rs 50") 
# elif age<=40 and age>18:
#     if age ==30:
#         print("no need to pay")
#     else:
#         print("you have to pay rs 80")
# else:
#     print("you have to pay rs 100")

    #nested if(if)

    #shorthand if
    a = 34
    if a>12:print("s is greater")

    #shorthand else if
    # a = 4
    # b = 7
    # print("a is smaller") if a<b else print("b is greater")

    # num = int(input("enter your number:"))
    # if num%2==0:
    #     print("even number")
    # else:
    #     print("odd number")

      
#jpt practice
x = "WELCOME!!"
print(x.center(50,"'"))
y = int(input("Enter your age: "))
if y<5:
    print("not eligible to play.")
elif y>=5 and y<=10:
    print("you have to pay ra10")
elif y>10 and y<=20:
    if y==15:
        print("no need to pay")
    else:
        print("you have to pay rs20")
else:
    print("You have to pay rs50")

