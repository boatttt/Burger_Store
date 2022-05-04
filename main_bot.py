import sys
import random
from random import randint

#List of names
names = ["Naomi", "Mio", "Rosmarie", "Kyle", "Dominicus", "Reigo", "Sheryl", "Lykke", "Hamid", "Sean"]
#lists to store variables
customer_details = {}
order_list = []
order_cost = []

# validates inputs to make sure that they aren't blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != '':
            return response
        else: 
            print('This cannot be left blank')
# validates inputs to check if theya re an integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else: 
                print (f'Please enter a number between {low} and {high} ')
        except ValueError:
            print ('That is not a vaild number')
            print (f'Please enter a number between {low} and {high} ')
# welcome message
def welcome():

    '''
    Purpose: to generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
   

    num = randint(0,9)

    name = (names[num])

    print('*** Welcome to Sean the Sheep Burgers ***')
    print('*** My name is ',name, '***')
    print("*** I will help you order your delicious Sheep Burger ***")

# pickup or delivery menu
def pickupmenu():
    del_pick = ''
    LOW = 1 
    HIGH = 2

    question = (f'Enter a number between {LOW} and {HIGH} ')
    print ("Do you want your order delivered or are you picking it up?")
    print ("For pickup, enter 1.")
    print ("For delivery, enter 2.")

    delivery = val_int(LOW, HIGH, question)
    
    if delivery == 1:
        print ('Pickup')
        del_pick = 'pickup'
        pickup()          

    else:
        print ('Delivery')
        order_list.append('Delivery Charge')
        order_cost.append(9)
        del_pick = 'delivery'
        deliver()

    return del_pick

#pickup function

def pickup():

#Basic Instructions
    question = ('Please enter your name ')
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])


    question = ('Please enter your phone number ')
    customer_details['phone'] = not_blank(question )
    print(customer_details['phone'])

#delivery function
def deliver():
    
#Basic Instructions

    question = ('Please enter your name ')
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ('Please enter your phone number ')
    customer_details['phone'] = not_blank(question )
    print(customer_details['phone'])

    question = ('Please enter your house number ')
    customer_details['house'] = not_blank(question )
    print(customer_details['house'])

    question = ('Please enter your street name ')
    customer_details['street'] = not_blank(question )
    print(customer_details['street'])

    question = ('Please enter your suburb name ')
    customer_details['suburb'] = not_blank(question )
    print(customer_details['suburb'])

# Burger menu function

burger_names = [ 'Beef burger', 'Cheese burger', 'Chicken burger', 'Beef and bacon burger',
             'Chicken and onion ring burger','Veggie burger', 'Fish burger',
             'Breakfast burger', 'Deluxe cheese burger','Deluxe chicken burger', 
             'Spicy Burger','Sean the sheep burger']

burger_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

def menu():
    number_burger = 12

    for count in range(number_burger) :
        print('{} {} ${:.2f}' .format(count+1, burger_names[count],burger_prices[count]))

#burger order function
def order():

    num_burgers = 0
    LOW = 1 
    HIGH = 5
    MENU_LOW = 1
    MENU_HIGH = 12

    question = (f'Enter a number between {LOW} and {HIGH} ')
    print('How many burgers do you want to order?')
    num_burgers =val_int(LOW, HIGH, question)
    for item in range(num_burgers):
        print('Please choose your burgers by entering the number from the menu.')
        question = (f'Please enter a number between {MENU_LOW} and {MENU_HIGH} ')
        burger_ordered = val_int(MENU_LOW, MENU_HIGH, question)

        burger_ordered = burger_ordered-1
        order_list.append(burger_names[burger_ordered])
        order_cost.append(burger_prices[burger_ordered])
        print('{} ${:.2f}' .format(burger_names[burger_ordered],burger_prices[burger_ordered]))
        num_burgers = num_burgers-1

#order printing function
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print('Customer Details')
    if del_pick == 'delivery':
        print('Your order is for delivery. A $9 delivery charge has been applied.')
        print(f"Customer name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} \nCustomer Street Name: {customer_details['street']} \nCustomer Suburb: {customer_details['suburb']}")

    elif del_pick == 'pickup': 
        print('Your order is for pickup')
        print(f"Customer name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} ")
    print()
    print('Order Details')
    count = 0
    for item in order_list:
        print('Ordered: {} Cost ${:.2f}'.format(item, order_cost[count]))
        count = count+1

    print()
    print('Total order cost')
    print(f'${total_cost:.2f}')

def confirmation():
    print ("Please confirm your order")

    print ("To confirm, please enter 1.")
    print ("To cancel, please enter 2.")

    while True:
        try:
            confirm = int(input ('Please enter a number '))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ('Order Confirmed')
                    print ('Your order has been sent to our kitchen and will be with you shortly.')
                    break

                elif confirm == 2:
                    print ('Order Cancelled')
                    print ('You can restart the order or exit.')
                    break

            else: 
                print('The number you enter must be 1 or 2')
        except ValueError:
            print ('That is not a valid number')
            print ('Please enter 1 or 2')

def new_exit():
    print ("Do you want to start another order or exit ?")

    print ("To start another order enter 1.")
    print ("To exit the bot enter 2.")

    while True:
        try:
            confirm = int(input ('Please enter a number '))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ('New order')
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break

                elif confirm == 2:
                    print ('Exit')
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    sys.exit()
                    break

            else: 
                print('The number you enter must be 1 or 2')
        except ValueError:
            print ('That is not a valid number')
            print ('Please enter 1 or 2')








def main():
    '''
    Purpose: to run all the functions
    Parameters: None
    Returns: None 
    '''
    welcome()
    del_pick = pickupmenu()
    menu()
    order()
    print_order(del_pick)
    confirmation()
    new_exit()

main()  