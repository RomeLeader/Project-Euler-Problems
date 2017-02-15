#!/usr/bin/python

def largest_palindrome_product():
    current_largest = 0
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            product = i*j
            if (str(product) == str(product)[::-1]): #Palindrome check on stringified numbers
                if product > current_largest:
                    current_largest = product
                    print(product)
    return

largest_palindrome_product()
