burger_names = [ 'Beef burger', 'Cheese burger', 'Chicken burger', 'Beef and bacon burger',
             'Chicken and onion ring burger','Veggie burger', 'Fish burger',
             'Breakfast burger', 'Deluxe cheese burger','Deluxe chicken burger', 
             'Spicy Burger','Sean the sheep burger']

burger_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

def menu():
    number_burger = 12

    for count in range(number_burger) :
        print('{} {} ${:.2f}' .format(count+1, burger_names[count],burger_prices[count]))

menu()