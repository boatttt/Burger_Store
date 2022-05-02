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