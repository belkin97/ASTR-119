import numpy as np 	#imports numpy, a useful database
import sys 			#gives us access to a command line

#define a function that returns a value
def expo(x):
	return np.exp(x) 	#return the np e^x function (get access to the exponentiation function)

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) 	#call the expo function

#define a main function
def main():
	n = 10 	#provide a default function for n

	#check if there is a command line argument provided
	if(len(sys.argv)>1): #this counts the number of arguments
		n = int(sys.argv[1]) 	#if an argument was provided, use it for n (Reset n)

	show_expo(n) 		#call the show_expo subroutine


#run the main function
if __name__=="__main__":
	main()