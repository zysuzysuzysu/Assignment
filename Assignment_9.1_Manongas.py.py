''' 
Suzanne Marie Mannongas
Assignment 8.1
August 1, 2020

Creating a program that performs file processing activities:
	- using OS library to validate directory exist
	- prompt user for directory they would like to save the file and name of file
	- prompt user for their name, address, phone number
	- write data into comma separated line
	- read file written and display contents
'''

import os # importing OS library

def AskInformation():
	"""Get input information from user"""
	 # ask inputs from user and making sure its converted into strings
	name = str(input("Name: "))
	address = str(input("Address: "))
	phone_num = str(input("Phone number: "))
	return f"{name}, {address}, {phone_num}" # inputs will be formed in this output string when called

def main():
	""" Executes all for functionalitites needed for program. """
	directory = input("Which directory would you like your file to be saved? ") # ask input for the path of the directory
	filename = input("What file name do you want your files to be saved as? ") # ask input for the name of the text file

	program = Files(directory, filename)

	try: # 
		with open(os.path.join(directory, filename+".txt"),"w") as text_file: # checks if directory exists; join and writes new file to the path of the first argument; .txt means its a text file
			text_file.write(AskInformation()) # writes the information to the new file from passed function
	
		print(f"The Directory \"{directory}\" exists. Writing file \"{filename}\" in that directory....") # display output that directory exists

	except FileNotFoundError: # catches error if directory was not found
		print("Directory does not exist! Please create a new directory: ") # displays output that the directory was not found
		directory= input("") # ask user for new name for a creation of new directory and rewrites directory assignment
		os.mkdir(directory) # command creates new directory

		with open(os.path.join(directory, filename+".txt"),"w") as text_file: # checks if directory exists; join and writes new file to the path of the first argument; .txt means its a text file
			text_file.write(AskInformation()) # writes the information to the new file from passed function
	
		print("\nOutput Information:")
		with open(os.path.join(directory, filename+".txt"),"r") as read_file: # opens and reads file with the path of the directory
			contents = read_file.read()
			print(contents)

	else:
		print("\nOutput Information:")
		with open(os.path.join(directory,filename+".txt"),"r") as read_file: # opens and reads file with the path of the directory
			contents = read_file.read()
			print(contents)
main()