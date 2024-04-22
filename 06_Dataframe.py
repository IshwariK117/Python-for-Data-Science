# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:21:56 2024

@author: sai
"""

#Finding number or rows and columns in a dataframe

import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"oracle","java"],
              'Fee':[2000,2500,2600,2200,np.nan,2400,2100,2900],
              'Duration':['30days','40days','50days','60days','70days','80days','90days','67days'],
              'Discount':[11.8,23.7,67.5,45.6,34.6,12.5,99.4,90.3]})
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count

##############################################
df=pd.DataFrame(technologies)
row_count=df.shape[0] #returns number of rows
row_count
col_count=df.shape[1] #return number of columns
print(row_count)
print(col_count)

#using DataFrame.apply() to apply function and column
import pandas as pd
import numpy as np
data={"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
def add_3(x):
      return x+3
df2=df.apply(add_3)
df2

#####################################################3
#print only one column
df2=((df.A).apply(add_3)) #A is a colum name
print(df2)

#####################################
#using apply function to single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]
#Apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_4)
df

###############################################################################
#apply lambda function to single column
#using Dataframe.transform()

def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)



##############################################################################
#using numpy on single function
#using DataFrame.apply() & [] operator
import numpy as np
df["B"]=df['B'].apply(np.square)
print(df)

'''
     A    B   C
0  196  196   9
1  225  225  10
2  256  256  11

'''

#we can use Numpy.square() method
#using Numpy.square() and [] operator

df['A']=np.square(df['A'])
print(df)

###############################################################################
#pandas groupby() with example
technologies=({
    'courses':["spark","Pyspark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'fee':[22000,25000,23000,24000,26000,25000,25000,220000,15000],
    'duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
    
    })

df=pd.DataFrame(technologies)
print(df)


#use groupby() to compute the sum
df2=df.groupby(['courses']).sum()
print(df2)
'''
            fee      duration  discount
courses                                
Hadoop    48000  55days35days    1000.0
NA        15000        40days       0.0
Pandas    26000        60days    2500.0
Pyspark   25000        50days    2300.0
Python   244000  40days50days    2800.0
Spark     25000        30days    1400.0
spark     22000        30days    1000.0
'''

#group by multiple columns
df2=df.groupby(['courses','duration']).sum()
print(df2)
'''
                    fee  discount
courses duration                  
Hadoop  35days     25000       0.0
        55days     23000    1000.0
NA      40days     15000       0.0
Pandas  60days     26000    2500.0
Pyspark 50days     25000    2300.0
Python  40days     24000    1200.0
        50days    220000    1600.0
Spark   30days     25000    1400.0
spark   30days     22000    1000.0
'''

#add index to grouped data
#add row index to the group 
df3=df.groupby(['courses','duration']).sum().reset_index()
print(df3)
'''
 courses duration     fee  discount
0   Hadoop   35days   25000       0.0
1   Hadoop   55days   23000    1000.0
2       NA   40days   15000       0.0
3   Pandas   60days   26000    2500.0
4  Pyspark   50days   25000    2300.0
5   Python   40days   24000    1200.0
6   Python   50days  220000    1600.0
7    Spark   30days   25000    1400.0
8    spark   30days   22000    1000.0
'''




###############################################################################
import numpy as np
technologies={
 'courses':["spark","Pyspark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
 'fee':[22000,25000,23000,24000,26000,25000,25000,220000,15000],
 'duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
 'discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
 }

df=pd.DataFrame(technologies)
print(df)

df.columns

#get the list of all column names from headers
column_headers=list(df.columns.values)
print("the column jheader",column_headers)

column_headers=list(df.column)
column_headers



column_headers=list(df)
column_headers

