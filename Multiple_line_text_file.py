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
print(f"{Fore.GREEN}This program will write multiple line of text contents into a text file mylife.txt" +Fore.RESET)
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
        add_line = input(f"{Fore.GREEN}Do you want to enter another line? (Type 'y' if yes and any key if no:) " + Fore.RESET)
        print("="*85)
    #Loop will end when condition is not met

#Output will be printed in new text file (mylife.txt)

#Displaying output instructions
print("="*85)
print(f"{Fore.LIGHTGREEN_EX} Note: The output of the program will be displayed in a new tkinter window.", "\n" 
      " And a txt file (mylife.txt) containing the multiple lines will be created as well. "+Fore.RESET)
print("="*85)

#For displaying the output in new window 
#Read the text file
with open("mylife.txt", "r") as output_file:  
    #Import modules
    import tkinter as tk
    from tkinter import *
    # Define the lines to be printed
    lines = []
    #Iterating over the txt file
    for line in output_file:
        lines.append(line)

    # Initialize the current line index
    current_line = 0

    # Define the function to be called when the button is clicked  
    def on_button_click():
        global current_line
        #If statement
        if current_line < len(lines):
            output_label.config(text=lines[current_line])
            current_line += 1  
    
    #Create a new window
    root = tk.Tk()
    root.geometry("500x150") #Window size
    root.title("File Handling - Showing the lines in mylife.txt")  # Adding a title
    
    #Add a button to the window
    button = tk.Button(root, text="Click to reveal lines", command=on_button_click)
    button.pack()
    
    #Window background
    root.configure(bg="wheat")

    #Add a label to display the output text
    output_label = tk.Label(root, text="" , font=("Arial", 14), bg=root['bg'], fg = "SaddleBrown")
    output_label.pack()

    #Run the main loop method
    root.mainloop()

#Displaying a thank you message after the user closes the tkinter window
prog_design.program_footer()