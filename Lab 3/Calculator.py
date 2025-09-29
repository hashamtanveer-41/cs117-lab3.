print("------Calculator-----")

while True:

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the  second number: "))

    print("Please select the operation:")
    print("1. Addition \t 2. Multiplication")
    print("3. Subtraction \t 4. Division")
    print("5. Modulus of numbers \t 6. Exit")

    operation = int(input("Number associated with the operation:"))

    if operation == 1 :
        print("The sum of numbers is: ", number1+number2)
    elif operation == 2:
                print("The product of numbers is: ", number1*number2)
    elif operation == 3:
                print("The difference of numbers is: ", number1-number2)
    elif operation == 4:
                print("The division of numbers is: ", number1/number2)          
    elif operation == 5:
                print("The remainder of numbers is: ", number1%number2)
    elif operation ==6:
            print("Thank you for using the calculator.")
            break           
    else :
        print("Please Select the valid operation.")


