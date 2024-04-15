# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:59:58 2024

@author: sai
"""


#pandas datframe-basic operation
#create dataframe with NONE/NULL to work with example

import pandas as pd
import numpy as np
technologies=({
    'courses':["spark","pyspark","hadoop","python","pandas",None,"spark","python"],
    'fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'duration':['30day','50days','55days','40days','60days','35days','','50days'],
    'discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
'''
    courses      fee duration  discount
r0    spark  22000.0    30day      1000
r1  pyspark  25000.0   50days      2300
r3   hadoop  23000.0   55days      1000
r4   python  24000.0   40days      1200
r5   pandas      NaN   60days      2500
r6     None  25000.0   35days      1300
r7    spark  25000.0               1400
r8   python  22000.0   50days      1600
'''

###############################################################################

#Data frame properties
df.shape
#(8, 4)

df.size
#32
df.columns       # Index(['courses', 'fee', 'duration', 'discount'], dtype='object')
df.columns.values    #array(['courses', 'fee', 'duration', 'discount'], dtype=object)
df.index           #Index(['r0', 'r1', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8'], dtype='object')
df.dtypes   
'''
courses      object
fee         float64
duration     object
discount      int64
dtype: object
'''
df.info
'''
<bound method DataFrame.info of     courses      fee duration  discount
r0    spark  22000.0    30day      1000
r1  pyspark  25000.0   50days      2300
r3   hadoop  23000.0   55days      1000
r4   python  24000.0   40days      1200
r5   pandas      NaN   60days      2500
r6     None  25000.0   35days      1300
r7    spark  25000.0               1400
r8   python  22000.0   50days      1600>
'''
###############################################################################

#accesing one column content
df['fee']
'''
r0    22000.0
r1    25000.0
r3    23000.0
r4    24000.0
r5        NaN
r6    25000.0
r7    25000.0
r8    22000.0
Name: fee, dtype: float64
'''
#accesing two column content
cols=['fee','duration']
df[cols]
df[['fee','duration']]

#select certain row and assign to another DataFrame
'''******
df[rows,column]
df[ : , : ]
start from row 7 upto end
df[7: , : ]
'''
df2=df[6:]
df2
'''
   courses      fee duration  discount
r7   spark  25000.0               1400
r8  python  22000.0   50days      1600
'''

df2=df[:6]
df2
'''
    courses      fee duration  discount
r0    spark  22000.0    30day      1000
r1  pyspark  25000.0   50days      2300
r2   hadoop  23000.0   55days      1000
r3   python  24000.0   40days      1200
r4   pandas      NaN   60days      2500
r5     None  25000.0   35days      1300
'''
###############################################################################

#accessing certain column from 'Duration'
df['duration'][3]
#'40days'

#subtracting specifc value from a column
df['fee']=df['fee']-500
df['fee']
'''
r0    21500.0
r1    24500.0
r2    22500.0
r3    23500.0
r4        NaN
r5    24500.0
r6    24500.0
r7    21500.0
'''

#pandas to Manipulate DataFrame
#describe dataFrame
#gives 5 number summary...if we want to find representative no. i.e,mean
#only applicable to numeric data

df.describe()
'''
                fee     discount
count      7.000000     8.000000
mean   23214.285714  1537.500000
std     1380.131119   570.557372
min    21500.000000  1000.000000
25%    22000.000000  1150.000000
50%    23500.000000  1350.000000
75%    24500.000000  1775.000000
max    24500.000000  2500.000000
'''
###############################################################################
df=pd.DataFrame(technologies,index=row_labels)

#assign new header by setting new column names
df.columns=['A','B','C','D']
df
'''
          A        B       C     D
r0    spark  22000.0   30day  1000
r1  pyspark  25000.0  50days  2300
r2   hadoop  23000.0  55days  1000
r3   python  24000.0  40days  1200
r4   pandas      NaN  60days  2500
r5     None  25000.0  35days  1300
r6    spark  25000.0          1400
r7   python  22000.0  50days  1600
'''
###############################################################################

#rename column name using rename() method
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)   #axis =1 for column and axis=0 for rows
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2.rename(columns={'A':'c1','B':'c2'})    #output reflect only after this line
'''
         c1       c2      c3    c4
r0    spark  22000.0   30day  1000
r1  pyspark  25000.0  50days  2300
r2   hadoop  23000.0  55days  1000
r3   python  24000.0  40days  1200
r4   pandas      NaN  60days  2500
r5     None  25000.0  35days  1300
r6    spark  25000.0          1400
r7   python  22000.0  50days  1600
'''
###############################################################################
#DROP DATAFRAME ROWS AND COLUMNS
df=pd.DataFrame(technologies,index=row_labels)

#drop rows by labels
df1=df.drop(['r1','r2'])
df1

#delete rows by position and index
df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

#when you have defualt indexes for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0) # it will delete row 0 and row 3
df1
df1=df.drop(range(0,2))  #it will delete 0 and 1
df1




























