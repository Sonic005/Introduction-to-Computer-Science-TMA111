#1.Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει τις πέντε μεγαλύτερες λέξεις ενός κειμένου το οποίο διαβάζει από αρχείο 
#και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα.

import string
import sys
import os

#Global
vowels = ['A','E','I','O','U']

def file_input():	
	while True:
		f_input = str(input("\n Please enter a file name i.e. '/../text.txt' : ").strip())
		
		if os.path.isfile(f_input):
			print ("File exist\n\n")
			break
		else:
			print ("File not exist")
	
	return f_input


def list_words(filename):
	words=[]
	try:
		file_in=open(filename,"r")
		words=[word for line in file_in for word in line.split()]
	except IOError:
		print("There is no such file")
	
	return words
	
	
def five_largest_words(words):
	result_words=[]
	words.sort(key=len , reverse=True)
	print ("The words list is: {}".format(words), "\n\n\n\n")			
	for word in words[:5]:
		word =''.join(char for char in word if char.upper() not in vowels)
		s = word.translate(str.maketrans('','',string.punctuation)) #remove punctuation
		result_words.append(s)

	print ("The Result list without vowels in reverse order is: {}".format(result_words[::-1]),"\n\n")
	
	
def Main():	
	five_largest_words(list_words(file_input()))
	
if __name__=='__main__':
	Main()
	