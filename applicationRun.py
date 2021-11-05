# -*- coding: utf-8 -*-
"""
Created on:

@author: 
"""
import userFunctions

# define the main menu
def menu():
    print("*"*40)
    print("     Vending Machine    ")
    print("*"*40)
    print("1. Buy")
    print("2. See options")
    print("3. Quit")
    print()
# end of menu function.
# define the login in function
def login():
    enteredID=input("\n\nPlease enter your MIT ID:")
    file = open("dataBase.txt")  # open the file
    readfile = file.read()  # read the file.
    file.close()  # close the file after reading.

    if enteredID in readfile:
        print('MIT ID', enteredID, 'Found In File. Please make your selection.')  # if it is present, return True
        return True
   
    if enteredID not in readfile:
        print('MIT ID', enteredID,
              'Unorthorised. Please try again.')  # If the ID is not in the file, print unauthorized
        return False
# end of login function


# define the main procedure             
def main():

    userFunctions.load_vm()          #Load default items in the VM

    userFunctions.disp()             # Display what VM has.

    o = login()  # this runs the login function. If it is successful o will be True, otherwise False.
    
    while(True):
        if o is False:
            o = login()
            continue  # the continue statement will skip the rest of the code and go back to the top of the loop.

        print("\n")
        print("Welcome to MIT Vending Machine")

        menu()                      # prints the menu on the screen.
        option=input("What would you like to do?")      # this is what the user enters.
        if  option=="1":            # The user wants to buy a product
            userFunctions.disp()
            print()
            print("What would you like to buy? (Press 3 to Cancel)")
            userFunctions.buy_item()
        elif option=="2":            # The user wants to display all items

            userFunctions.disp()
        
        elif option=="3":            #The user wants to quit their session
            userFunctions.quit_vm()
            break                    # break will end the loop and thus exit the program.

        else:
            print(option)
            print("Invalid menu option!");
# end of main procedure
       

main()#Python will execute code from this point
        
        
        
        
