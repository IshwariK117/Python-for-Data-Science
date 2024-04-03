# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:08:24 2024

@author: sai
"""

#series -used to model ONE DIMENSIONAL DATA
#similar to list in python
#all  features are dimension
#all rows is called data model
#series object has #index and name/labels
import pandas as pd

#the index can be string based as well
#in which case pandas indicate
#that the datatype for the index is object

songs2=pd.Series([145,142,38,13],name='counts')
songs2.index

songs3=pd.Series([145,142,38,13],name='count',
                 index=['Paul','John','George','Ringo'])
songs3.index
songs3
###########################################################

#in series there is name and in numpy there is number
#numeric value will become NaN when you load datset
#None,NaN ,nan,and null are synonyms

import pandas as pd
f1=pd.read_csv('age.csv')
f1
df = pd.read_excel(r'C:/1-Python/Bahaman.xlsx')

#the series object behave similarly to a Numpy array.
import numpy as np
numpy_ser=np.array([145,142,38,13])
songs3[1]     # 142

numpy_ser[1]  #142
#they both have methods
songs3.mean()    #84.5
numpy_ser.mean()   #84.5

####################################################
#PANDAS series data structure provides support for basic CRUD
#column name should not have space 
#crud operation
george=pd.Series([10,7,13,1],
                 index=['1965','1978','1970','1970'],
                 name='George_Songs')
george
#whenever we want repeted index metion exclusive index

#without name it gives defult integer value but they are not unique
george=pd.Series([10,7,13,1],
                 name='George_Songs')
george
#########################################################

#Reading
#read or select data from series
george['1970']
'''
output:
1970    13
1970     1
'''
#we can iterate data in a series
for item in george:
    print(item)
    '''
    output:
    10
    7
    13
    1
    '''
    
############################################
#update - to update we used standard index assignment operator
george['1978']=68
george
'''
1965    10
1978    68
1970    13
1970     1
Name: George_Songs, dtype: int64
'''


















