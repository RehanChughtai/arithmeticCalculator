#Function to divide two user inputted values together
#and format to 2 decimal places
def division():
    print("Division Calculator")
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = int(a) / int(b)
    print("Your answer is: " , "{0:.2f}".format(sum))