# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:01:45 2022

@author: Eremeeva Elena
"""

# for example: id_customers = [5475683, 2315454, 9999200, 1351654, 2511355, 1313515, 3899900]

def count_customers1 (n_customers):
    groups_customers = {}
    # Create dict, where key will be number of group, value will be count of customers
    
    for id_number in id_customers[:n_customers]:
        sum_digits = 0
    # id_customers[:n_customers] slice from the list with id_number of customers
        
        while id_number > 0:
            sum_digits += id_number%10
            id_number = id_number//10
        # Calculating the amount digits of id number customer
        
        if sum_digits not in groups_customers.keys():
            groups_customers[sum_digits] = 1
        # if key is absent, add key with value equal to 1
        
        else:
            groups_customers[sum_digits] += 1
        # else add value
            
    return groups_customers

# for example: print(count_customers1 (3))

def count_customers2 (n_customers, n_first_id):
    groups_customers = {}
    # Create dict, where key will be number of group, value will be count of customers
    
    first_index = id_customers.index(n_first_id)
    last_index = first_index + n_customers
    # first and last index fo slice
    
    for id_number in id_customers[first_index:last_index]:
        sum_digits = 0
    # id_customers[first_index:last_index] slice from the list with id_number of customers    
    
        while id_number > 0:
            sum_digits += id_number%10
            id_number = id_number//10
        # Calculating the amount digits of id number customer
            
        if sum_digits not in groups_customers.keys():
            groups_customers[sum_digits] = 1
        # if key is absent, add key with value equal to 1
        
        else:
            groups_customers[sum_digits] += 1
        # else add value
        
    return groups_customers

# for example: print(count_customers2 (5, 9999200))