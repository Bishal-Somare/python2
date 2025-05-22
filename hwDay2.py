a = 2
b = 4
print(a, b)

a = 5
b = 1.5
c = a / b
print(c)

a = 2.5
b = 2
result = 2.5 * 2
print(type(result))

#complex numbers
complex_num1 = 2 + 3j
complex_num2 = 1 - 2j
print("Complex Addition: ", complex_num1 + complex_num2)
print("Complex Subtraction: ", complex_num1 - complex_num2)
print("Complex Multiplication: ", complex_num1 * complex_num2)
print("Complex Division: ", complex_num1 / complex_num2)
print()

#float numbers
float_num1 = 3.5
float_num2 = 1.5
print("Float Addition: ", float_num1 + float_num2)
print("Float Subtraction: ", float_num1 - float_num2)
print("Float Multiplication: ", float_num1 * float_num2)
if float_num2 != 0:
  print("Float Division: ", float_num1 / float_num2)
else:
  print("Cannot divide by zero")