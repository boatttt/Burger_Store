#list to store ordered burgers
order_list = ['Beef Burger', 'Cheese Burger', 'Chicken Burger', 'Beef Burger']
#list to store order prices
order_cost = [8.50, 8.50, 8.50, 8.50]

cust_details = {'name':'Ryan', 'phone':'022098324', 'house':'27', 'street':'Blind', 'suburb':'Howick'}

def print_order():
    total_cost = sum(order_cost)
    print('Customer Details')
    print(f"Customer name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} \nCustomer Street Name: {cust_details['street']} \nCustomer Suburb: {cust_details['suburb']}")
    print()
    print('Order Details')
    count = 0
    for item in order_list:
        print('Ordered: {} Cost ${:.2f}'.format(item, order_cost[count]))
        count = count+1

    print()
    print('Total order cost')
    print(f'${total_cost:.2f}')

print_order()

