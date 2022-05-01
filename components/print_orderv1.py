#list to store ordered burgers
order_list = ['Beef Burger', 'Cheese Burger', 'Chicken Burger', 'Beef Burger']
#list to store order prices
order_cost = [8.50, 8.50, 8.50, 8.50]

count = 0
for item in order_list:
    print('Ordered: {} Cost ${:.2f}'.format(item, order_cost[count]))
    count = count+1