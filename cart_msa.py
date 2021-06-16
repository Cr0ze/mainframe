"""
File: cart_msa.py
Author: Max Appleton (msa)

Purpose: This project will create a program that stores a list of products in a 
         shopping cart along with their prices. The user should have the ability to 
         add items to the list, remove them, and see the total price of the cart.
"""
#-----------------------------------------------------------------------------------
#############                 
# TEST CODE #                
#############                
#items = ['Bread', 'Carrots', 'Milk', 'Bagels', 'Chips', 'Gold Bars']
#prices = [2.50, 5.60, 9.99, 13.99, 4.50, 1865.31]
#quantity = [1, 2, 1, 10, 200, 1]
#-----------------------------------------------------------------------------------
#Create a list
items = []
prices = []
quantity = []
print('\nWelcome to the Shopping Cart Program!\n')

#Start the program
run = True

while run:

    #Menu
    print('Please select one of the following:\n1. Add item\n2. View cart\n3. Remove item')
    print('4. Compute total\n5. Quit')
    func_choice = int(input('Please enter an action: '))

    #Get user input to add to the list
    if func_choice == 1:
        #Get Item name
        item = input('\nWhat item would you like to add? ').capitalize()
        #Get item price
        cost = float(input(f"What is the price of '{item}'? "))
        #How many of the item
        quantity_of_item = int(input(f"How many '{item}' do you want to add to the cart? "))
        #Update the lists
        items.append(item)
        prices.append(cost)
        quantity.append(quantity_of_item)
        print(f"{quantity_of_item} '{item}' has been added to the cart.\n")

    #Display the List on prompt
    if func_choice == 2:
        print('\nThe contents of the shopping cart are:\n(item :quanity - price)')
        num = 0

        for position in range(len(items)):
            
            num += 1
            print(f'{num}. {items[position]:10}:{quantity[position]:^3} - ${prices[position]:.2f}')
        
        print('Prices are reflective of price per item\n')

    #Remove an item from the list
    if func_choice == 3:
        rm_item = int(input('\nWhich item would you like to remove? '))
        #Converting the user input to a base-0 index
        rm_item = rm_item - 1

        for position in range(len(items)):

            if position == rm_item:
                del items[position]
                del prices[position]
                del quantity[position]
                did_find = 'yes'
                break
            
            else:
                did_find = 'no'

        if did_find == 'yes':
            print('Item removed.')

        elif did_find == 'no':
            print('Sorry, that is not a valid item number.')
        
        print()

    #Display the total of the list
    if func_choice == 4:
        
        sum = 0
        for position in range(len(items)):
            sum += prices[position] * quantity[position]
        
        print(f'\nThe total price of the items in the shopping cart is ${sum:.2f}\n')

    #Exit the program
    if func_choice == 5:

        print('\nHave a nice day!')
        run = False
