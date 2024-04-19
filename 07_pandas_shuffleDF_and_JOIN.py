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
df3=df1.join(df2,lsuffix="_left",rsuffix="_right" ,how='right')
print(df3)
'''
   courses_left     fee duration courses_right  discount
r1       python  2000.0   30days         spark      2000
r6          NaN     NaN      NaN        python      3000
r3      pyspark  3400.0   35days          java      1000
r4       hadoop  1000.0   50days            go      2000
'''

###############################################################################

#pandas merging DataFrame
import pandas as pd
technologies={
    
    'courses':["python","spark","pyspark","hadoop"],
    'fee':[2000,2500,3400,1000],
    'duration':['30days','40days','35days','50days']
    }

index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)


technologies2={
        'courses':['spark','python','java','go'],
        'discount':[2000,3000,1000,2000]
    }

index_labels2=['r1','r6','r3','r4']
df2=pd.DataFrame(technologies2,index=index_labels2)


df3=pd.merge(df1,df2)
print(df3)
'''
  courses   fee duration  discount
0  python  2000   30days      3000
1   spark  2500   40days      2000
'''


#using DataFrame,merge
df3=df1.merge(df2)
print(df3)


import pandas as pdss
df=pd.DataFrame({'courses':['spark','pyspark','python','pandas'],
                 'fee':[2000,2000,3300,2000]})

df1=pd.DataFrame({'courses':['pandas','hadoop','hyperian','java'],
                  'fee':[25000,25300,24500,34222]})

#using pandas.concat() to concat two dataframe
data=[df,df1]
df2=pd.concat(data)
df2
'''
    courses    fee
0     spark   2000
1   pyspark   2000
2    python   3300
3    pandas   2000
0    pandas  25000
1    hadoop  25300
2  hyperian  24500
3      java  34222
'''



################################################################################
import pandas as pd
df=pd.DataFrame({'courses':['spark','pyspark','python','pandas'],
                 'fee':[2000,2000,3300,2000]})

df1=pd.DataFrame({'courses':['pandas','hadoop','hyperian','java'],
                  'fee':[25000,25300,24500,34222]})

df2=pd.DataFrame({'duration':['30days','40days','35days','60days','55days'],
                  'discount':[1000,2300,2500,2000,3000]})

df3=pd.concat([df1,df1,df2])
print(df3)
'''
   courses      fee duration  discount
0    pandas  25000.0      NaN       NaN
1    hadoop  25300.0      NaN       NaN
2  hyperian  24500.0      NaN       NaN
3      java  34222.0      NaN       NaN
0    pandas  25000.0      NaN       NaN
1    hadoop  25300.0      NaN       NaN
2  hyperian  24500.0      NaN       NaN
3      java  34222.0      NaN       NaN
0       NaN      NaN   30days    1000.0
1       NaN      NaN   40days    2300.0
2       NaN      NaN   35days    2500.0
3       NaN      NaN   60days    2000.0
4       NaN      NaN   55days    3000.0
'''




