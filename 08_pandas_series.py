# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:59:29 2024

@author: sai
"""


import pandas as pd
#read excel file 
df=pd.read_excel(r'C:\Users\sai\Downloads\BitcoinHeistData')

print(df)

#########################################################################
#initialize dataframe and convert  into list form'
#using Series.values.tolist()



import pandas as pd
df=pd.DataFrame({'courses':['spark','pyspark','python','pandas'],
                 'fee':[2000,2000,3300,2000]})
print(df)
col_list=df["courses"].values.tolist()
print(col_list)

#['spark', 'pyspark', 'python', 'pandas']


#using list() function
col_list=list(df["courses"])
print(col_list)


import numpy as np
#convert numpy array
col_list=df['courses'].to_numpy()
print(col_list)



#arrays in numpy
#create ndarray
import numpy as np
arr = np.array([10,20,30])
print(arr)
"output:[10 20 30]#array"
a = [12,20,33]
print(a)
"output:[12, 20, 33]#list"
#difference between numpy and array
#ML is work on multidimentionl
#all the features of dataframe are called dimention
#
#create a multi-dimentional array
arr = np.array([[10,20,30],[40,50,60]])
#list inside list then we get multidimentional array
print(arr)
'''output:
    
    [[10 20 30]
     [40 50 60]]
'''
#represent the minimum dimentionas
#use ndmin param to specify how many minimum
#dimensions you wanted to create an array with minimum dimention
arr = np.array([10,20,30,40],ndmin =3)#convert array into 3 dimention
print(arr)
'''output:
    [[[10 20 30 40]]]
'''
#change the datatype
#dtype parameter
arr = np.array([10,20,30],dtype =complex)
print(arr)
'''output:
    [10.+0.j 20.+0.j 30.+0.j]
'''
#get the dimentions of array
#get dimention of the array

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)
print(arr)
'''output:
    
    print(arr.ndim)
    2

    print(arr)
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
'''
#finding size of each item in the array
arr = np.array([10,20,30])
print("each item conatin in bytes:",arr.itemsize)
#ndim is property using this we can find out
'''output:
    each item conatin in bytes: 4
'''
###########################
arr = np.array([10,20,30])
print("Each item is of the type",arr.dtype)
################################
#get the shape and size of array
#get shape and size of array
arr = np.array([10,20,30],[40,50,60],[70,80,90])
print("array size:",arr.size)
print("array shape:",arr.shape)
############
##create numpy array from list
#creation of arry
arr = np.array([10,20,30])
print("array:",arr)
#####################
#creating array from list with type float
arr = np.array([[10,20,30],[30,40,50]],dtype='float')
print("array created by using list:\n",arr)
########################
#create a sequence of intreger using arange()
#create a sequence of integer
#from 0 to 20 with steps of 3
arr = np.arange(0,20,3)
print("A sequence array with steps of 3:\n",arr)
'''output
print("A sequence array with steps of 3:\n",arr)
A sequence array with steps of 3:
 [ 0  3  6  9 12 15 18]
'''
#array indexing in numpy


#access single element using index
arr =np.arange(11)
print(arr)
'''output
[ 0  1  2  3  4  5  6  7  8  9 10]
'''
print(arr[2])
print(arr[-5])
#output:6



##############################################################
import numpy as np

# Create a 2D NumPy array
arr = np.array([[10, 20, 30, 40, 50], [20, 30, 40, 50, 30]])

# Print the array
print(arr)

# Print the shape of the array
print(arr.shape)

# Access an element in the array (indexing starts from 0)
print(arr[1, 1])  # Accesses the element at row 1, column 1



######################################################

#access element using slicing
np.array = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x=arr[1:8:2]
print(x)


########################################################

multi_arr = np.array([[10, 20, 30],
                      [40, 50, 60],
                      [60, 10, 20],
                      [12, 34, 56]])

print(multi_arr)
# Output:
# [[10 20 30]
#  [40 50 60]
#  [60 10 20]
#  [12 34 56]]

element = multi_arr[1, 2]
print(element)
# Output: 60


