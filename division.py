# division using exception handling...
while True:
    try:
        first =int(input("enter first number : "))
        break
    except ValueError:
        print("invalid input.. please enter correct value..")
while True:
    try:
        second = int(input("enter second number : "))
        break
    except ValueError:
        print("invalid input.. please enter correct value..")

division = first / second
print(float(division))
