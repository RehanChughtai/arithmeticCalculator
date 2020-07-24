import addition

def getMenuChoice():
    #Prints menu options
    def menu():       
        print(30 * "-", "Arithmetic Calculator", 30 * "-")
        print("1. Addition Calculator ")
        print("2. Subtraction Calculator ")
        print("3. Multiplication Calculator ")
        print("4. Division Calculator ")        
        print("5. Exit Calculator ")
        print(83 * "-")

    loop = True
    int_choice = -1
    # While loop is True, continue iterating until False.
    while loop:          
        menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            int_choice = 1
            #Calls addition function on choice
            addition.addition()
            loop = True
        elif choice == '2':
            int_choice = 2
            #Calls subtraction function on choice
            subtraction()
            loop = True 
        elif choice == '3':
            int_choice = 3
            #Calls multiplication function on choice
            multiplication()
            loop = True
        elif choice == '4':
            int_choice = 4
            #Calls devision function on choice
            division()
            loop = True
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            #Loop becomes False and exits the script
            loop = False  
        else:
            #Any value other than 1-5 will validate as an error message to loop back to the menu
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]

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

#Call the function to activate the menu
getMenuChoice()