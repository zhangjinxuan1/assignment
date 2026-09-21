#Name:Zhangjinxuan
#Assignment one
#ddl is22/9/2026 23:59pm
print("Simple Calculator")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
op = input("Choose operation(+,-,*,/):")
if op =="+":
	print("Result:",num1+num2)
elif op =="-":
	print("Result:",num1-num2)
elif op =="*":
	print("Result:",num1*num2)
elif op =="/":
	print("Result:",num1/num2)
else:
	print("Invalid operation")


