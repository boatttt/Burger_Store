# Menu so that user can choose either pickup or delivery

print ("Do you want your order delivered or are you picking it up?")

print ("For pickup, enter 1.")
print ("For delivery, enter 2.")

while True:
    try:
        delivery = int(input ('Please enter a number '))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print ('Pickup')
                break

            elif delivery == 2:
                print ('Delivery')
                break

        else: 
            print('The number you enter must be 1 or 2')
    except ValueError:
        print ('That is not a valid number')
        print ('Please enter 1 or 2')