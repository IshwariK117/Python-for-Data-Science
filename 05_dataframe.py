# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:05:40 2024

@author: Sai
"""
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySparks","Hadoop","Python",None,"C++"],
    'Fee':[2000,3000,5000,4000,np.nan,1000],
    'Duration':['30days','20days','45days','60days','55days','35days'],
    'Discount':[100,200,300,400,500,50]
        })
df = pd.DataFrame(technologies)
df2 = df.iloc[[2,3,4]]#Select rows by index list
df2 #Select rows by index list 
df2 = df.iloc[1:5] #select rows byinteger index
df2
df2 = df.iloc[:1]#select first row
df2
df2 = df.iloc[:3]#select first 3 row
df2
df = df.iloc[-1:] #select last row
df2
df = df.iloc[-3:]  #select last three row
df2
df = df.iloc[::2]#select alternate row

#############
#select rows by index Labels
df2 = df.loc['r2'] #select row by label
df2
#whenever we are write multiple row we need to give 
df2 = df.loc[['r2','r3','r6']]#select rows by index labels
df2
df2 = df.loc['r1':'r5']#select rows by label index row
df2
df2 = df.loc['r1':'r5':2]#select alternate rows with index
df2
##########################################

#pandas select  columns by name or index
#by using df[] notation
df2 = df['Courses']
#select multiple columns
df2 = df[['Courses','Fee','Duration']]

#using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
#seleect multiple columns

df2 = df.loc[:,['Courses','Fee','Duration']]
#Select random columns
df2 = df.loc[:,['Courses','Fee','Discount']]
df2
#select columns between two columns
df2 = df.loc[:,'Fee':'Discount']
df2
#select columns by range
df2 = df.loc[:,'Duration':]
df2
#select columns by range All the columns upto duration
df2 = df.loc[:,:'Duration']
df2
#select every alternate columns
df2 = df.loc[:,::2]
df2
##################################
#####################
#Pandas.DataFrame.query() by example
#Query all rows with Courses equals 'Spark'
df2= df.query("Courses == 'Spark'")
print(df2)
##############
#not equals condition
df2 = df.query("Courses != 'Spark'")
print(df2)
####################################33
#############################3
###############################
#Pandas  Add column to DataFrame
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySparks","Hadoop","Python",None,"C++"],
    'Fee':[2000,3000,5000,4000,np.nan,1000],
    'Duration':['30days','20days','45days','60days','55days','35days'],
    'Discount':[100,200,300,400,500,50]
        })
df = pd.DataFrame(technologies)
print(df)

###############################3
#Add column to Dataframe
#Add new  column to the DataFrame

tutors = ['Ram','sham','radha','Ghansham','Ganesh','Ramesh']
df2 = df.assign(TutorAssiged=tutors)
print(df2)
################################
#Add multiple column to the dataframe
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df.assign(MNC=MNCCompanies,tutors=tutors)
df2
##############################3
#Derive column from existing column
df =pd.DataFrame(technologies)
df2 = df.assign(Discount_Percent=lambda x:x.Fee*x.Discount/100)
print(df2)
##############################
#Append Column to  Existing Pandas Dataframe
#Add new column to the existing dataframe
df = pd.DataFrame(technologies)
df["MNCCompanies"] =MNCCompanies
print(df)
############################
#add new  column at the specific position
df = pd.DataFrame(technologies)
df.insert(0, 'Tutors', tutors)
print(df)
########################
#Pandas rename column with example
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySparks","Hadoop","Python",None,"C++"],
    'Fee':[2000,3000,5000,4000,np.nan,1000],
    'Duration':['30days','20days','45days','60days','55days','35days'],
    'Discount':[100,200,300,400,500,50]
        })
df = pd.DataFrame(technologies)
print(df)
df.columns
print(df.columns)
#pandas rename column name
#rename a single column
df2 = df.rename(columns={'Courses':'Courses_list'})
print(df2.columns)
#

#renam multiple column
# when we want to rename multiple column we need to use dictionary
df.rename(columns={'Courses':'Courses_list','Fee':'Course_fee','Duration':'courses_duration'},inplace=True)
print(df.columns)
df.columns
###############################

