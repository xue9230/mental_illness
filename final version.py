#load libraries
import pandas as pd
import matplotlib.pyplot as plt

# read csv file
data=pd.read_csv('survey.csv')
print(data.head())

# analyze data and find out the frequence level for different countries
# find out mental illness people and sorted by country
# define a function to do the analysis for requence
# location( where they want to analysis)
# dp(data name)
# num(how many top locations want to show on the visualization) since
#  the data is too much, if we want to narrow the data, if not just
#  insert 0
def fre_analysis(location,dp,num):
   f=dp[location].value_counts().reset_index()
   headers=[location,'frequence']
   f.columns=headers
   f=f.head(num)
   #show the data
   print(f)
   
   location1 = list(f[location])
   mental_con = list(f['frequence'])
   fig = plt.figure(figsize = (30, 10))
 
    # creating the bar plot
   plt.bar(location1, mental_con, color ='red',
        width = 0.5)
 
   plt.xlabel(location)
   plt.ylabel("No. of frequence for mental illness")
   plt.title(("Top 10 most frequence mental illness ")+(location))
   plt.show()

fre_analysis('Country',data,10)
fre_analysis('state',data,10)


# Analysis the attitude 

data.loc[data["treatment"]=="Yes","pos_attitude"]=1
data.loc[data["treatment"]=="No","pos_attitude"]=0
data.loc[data["treatment"]=="Yes","nav_attitude"]=0
data.loc[data["treatment"]=="No","nav_attitude"]=1

# define the function to do the annlysis for attitude
# location(where to analysis)
# dp (data name)
# num (the number of attitude should be high than num), since the data
# is too much, if we want to narrow the data, if not just insert 0
def att_analysis(location, dp,num):
 at=dp.groupby(location)
 at=at[('pos_attitude'),('nav_attitude')].sum().reset_index()
 at2=at[(at['pos_attitude']>num)|(at['nav_attitude']>num)]

 # print data
 print(at2) 
 #plot visualization

 plt.figure(figsize = (30, 10))

 plt.xlabel(location)
 plt.ylabel("number of illness")
 plt.title (("Attitude varies by ")+location)

 # Plot a simple line chart
 plt.plot(at2[location], at2['pos_attitude'], color='red', label='positive attitude')

 # Plot another line on the same chart/graph
 plt.plot(at2[location], at2['nav_attitude'], color='blue', label='nagetive attitude')
 plt.show()

att_analysis("Country",data,10)
att_analysis("state",data,10)

