#Customer details dictionary
customer_details = {}

#Basic instructions
print('Please enter the pickup information')

#Customer name and details not blank
valid = False
while not valid:
    customer_details['name'] = input('What is your name? ')
    if customer_details['name'] != '':
        print(customer_details['name'])
        break

    else:
        print('Sorry, this cannot be left blank')

#Phone number and details not blank
valid = False
while not valid:
    customer_details['phone'] = input('Please enter your phone number ')
    if customer_details['phone'] != '':
        print(customer_details['phone'])
        break

    else: 
        print('Sorry, this cannot be left blank')

print(customer_details)