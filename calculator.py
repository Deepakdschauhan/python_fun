#calculator
a = int(input("enter first number: "))
b = int(input("enter second number: "))
action =input( "enter action =  +, -, *, /, //, %  :")

if action == "+":
    print(a+b)
elif action == "-":
    print(a-b)
elif action == "*":
    print(a*b)
elif action == "/":
    print(a/b)
elif action == "//":
    print(a//b)
elif action == "%":
    print(a%b)
else:
    print("your input is wrong...")