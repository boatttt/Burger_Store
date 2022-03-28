import random
from random import randint

 #List of names
names = ["Naomi", "Mio", "Rosmarie", "Kyle", "Dominicus", "Reigo", "Sheryl", "Lykke", "Hamid", "Sean"]

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

def main():
    '''
    Purpose: to run all the functions
    Parameters: None
    Returns: None 
    '''
    welcome()


main()