# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:03:42 2024

@author: sai
"""
#1.Write a Python function that takes two lists and returns True if they have at least one common  member
def common_member(list1, list2):
    # Convert lists to sets for efficient membership checking
    set1 = set(list1)
    set2 = set(list2)
    
    # Check if there's any common element between the sets
    if set1.intersection(set2):
        return True
    else:
        return False

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(common_member(list1, list2))  # Output: True



#2.Use list comprehension to construct a new list but add 6 to each item.
list1=([1,2,3,4,5])
new_list=[x+6 for x in list1]
print(new_list)
#output:[7, 8, 9, 10, 11]
    

#3.write python program to reverse a sring
original_string="Hello , Python"
rev_string=original_string[ : :-1]
print(rev_string)
#output:nohtyP , olleH


#4.write python program to iterate over dictionaries using for loop
dict1={'a':4,'b':6,'c':5,'d':8}
for key,value in dict1.items():
    print(key,value)
'''
output:
    a 4
    b 6
    c 5
    d 8
'''

#5.Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.
original_dict = {'a': 1000, 'b': 2500, 'c': 3000}
filtered_dict = {key: value for key, value in original_dict.items() if value > 2000}
print(filtered_dict)  # Output: {'b': 2500, 'c': 3000}



#6.Open the file data.txt using file operations
import pandas as pd
with open('iris.csv','r') as file:
    df=pd.read_csv('iris.csv')

print(df)   


#7python program to print 0th index and 4th index
import numpy as np
arr1=np.array([11,22,33,44,55])
print(arr1)
print(arr1[0])          #output:11
print(arr1[4])          #output:55

#8.Write a Python program to filter a list of integers using Lambda.
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter even numbers using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
print("Even numbers from the list:", even_numbers)
# Filter odd numbers using lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))
print("Odd numbers from the list:", odd_numbers)




#9. Write a Pandas program to create the specified columns and rows from a given data frame.  
import pandas as pd
dataset={
    'name': ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19] ,
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1] ,
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] ,
    'labels': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
    }
df=pd.DataFrame(dataset)
print(df)
'''
      name  score  attempts qualify labels
0     Anna   12.5         1     yes      a
1     Dinu    9.0         3      no      b
2     Ramu   16.5         2     yes      c
3     Ganu    NaN         3      no      d
4    Emily    9.0         2      no      e
5   Mahesh   20.0         3     yes      f
6   Jayesh   14.5         1     yes      g
7   venkat    NaN         1      no      h
8     Ajay    8.0         2      no      i
9  Dhanesh   19.0         1     yes      j
'''


#10.define array  data array=([11,22,33,44,55]) and slice it form 0 to 4
import numpy as np
arr2=np.array([11,22,33,44,55])
print("slicing from 0 to 4",arr2[ :4])       #it excludes 4th index [0:3]
#output : slicing from 0 to 4 [11 22 33 44]


 