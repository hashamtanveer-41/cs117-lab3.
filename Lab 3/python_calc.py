# making a simple calculator on python.
# prompt user to input two numbers.

while True:
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))

 # now for operators we can use conditionals to check which operation the user wants
 operator= (input("Please Select your operator (+,-,*,/) "))

 if operator =='+':
    print("Result: " ,num1+num2)
 if operator =='-':
    print("Result: " ,num1-num2)
 if operator =='*':
    print("Result: " ,num1*num2)
 if operator =='/':
    if num2 == 0:
        print("math error cannot divide by zero")
    if (num2 !=0):
        print("Result: " ,num1/num2) 
 else:
    print("wrong operator selected")
 #now we ask user if he wants to check that his number is even or odd.
 evenodd =input("Plz type 'y' if u would like to check if the given numbers are even/odd ")

 if (evenodd=='y'):
    noselect=int(input("check no 1 or 2 for even/odd "))
    if (noselect==1 and num1 %2 == 0):
        print("num 1 is even")
    if(noselect==1 and num1 %2!= 0):
        print ("num 1 is odd")
    if(noselect==2 and num2 %2==0):
        print("num 2 is even")
    if(noselect==2 and num2 %2!=0):
        print("num 2 is odd")
 else:
    print("you have not selected even/odd check ")
 # now we ask user if he wants to check the percentages of each number
 percentage=(input("Please input 'y' if you would like to take percentages of the numbers "))
 if percentage == 'y':
    casepercent=int(input("please chose method for taking percentage,  1.num1/num2  2.num2/num1 "))
    if casepercent == 1:
        print((num1/num2)*100)
    if casepercent == 2:
        print ((num2/num1)*100)
       
 else :
    print("you have not chosen to take the percentage of the numbers ")
    
 exitCalculator = input("Do you want to exit the calculator (Y/N): ")
 if exitCalculator == 'y':
    print("Thank you for using the calculator.")
    break




