#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Nov 2020
# This program adds two numbers provided by the user
 
def main():

    # Input
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
 
    # process
    total = float(num1) + float(num2)
 
    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, total)) 


if __name__ == "__main__":
    main()
