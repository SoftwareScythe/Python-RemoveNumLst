
import os
import time

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")
#nt is a window check, if you are on window use cls, else clear(Mac)


best = [32,57,6,5,1,5,2,9,8,47,3,8,9,7,3,4,6,3,2,1,12,34]

def show_list(list):
	print("This is the list currently {}.".format(list))

def show_Quit():
	print("Enter 'Quit' to stop removing values")


while True:
	
	show_Quit()
	show_list(best)
	value = input("What number value you want to remove? ")
	
	

	if value.upper() == 'QUIT':
		break

	try:
		value = abs(int(value)) #abs is absolute value. This is here if user enters a negative number
	except ValueError: #This error checker here for none integers. If enter, make position None.
		value = None
		clear_screen()
		print("Please only enter number that are in the list, not words and letters. Try again.\n")
		continue

	index = 0
	while True:
		try:
			best.remove(value)
		except ValueError:
			if index == 0:
				clear_screen()
				print("There isn't any {}'s in the list currently.\n".format(value))
				break
			else:
				clear_screen()
				print("The value {} has been removed fully.\n".format(value))
				break
		index +=1


clear_screen()
print("Here's the final list: ")
show_list(best)
