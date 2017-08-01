
# coding: utf-8

# In[59]:
#Q1  Top ten most viewed movies with their movies Name
import pandas as pd    
import matplotlib.pyplot as plt
import numpy as np
import collections
import operator

with open('C:/Users/World/Desktop/ml-1m/ml-1m/movies.dat','r') as f:
    df_movies = pd.DataFrame(l.rstrip().split("::") for l in f)

with open('C:/Users/World/Desktop/ml-1m/ml-1m/ratings.dat','r') as f:
    df_ratings = pd.DataFrame(l.rstrip().split("::") for l in f)

df_movies.columns = ['MovieID','Title','Genres']
df_ratings.columns = ['UserID', 'MovieID', 'Rating', 'Timestamp']

df_result = pd.merge(df_movies, df_ratings, on='MovieID', how='outer')
#print df_result

a = df_result['Title']
counter=collections.Counter(a)

a = counter.most_common(10)
No_of_views=list()
for item in a:
    No_of_views.append(item[1])
No_of_views1 = np.array(No_of_views,int)

titles = list()
for item in a:
    titles.append(item[0])

Movie_title = range(10)
LABELS = titles

plt.bar(Movie_title, No_of_views1, width = 1/1.5, color="blue")
plt.xticks(Movie_title, LABELS, rotation='vertical')
plt.show()


# In[143]:
#Q2 module to plot a chart for the age wise distribution of the count of views for the movie American beauty

with open('C:/Users/World/Desktop/ml-1m/ml-1m/users.dat','r') as f:
    #next(f) # skip first row
    df_users = pd.DataFrame(l.rstrip().split("::") for l in f)
    
df_users.columns = ['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code']
        
df_result1 = pd.merge(df_ratings, df_users, on='UserID', how='outer')

df_result1.set_index('MovieID', inplace=True)

#print ab

df_result1['Age_Group'] = pd.cut(np.array(df_result1['Age'],int), 6,labels=False)
labels = np.array('under18 18-24 25-34 35-44 45-54 55-65'.split())
df_result1['Age_Group'] = labels[df_result1['Age_Group']]
ab = df_result1.loc['2858']

Ages = ab['Age_Group']
counter = collections.Counter(Ages)
print counter
d1 = dict()
d1 = counter

plt.bar(range(len(d1)), d1.values())
plt.xticks(range(len(d1)), d1.keys())
plt.show()


# In[192]:
#Q3 Display how the genres are ranked for each profession

df_rank = pd.merge(df_result, df_users, on = 'UserID',how='outer')

df_rank2 = pd.DataFrame()
df_rank2 = df_rank.filter(items=['Occupation','Genres','Rating'])
df_rank2['Occupation'].fillna('0', inplace=True)

Occupations = df_rank2['Occupation']
counter = collections.Counter(Occupations)
Occupation_lst = counter.keys()
print counter

Genres = df_rank2['Genres']
counter = collections.Counter(Genres)
Genres_lst = counter.keys()
#print Genres_lst

df_occupation_genre = pd.DataFrame()
df_occupation = pd.DataFrame()

df_rank2.set_index('Occupation', inplace=True)

for i in Occupation_lst:
    
    df_occupation = df_rank2.loc[i]
    #print df_occupation
    for item in Genres_lst:
        if (df_occupation['Genres']==item).any()==True:
            a = df_occupation.loc[[item], 'Rating':]
            Rating_lst = a['Rating']
            Rating_array = np.array(Rating_lst,int)
            Rating_sum = np.sum(Rating_array)
            a['Rating_sum'] = Rating_sum
            print a 
        else: continue  
       
       
#Q4 Top 5 genres for the occupation 'Programmers'

df_programmer = df_rank2.loc['12']
#print df_programmer
lst = df_programmer['Genres']
counter = collections.Counter(lst)
#print counter.most_common(5)

genres_12 = dict()
genres_12 = counter
#print Common_genres_12
a = counter.most_common(5)
print a
dictg12 = dict()
for x,y in a:
    dictg12[x]=y
print dictg12
plt.bar(range(len(dictg12)), dictg12.values())
plt.xticks(range(len(dictg12)), dictg12.keys(),rotation='vertical')
plt.show()
