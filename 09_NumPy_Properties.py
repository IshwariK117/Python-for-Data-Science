# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:17:49 2024

@author: sai
"""

#ndarray.shape
#to get shape of Python NumPy

#shape
import numpy as np
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
#(2, 3)

#resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)



#NumPy also provide array.reshape
array=np.array([10,20,30],[40,50,60])
new_array=array.reshape(3,2)
print(new_array)

####################################################################
#arithmetic operation
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,3,2,4])

#add
add_arr=np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}")
'''
Adding two arrays:
[[ 1  4  4  7]
 [ 5  8  8 11]
 [ 9 12 12 15]
 [13 16 16 19]]
the output depends on the 0th rows of arr1 and 0th column of arr2
'''
#sub
sub_arr=np.subtract(arr1,arr2)
print(sub_arr)
'''
[[-1 -2  0 -1]
 [ 3  2  4  3]
 [ 7  6  8  7]
 [11 10 12 11]]
'''

#multiply()
mul_arr=np.multiply(arr1,arr2)
print(mul_arr)
'''
[[ 0  3  4 12]
 [ 4 15 12 28]
 [ 8 27 20 44]
 [12 39 28 60]]
'''


#div
div_arr=np.divide(arr1,arr2)
print(f"Divoiding two arrays:\n{div_arr}")

#reciprocal
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"after applying reciprocal function to array:\n{rep_arr1}")



#numpy.power()
#this function treat element in the first input array

arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(pow_arr1)
#[  27 1000  125]


arr2=np.array([3,2,1])
pow_arr1=np.power(arr1,arr2)
print(pow_arr1)
#[ 27 100   5]


#numpy.mod()
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr=np.mod(arr1,arr2)
print(f"after applying mod function to array:\n{mod_arr}")
#[1 0 1]


###########################################
#we can create an empty array
from numpy import empty
a=empty([3,3])
print(a)
'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

###############################################

np.__version__
# '1.24.3'
#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)

#create one array
from numpy import ones
a=ones([5])
print(a)


#create array with vstack
from numpy import array
from numpy import vstack
#first array
a1=array([1,2,3])
print(a1)
#second array
a2=array([4,5,6])
print(a2)

#vertical stack
a3=vstack((a1, a2))
print(a3) 
'''
[[1 2 3]
 [4 5 6]]
'''
print(a3.shape)


###############################################
#hstack
from numpy import array
from numpy import hstack
#first array
a1=array([1,2,3])
print(a1)
#second array
a2=array([4,5,6])
print(a2)

#horizontal stack
a3=hstack((a1, a2))
print(a3) 
#[1 2 3 4 5 6]

##################################################





