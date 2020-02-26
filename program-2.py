#2.Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει ένα κείμενο από ένα αρχείο και χαρακτηρίζει κάθε λέξη ως καλή ή κακή, 
#ανάλογα με τα σύμφωνα που περιέχουν. Αν τα σύμφωνα f,c,k, και r είναι περισσότερα των άλλων, τότε η λέξη είναι “κακή”.


import string
import sys
import os

#Global
bad_consonants =['F','C','K','R']
consonants =['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']

def file_input():	
	while True:
		f_input = str(input("\n Please a enter file name i.e. '/../text.txt': ").strip())
		
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


def check_word(word):
	bad =0
	good=0
	for c in word:	
		if c.upper() in bad_consonants:
			bad+=1
		elif c.upper() in consonants:
			good+=1		
	if bad > good:
		return True
	else:
		return False
	
	
def good_bad(words):
	good_words=[]
	bad_words=[]
	for w in words:
		s = w.translate(str.maketrans('','',string.punctuation)) # remove punctuation
		if check_word(s):
			bad_words.append(s)
		else:
			good_words.append(s)
	
	#print ("The good words list is: {}".format(good_words), "\n\n")			
	print ("The bad words list is: {}".format(set(bad_words)),"\n\n")			
			
			
def Main():
	good_bad(list_words(file_input()))
	
if __name__=='__main__':
	Main()
	