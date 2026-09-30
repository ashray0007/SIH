#This program contains a calculator

def sum(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b





while(1):

	print("\nList of operation")
	print("1. sum\n2. Subtract\n3. Multiply\n4. Divide")

	operation=input("\nWhich Operation do you want to perform ")


	if(operation=="1"):
		first_value=float(input("Enter first number "))
		second_value=float(input("Enter second value "))
		print("\nThe sum of given two numbers is:", sum(first_value,second_value))
		print("------------------------------------------------------")


	elif(operation=="2"):
		first_value=float(input("Enter first number "))
		second_value=float(input("Enter second value "))
		print("\nThe subtract of given two numbers is:", subtract(first_value,second_value))
		print("------------------------------------------------------")


	elif(operation=="3"):
		first_value=float(input("Enter first number "))
		second_value=float(input("Enter second value "))
		print("\nThe multiply of given two numbers is:", multiply(first_value,second_value))
		print("------------------------------------------------------")
	
	elif(operation=="4"):
	
		first_value=float(input("Enter first number "))
		second_value=float(input("Enter second value "))
		print("\nThe divide of ", first_value,"/",second_value," is ", divide(first_value,second_value))
		print("------------------------------------------------------")
	
	else:
		print("\nInvalid input,Please enter a valid input")
		print("------------------------------------------------------")


