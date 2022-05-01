#list to store ordered burgers
order_list = ['Beef Burger', 'Cheese Burger', 'Chicken Burger', 'Beef Burger']
#list to store order prices
order_cost = [8.50, 8.50, 8.50, 8.50]

cust_details = {'name':'Ryan','phone':'022098324', 'house':'27', 'street':'Blind', 'suburb':'Howick'}

#print customer details
print('\n Customer Name: {} Customer Phone: \n{} Customer House Number: \n{} Customer Street Name: \n{} Customer Suburb: \n{}'.format( cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb'],))

count = 0
for item in order_list:
    print('Ordered: {} Cost ${:.2f}'.format(item, order_cost[count]))
    count = count+1