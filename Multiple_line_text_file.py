#Kate Eurisse L. Martinez_BSCPE1-5_Multiple line text contents file

#A Python program that contains a method that writes multiple line of text contents into a text file mylife.txt

#Create a text file named mylife.txt

#Open the text file
with open("mylife.txt", "w") as input_file:   
    #Initialize the loop control variable
    add_line = "y"
    #Loop condition
    while add_line == "y":
        #Ask the user to enter a line
        lines = input("Please enter a line: ")
        #Write the line into the text file mylife.txt
        input_file.write(lines + "\n")
        #Ask the user if he/she wants to input another line
    #Loop will end when condition is not met