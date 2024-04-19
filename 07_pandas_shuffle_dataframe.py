# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:03:46 2024

@author: sai
"""

import pandas as pd

technologies={
      'courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
      'fee':[20000,25000,26000,220000,24000,21000,22000],
      'duration':['30days','40days','35days','40days','60days','50days','55days'],
      'discount':[1000,2000,25000,2300,3400,3400,3200]
    }

df=pd.DataFrame(technologies)
print(df)

#shuffle the dataframe rows rows and return all rows
df1=df.sample(frac=0.5)
print(df1)
'''
   courses     fee duration  discount
6     java   22000   55days      3200
4   pandas   24000   60days      3400
5   oracle   21000   50days      3400
3   python  220000   40days      2300
2   hadoop   26000   35days     25000
1  pyspark   25000   40days      2000
0    spark   20000   30days      1000
'''

###############################################################################
#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)
'''
   index  courses     fee duration  discount
0      2   hadoop   26000   35days     25000
1      5   oracle   21000   50days      3400
2      1  pyspark   25000   40days      2000
3      3   python  220000   40days      2300
4      6     java   22000   55days      3200
5      4   pandas   24000   60days      3400
6      0    spark   20000   30days      1000
'''

###############################################################################

import pandas as pd
technologies={
    
    'courses':["python","spark","pyspark","hadoop"],
    'fee':[2000,2500,3400,1000],
    'duration':['30days','40days','35days','50days']
    }

index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)
print(df1)
'''
    courses   fee duration
r1   python  2000   30days
r2    spark  2500   40days
r3  pyspark  3400   35days
r4   hadoop  1000   50days
'''

technologies2={
        'courses':['spark','python','java','go'],
        'discount':[2000,3000,1000,2000]
    }

index_labels2=['r1','r6','r3','r4']
df2=pd.DataFrame(technologies2,index=index_labels2)
print(df2)
'''
   courses  discount
r1   spark      2000
r6  python      3000
r3    java      1000
r4      go      2000
'''
#pandas join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)
'''
   courses_left   fee duration courses_right  discount
r1       python  2000   30days         spark    2000.0
r2        spark  2500   40days           NaN       NaN
r3      pyspark  3400   35days          java    1000.0
r4       hadoop  1000   50days            go    2000.0
'''





#inner join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right" ,how='inner')
print(df3)
'''
  courses_left   fee duration courses_right  discount
r1       python  2000   30days         spark      2000
r3      pyspark  3400   35days          java      1000
r4       hadoop  1000   50days            go      2000
'''



#left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right" ,how='left')
print(df3)
'''
   courses_left   fee duration courses_right  discount
r1       python  2000   30days         spark    2000.0
r2        spark  2500   40days           NaN       NaN
r3      pyspark  3400   35days          java    1000.0
r4       hadoop  1000   50days            go    2000.0
'''                               

#right join















