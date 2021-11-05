# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""
from re import search
from typing import Match
import contents

# this variable contains all the items in the vending machine.
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
items=[]#LIST WHICH HAS ALL THE ITEMS- The items are OBJECTS OF CLASS VENDING MACHINE

def load_vm(): #LETS PUT SOME DEFAULT ITEMS IN THE VENDING MACHINE
    vm1=contents.water
    items.append(vm1)  
    vm2=contents.chips
    items.append(vm2)
    vm3=contents.chocolate
    items.append(vm3)
    vm4=contents.energy_drink
    items.append(vm4)



    
def add_item():   
    print("       ADD Item")  
    ####

     
def buy_item():
    print("       Purchase Item")
    print("-" * 40, "\n")
    
    # Use the match function to find the item that the user wants to buy
    userinput=input("Please enter the item ID: ")
    found = False
    item_to_buy = search (userinput)
    #for item in items:
        #if  Match (userinput, item.itemID):
        #    item_to_buy = item
        #    found = True
        #    break
    # print error message if item is not found
    if item_to_buy is None: #found == False:
        print("No such item ID, try again!")
    else:
        # check that the item has stock available
        if item_to_buy.quantity > 0:
            # use calculate function to get the userinput and how much they are paying         
            calculate(item_to_buy)
            # reduce the stock level
            if item_to_buy.itemID == "A1":
                contents.water.quantity -= 1
            elif item_to_buy.itemID == "A2":
                contents.chips.quantity -= 1
            elif item_to_buy.itemID == "A3":
                contents.chocolate.quantity -= 1
            elif item_to_buy.itemID == "A4":
                contents.energy_drink.quantity -= 1           
        else:
            print("Empty slot for itemmID:", item_to_buy.itemID)


            
def calculate(item_to_buy):
    price = item_to_buy.price
    print("Item Price : $", price)
    #        CHECK BALANCE
    # loop until the price has been paid
    input_price = 0
    
    while input_price != price:   # loop while price is not fully paid.
        user_input = input("Enter Paid amount : $")
        #input_price = float(input("Enter Paid amount : $"))  
        input_price = float(user_input)  
        if input_price == price:
            print(input_price,"is correct. Transaction Complete. Enjoy!")
        elif input_price > price:
            change = input_price - price
            print("Here is your item and your change. Transaction Complete. Enjoy!", "\n", "$", change)
            # input_price -= change
            input_price = input_price - change
        elif input_price < price:
            price = price - input_price  # find remaining
            print("$", price, " still required:")
            input_price = 0   # This will force the loop to repeat
   
def search(search_itemID):          
        
    for item in items: # loop all the items
        if item.itemID == search_itemID:
            print (item.itemID,"found!") # check if the itemID matches the itemID in the parameter of this function.
            return item
         
    print (search_itemID, "not found")
         # return the item object if it was found.

def disp():
    # use a loop to print the items
    print("          Contents of VM")
    print("-"*40, end="\n\n")
    print("Items in VM (Total:", len(items), ")", sep="", end="\n\n")
    print("{}\t{}\t\t{}\t\t{}\t{}".format("NO#", "Item ID", "Price", "Quantity", "Item Name"))
    for count, item in enumerate(items, start=1):
        print("{}.\t{}\t\t${}\t\t{}\t\t{}".format(count, item.itemID, item.price, item.quantity, item.iname))

    #SHOW THE RECEIPTS TO USER 

    
def quit_vm():
     print() 
     print("Terminating ... ") 
     
