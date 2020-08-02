''' 
Suzanne Marie Mannongas
Assignment 8.1
August 1, 2020

Creating a program that performs file processing activities:
	- using OS library to validate directory exist
	- prompt user for directory they would like to save the file and name of file
	- prompt user for their name, address, phone number
	- write data as a line of comma separated values
	- read file written and display contents
'''

import os # importing OS library

def AskInformation():
	"""Get input information from user"""
	 # ask inputs from user and making sure its converted into strings
	name = str(input("\n\tName: "))
	name = name.strip() # takes out any spaces before and after the input
	name = name.title() # name is ensured to be in Title case

	address = str(input("\tAddress: "))
	address= address.strip() # deleted spaces before and after input
	address = address.title() # address is in Title case

	phone_num = str(input("\tUS Phone number (XXX-XXX-XXXX): \n\t\t Please type the 10 digit numbers:  "))
	split_num_1 = phone_num[:3] # takes first 3 numbers
	split_num_2 = phone_num[3:6] # takes numbers from 4th to 6th number
	split_num_3 = phone_num[6:10] # takes numbers from 7th to 10th number; only take no more than 10 digits as input
	
	if len(phone_num)<10: # checks if length satisfies US phone numbers
		formatted_phone_num = f"{split_num_1}-{split_num_2}-{split_num_3}. Memo: missing digits." # puts memo that it is less than required amount
	elif len(phone_num)>10: # checks if length is more than 10
		formatted_phone_num = f"{split_num_1}-{split_num_2}-{split_num_3}. Memo: More than 10 digits have been detected, but was truncated." # puts memo for more than amount
	else: # satisfies the given amount
		formatted_phone_num = f"{split_num_1}-{split_num_2}-{split_num_3}" # string's new format

	return f"{name}, {address}, {formatted_phone_num}"

def main():
	""" Executes all for functionalitites needed for program. """
	directory = input("Which directory would you like your file to be saved? ") # ask input for the path of the directory
	filename = input("What file name do you want your files to be saved as? ") # ask input for the name of the text file

	try: # try running program
		with open(os.path.join(directory, filename+".txt"),"w") as text_file: # checks if directory exists; join and writes new file to the path of the first argument; .txt means its a text file
			print(f"The Directory \"{directory}\" exists. Writing file \"{filename}\" in that directory....") # display output that directory exists
			text_file.write(AskInformation()) # writes the information to the new file from passed function
		
	except FileNotFoundError: # catches error if directory was not found
		print("Directory does not exist! Please create a new directory: ") # displays output that the directory was not found
		directory= input("") # ask user for new name for a creation of new directory and rewrites directory assignment
		os.mkdir(directory) # command creates new directory

		with open(os.path.join(directory, filename+".txt"),"w") as text_file: # takes new directory the file inside as location
			text_file.write(AskInformation()) # writes the information to the new file from passed function
	
		print("\nOutput Information:") # display for output
		with open(os.path.join(directory, filename+".txt"),"r") as read_file: # opens and reads file with the path of the directory
			contents = read_file.read() # assign to contents and reads file
			print(contents) # prints file content

	else: # if the program runs smoothly, it will display this action
		print("\nOutput Information:") # display for output
		with open(os.path.join(directory,filename+".txt"),"r") as read_file: # opens and reads file with the path of the directory
			contents = read_file.read() # assigns and reads file
			print(contents) # prints file content

main() #calling of main() will execute the function