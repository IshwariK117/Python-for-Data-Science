# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:16:29 2024

@author: sai
"""

#arrays in NumPy
#create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)  
#[10 20 30]

#create a multi-dimnesional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
'''
[[10 20 30]
 [40 50 60]]
'''


#we canrepresent minimum dimension using ndmin
arr=np.array([10,20,30,40],ndmin=3)
print(arr)
#[[[10 20 30 40]]]

#we can also change the datatype using dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)
#[10.+0.j 20.+0.j 30.+0.j]


#get the dimension of the array
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)
print(arr)
'''
2

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''

#check the size of each item in array
arr=np.array([10,20,30,40])
print(arr.itemsize)
#4


##get the shape and size of array
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
print("array size",arr.size)
print("array shape:",arr.shape)
'''
array size 10
array shape: (2, 5)
'''



#creating array from list with float type
arr=np.array([[10,20,30],[40,50,60]],dtype='float')
print(arr)
'''
[[10. 20. 30.]
 [40. 50. 60.]]
'''


#create sequence of integers using arange()
#create sequnce of integersfrokm 0 to 20 with step of 3
arr=np.arange(0,20,3)
print("a sequntial array with step of 3",arr)
#a sequntial array with step of 3 [ 0  3  6  9 12 15 18]

####################################################################
#array indexing in NUMPY
arr=np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]

print(arr[2])


