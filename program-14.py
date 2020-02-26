#14.Γράψτε ένα πρόγραμμα σε Python το οποίο διαβάζει από ένα αρχείο έναν πίνακα 3x3 ο οποίος έχει γραφεί ως αρχείο κειμένου
#όπου κάθε γραμμή του είναι γραμμή του πίνακα #και τα στοιχεία διαχωρίζονται με κενά. 
#Ο πίνακας αποθηκεύεται με τη μορφή εμφωλευμένης λίστας και εμφανίζετε στον χρήστη την ορίζουσά του.


import string
import sys
import os

def file_input():	
	while True:
		f_input = str(input("\n Please enter a file name i.e. '/../text.txt':").strip())	
		if os.path.isfile(f_input):
			print (" File exist\n\n")
			break
		else:
			print ("File does not exist")
	
	return f_input


def list_rows(filename):
	try:
		file_in=open(filename,"r")
		matrix = [[int(num) for num in line.split()] for line in file_in if line.strip() !=""]
		assert  all([len(matrix)==len(row) for row in matrix]) is True
		#assert  any([len(matrix)!=len(row) for row in matrix]) is False
	except AssertionError:
			print("\n Can't find determinant matrix isn't square : " , matrix ,"\n\n")			
	except OSError:
		print("Can't open file {}".format(filename))
	print ("The matrix is: {}     Matrix dimension : {}x{}" .format(matrix,len(matrix),len(matrix[0])))
	
	return matrix
	
def det_2_by_2(mini):
	mini_det=(mini[0][0]*mini[1][1])-(mini[0][1]*mini[1][0]) 
	return mini_det
# [
#   a , b , c
#   d , e , f
#   g , h , i
# ]
def find_determinant(matrix):
	a, b, c = matrix[0]
	efhi = [x[1:] for x in matrix[1:]]
	dfgi = [x[::2] for x in matrix[1:]]
	degh = [x[0:2] for x in matrix[1:]]

	det = a*det_2_by_2(efhi) - b*det_2_by_2(dfgi) + c*det_2_by_2(degh)
	
	print ("\nThe Determinant of given Matrix is: {}".format(det),"\n\n")
	return 
	
	
def Main():	
	find_determinant(list_rows(file_input()))
	
if __name__=='__main__':
	Main()
	