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

print(os.getcwd())
print(os.listdir())

#filename = input("What file name do you want your files to be saved as? ")
#filename = str(filename+".txt")
directory = input("\nWhich directory would you like your file to be saved? ")

def main():
	check_if_exist = os.path.isdir(directory)
	if check_if_exist==True:
		print("Successful")
	elif check_if_exist == False:
		print("Directory does not exist! Please create a new directory: ")
		new_directory = input("")
		os.mkdir(new_directory)

main()