pizza_names = [ 'Beef burger', 'Cheese burger', 'Chicken burger', 'Beef and bacon burger',
             'Chicken and onion ring burger','Veggie burger', 'Fish burger',
             'Breakfast burger', 'Deluxe cheese burger','Deluxe chicken burger', 
             'Spicy Burger','Sean the sheep burger']

pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

def menu():
    number_pizza = 12

    for count in range(number_pizza) :
        print('{} {} ${:.2f}' .format(count+1, pizza_names[count],pizza_prices[count]))

menu()