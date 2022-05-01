burger_names = [ 'Beef burger', 'Cheese burger', 'Chicken burger', 'Beef and bacon burger',
             'Chicken and onion ring burger','Veggie burger', 'Fish burger',
             'Breakfast burger', 'Deluxe cheese burger','Deluxe chicken burger', 
             'Spicy Burger','Sean the sheep burger']

burger_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered burgers and price
order_list =[]
order_cost = []

def menu():
    number_burger = 12

    for count in range(number_burger) :
        print('{} {} ${:.2f}' .format(count+1, burger_names[count],burger_prices[count]))

menu()


#ask for total number of burgers to order
num_burgers = 0

while True:
    try:
        num_burgers = int(input('How many burgers would you like to order? '))
        if num_burgers >=1 and num_burgers <=5: 
            break
        else:
            print('Your order must contain between 1 and 5 Burgers')
    except ValueError:
        print('That is not a vaild number.')
        print('Please enter between 1 and 5.')


print(num_burgers)

#choose burger from menu

print ('Please choose your burger by entering the number of the burger from the menu ')
for item in range(num_burgers):
    while num_burgers > 0:
        burger_ordered = int(input())
        burger_ordered = burger_ordered-1
        order_list.append(burger_names[burger_ordered])
        order_cost.append(burger_prices[burger_ordered])
        print('{} ${:.2f}' .format(burger_names[burger_ordered],burger_prices[burger_ordered]))
        num_burgers = num_burgers-1


