# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:52:28 2024

@author: sai
"""
#pandas Dataframe-2-dimensional data structure
#immutable,heterogeneous tabular
#data structure with labeled axes rows,and column


#Dataframe features-
'''
support named rows and column
step1-go to anaconda navigator
2-select environment tab
3.by default it will be base terminal
4-on base terminal -pip install pandas

'''
#######################################################
'''
upgrade pandas to latest specific version
on base terminal write 
conda install -c anaconda pandas

#upgrade t specific version ==2.2.1
'''
#to check version
import pandas as pd
pd.__version__
#'2.0.3'

#########################################################
#craete pandas dataframe from list
import pandas as pd
technologies=[["spark",20000,"30days"],
              ["pandas",20000,"40days"]
              ]
df=pd.DataFrame(technologies)
print(df)
'''
        0      1       2
0   spark  20000  30days
1  pandas  20000  40days
'''
########################################################
#we give label to column and indexes ,dataframe by default assign 
#incremental sequence numners as labels '
#to both rows and columns ,these are  called Index
#add  column and row lables  to the DataFrame 
column_name=["courses","fee","duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_label)
print(df)
'''
  courses    fee duration
a   spark  20000   30days
b  pandas  20000   40days
'''
###########################################################
#check data type
df.dtypes
'''
courses     object
fee          int64
duration    object
dtype: object
'''

###########################################################
#we can also assign custom datatypes  to column
#set custom types to DatFrame

import pandas as pd
technologies={
    'courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
    'fee':[20000,25000,26000,22000,24000,21000,22000],
    'discount':[11.8,23.8,13.4,15.7,12.5,25.4,18.4]
    }
df=pd.DataFrame(technologies)
print(df)
'''
   courses    fee  discount
0    spark  20000      11.8
1  pyspark  25000      23.8
2   hadoop  26000      13.4
3   python  22000      15.7
4   pandas  24000      12.5
5   oracle  21000      25.4
6     java  22000      18.4
'''

print(df.dtypes)
'''
courses      object
fee           int64
discount    float64
dtype: object
'''

#convert all types to best possible types
df2=df.convert_dtypes()   #******convert object to string
print(df.dtypes)
'''
courses      object
fee           int64
discount    float64
dtype: object
'''

#change all columns to same type
df=df.astype(str)     #********convert string to object
print(df.dtypes)
'''
courses     object
fee         object
discount    object
dtype: object
'''

#change type for one or multiple columns
df=df.astype({"fee":int,"discount":float})
print(df.dtypes)
'''
courses      object
fee           int32
discount    float64
dtype: object
'''

#convert datatypes in all coumn which we mention in list
df=pd.DataFrame(technologies)
df.dtypes
cols=['fee','discount']
df[cols]=df[cols].astype('float')
df.dtypes
'''
courses      object
fee         float64
discount    float64
dtype: object
'''

#ignore error
df=df.astype({'courses':int},errors='ignore')
df.dtypes
'''
it will give error if we do not mention  => errors='ignore'
invalid literal for int() with base 10: 'spark': Error while type casting for column 'courses
'''

#generate errors
df=df.astype({'courses':int},errors='raise')
df.dtypes
'''
ValueError: invalid literal for int() with base 10: 
'spark': Error while type casting for column 'courses'
'''

#convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)

df['discount']=pd.to_numeric(df['discount'])
df.dtypes
'''
courses      object
fee          object
discount    float64
dtype: object
'''
########################################################
import pandas as pd
#create dataframe from dictionary
technologies={
    'courses':["spark","pyspark","hadoop"],
    'fee':[20000,250000,260000],
    'duration':['30days','40days','50days'],
    'discount':[1000,2300,1500]
    }
df=pd.DataFrame(technologies)
df

#convert dataframe to csv
df.to_csv('data_file.csv')
#after we check in our folder =>1-python ,csv file has created

##########################################################
#create dataframe from csv file
df=pd.read_csv('data_file.csv')

##########################################################
'''
TAKEAWAY-
how to give null values

'''













