#define a function
def flow_control(k):

	#define a string based on the value of k
	if(k==0):
		s = "Variable k = %d equals 0." % k

	elif(k==1):
		s = "Variable k = %d equals 1." % k

	else:
		s = "Variable k = %d does not equal 0 or 1." % k #%d is a special character sign, python interprets this protected character, takes an input variable and with this we result in an integer, python uses % to tell itself "whatever follows this percent sign I need to place into the string"
		#These are the three types of if, or, otherwise type conditions
	# print the variable
	print(s)

#define a main function
def main():

	#decalre an integer
	i = 0

	# try flow_control for 0, 1, 2 #This designates the sequence at which commands operate
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

#run the program
if __name__=="__main__":
	main()