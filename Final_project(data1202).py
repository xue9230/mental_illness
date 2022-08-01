#load libraries
import pandas as pd
import matplotlib.pyplot as plt

# read csv file
data=pd.read_csv('survey.csv')
print(data.head())

# analyze data and find out the frequence level for different countries
# find out mental illness people and sorted by country
# for countries there are too many, only show top 10 countries
f_state=data['state'].value_counts().reset_index()
headers=['state','frequence']
f_state.columns=headers
f=f.head(10)
print(f_state.head(10))

# visualization for showing the top 10 frequence mental illness countries
#for different country
country = list(f['Country'])
mental_con = list(f['frequence'])
fig = plt.figure(figsize = (30, 10))
 
# creating the bar plot
plt.bar(country, mental_con, color ='red',
        width = 0.5)
 
plt.xlabel("Country")
plt.ylabel("No. of frequence for mental illness")
plt.title("Top 10 most frequence mental illness countries")
plt.show()

# for different state within US
state = list(f_state['state'])
mental_con_state = list(f_state['frequence'])
fig = plt.figure(figsize = (30, 10))
 
# creating the bar plot
plt.bar(state, mental_con_state, color ='blue',
        width = 0.5)
 
plt.xlabel("State")
plt.ylabel("No. of frequence for mental illness")
plt.title("Top 10 most frequence mental illness countries")
plt.show()

# Analysis the attitude 
# first by countries

data.loc[data["treatment"]=="Yes","pos_attitude"]=1
data.loc[data["treatment"]=="No","pos_attitude"]=0
data.loc[data["treatment"]=="Yes","nav_attitude"]=0
data.loc[data["treatment"]=="No","nav_attitude"]=1

at=data.groupby('Country')
at=at[('pos_attitude'),('nav_attitude')].sum().reset_index()

#only want to show more attitude country which is more than 10
at2=at[(at['pos_attitude']>10)|(at['nav_attitude']>10)]
print(at2)

#plot visualization


plt.figure(figsize = (30, 10))

plt.xlabel("Country")
plt.ylabel("number of illness")
plt.title("Attitude varies by countries")

# Plot a simple line chart
plt.plot(at2['Country'], at2['pos_attitude'], color='red', label='positive attitude')

# Plot another line on the same chart/graph
plt.plot(at2['Country'], at2['nav_attitude'], color='blue', label='nagetive attitude')
plt.show()

#Analysis by states
at_state=data.groupby('state')
at_state=at_state[('pos_attitude'),('nav_attitude')].sum().reset_index()
at_state

#plot visualization for states

plt.figure(figsize = (30, 10))

plt.xlabel("state")
plt.ylabel("number of illness")
plt.title("Attitude varies by state")

# Plot a simple line chart
plt.plot(at_state['state'],at_state['pos_attitude'], color='purple', label='positive attitude')

# Plot another line on the same chart/graph
plt.plot(at_state['state'], at_state['nav_attitude'], color='yellow', label='nagetive attitude')
plt.show()