#4.Γράψτε μια συνάρτηση η οποία μετατρέπει ένα string σε αριθμό σύμφωνα με την αναπαράσταση των αριθμών σε ASCII code 
#και μετά ελέγχει αν ο αριθμός είναι πρώτος. Για τον έλεγχο αν ένας αριθμός είναι πρώτος ΔΕΝ μπορείτε να χρησιμοποιήσετε εξωτερική βιβλιοθήκη.

import string
import sys

def string_input():	
	while True:
		try:
			s_input = str(input("\n Please Input a String :"))
			assert  any([char not in string.printable for char in s_input]) is False
		except AssertionError:
			print("\n Chars in input string must be : " , string.printable)			
		else:
			print ("\nThnx for the string :\)")
			break
	print ("\n Your Input string was: " , s_input)
	return s_input


def check_if_Prime(s):

	input=int(''.join(str(ord(c)) for c in s))
	print("\n...and it's number after we 've concatenated each char ( bckspace counts !) is {}: " .format(input) )

	if input > 1: 
		for i in range(2, input//2):
			if(input % i) == 0:
				print("\nThe number {} is not a Prime Number\n".format(input))
				break
		else:
			print ("\n{} is a Prime Number !!".format(input))
			print("\n\nThe largest known prime number has 24,862,048 digits, found by GIMPS in December 2018\n")
	else:
		print ("\n{} is a Prime Number !\n".format(input))		
	
		
def Main():
	check_if_Prime(string_input())
	
if __name__=='__main__':
	Main()