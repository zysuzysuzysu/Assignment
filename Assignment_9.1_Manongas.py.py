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

directory = input("\nWhich directory would you like your file to be saved? ")
filename = input("What file name do you want your files to be saved as? ")
filename = str(filename+".txt")

def main():
	try:
		with open(os.path.join(directory, filename)) as file:
			print(file.read())
	except:
		print("Directory does not exist! Creating a new directory named TEMP...")

	
if __name__=="__main__":
	main()