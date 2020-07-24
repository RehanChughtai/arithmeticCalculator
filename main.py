def addition():
    print("Addition Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) + int(b)
    print("Your answer is: " , sum)

def subtraction():
    print("Subtraction Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) - int(b)
    print("Your answer is: " , sum)

def multiplication():
    print("Multiplication Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) * int(b)
    print("Your answer is: " , sum)

def division():
    print("Division Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) / int(b)
    print("Your answer is: " , "{0:.2f}".format(sum))

division()