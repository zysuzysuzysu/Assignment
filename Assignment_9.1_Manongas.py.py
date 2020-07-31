''' 
Suzanne Marie Mannongas
Assignment 8.1
July 30, 2020

Creating a program that performs file processing activities:
	- using OS library to validate directory exist
	- prompt user for directory they would like to save the file and name of file
	- prompt user for their name, address, phone number
	- write data into comma separated line
	- read file written and display contents
'''

import os.path
import json

print(os.getcwd())
print(os.listdir())

def AskInformation():
	name = input("Name: ").split(",")
	address = input("Address: ").split(",")
	phone_num = input("Phone number: ").split(",")
	information = name + address + phone_num
	return information
	
def main():
	directory = input("Which directory would you like your file to be saved? ")
	filename = input("What file name do you want your files to be saved as? ")

	try:
		with open(os.path.join(directory, filename+".txt"),"w") as text_file:
			json.dump(AskInformation(), text_file)

	except FileNotFoundError:	
		print("Directory does not exist! Please create a new directory: ")
		new_directory = input("")
		os.mkdir(new_directory)

		with open(os.path.join(new_directory, filename+".txt"),"w") as text_file:
					json.dump(AskInformation(), text_file)
	else:		
		print("Output Information:")

		with open(os.path.join(directory, filename+".txt"),"r") as read_file:
			contents = read_file.read()
			print(contents)



main()