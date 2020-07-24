
#Function to add two user inputted values together
def addition():
    print("Addition Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) + int(b)
    print("Your answer is: " , sum)

#Function to subtract two user inputted values together
def subtraction():
    print("Subtraction Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) - int(b)
    print("Your answer is: " , sum)

#Function to multiply two user inputted values together
def multiplication():
    print("Multiplication Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) * int(b)
    print("Your answer is: " , sum)

#Function to divide two user inputted values together
#and format to 2 decimal places
def division():
    print("Division Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) / int(b)
    print("Your answer is: " , "{0:.2f}".format(sum))

division()