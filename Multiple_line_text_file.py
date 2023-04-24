#Kate Eurisse L. Martinez_BSCPE1-5_Multiple line text contents file

#A Python program that contains a method that writes multiple line of text contents into a text file mylife.txt

#Import certain modules for the program's design and text formatting
from colorama import Back, Fore, Style 
import prog_design

#Print header art for the program
prog_design.multiple_line_header()

#Ask the user's name and printing a greeting
print("//" * 20)
name = input(f"{Fore.RED} Enter your name: "+ Fore.RESET)
print("//"*20, "\n\n") 
print(Back.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, ("Hello " + name).center(84, "*") + Back.RESET, "\n")

#Display the program's instructions
print(f"{Fore.GREEN}This program will writes multiple line of text contents into a text file mylife.txt" +Fore.RESET)
print("="*85)
#Create a text file named mylife.txt

#Open the text file
with open("mylife.txt", "w") as input_file:   
    #Initialize the loop control variable
    add_line = "y"
    #Loop condition
    while add_line == "y":
        #Ask the user to enter a line
        lines = input(f"{Fore.RED}Please enter a line: "+Fore.RESET)
        #Write the line into the text file mylife.txt
        input_file.write(lines + "\n")
        #Ask the user if he/she wants to input another line
        add_line = input(f"{Fore.GREEN}Do you want to enter another line? (Type 'y' if yes and any key if no: " + Fore.RESET)
        print("="*85)
    #Loop will end when condition is not met