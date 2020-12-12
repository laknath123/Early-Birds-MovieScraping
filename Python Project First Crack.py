#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd 

def read_df_create_sqldb(filename):
    db=pd.read_csv(filename) #read in csv file as pandas dataframe
    create_query="""CREATE TABLE """  + filename[:-4] + """ ("""  #generate SQL Create Query based on the attributes of the table
    for x in range(len(db.columns)):
        if x < len(db.columns)-1: 
            create_query+= db.columns[x] + " VarCHAR2(20), "
        else:    
            create_query+=db.columns[x]+ " VarCHAR2(20))"
        try: #create a database file based on filename, test connection
            connection = sqlite3.connect("movies-main3.sqlite")
            cursor=connection.cursor()
        except: 
            print("Database Connection Error")
    cursor.execute(create_query)  
    insertquery='INSERT INTO '+ filename[:-4]
    for x in range(len(db.columns)):
        if x==0:
            insertquery+=' VALUES(?,' 
        elif x<(len(db.columns)-1):
            insertquery+='?,'
        else:
            insertquery+='?)'   
    cursor.executemany(insertquery,db.values.tolist())
    connection.commit()
    return db


# In[2]:


tablenames=["links.csv", "movies.csv", "ratings2.csv","tags.csv"]
dflist=[]
for x in tablenames:
    results=read_df_create_sqldb(x)
    dflist.append(results)


# In[3]:


#Get Average Rating For Movies
query= "SELECT m.title, round(avg(rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=m.movieId WHERE r.movieid IN ('2059.0') GROUP BY m.movieId, m.title"
connection=sqlite3.connect('movies-main2.sqlite')
cursor=connection.cursor()
cursor.execute(query)
rows=cursor.fetchall()
for x in rows:
    print(x)


# In[10]:


#Get movieId from name

movie_title_df=dflist[1]
movietitle=input("Enter a movie title")
results=list(movie_title_df[movie_title_df['title'].str.match(movietitle)]['movieId'])
query2= "SELECT m.title, round(avg(rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=m.movieId WHERE m.movieid IN ("
for x in range(len(results)):
    if x < len(results)-1:
        query2+=str(results[x])+","
    else:
        query2+=str(results[x])+")"
    
query2+=" GROUP BY m.movieId, m.title"

connection=sqlite3.connect('movies-main2.sqlite')
cursor=connection.cursor()
cursor.execute(query2)
rows=cursor.fetchall()
for x in rows:
    print(x)


# In[8]:


query2="SELECT * FROM links"

connection=sqlite3.connect('movies-main2.sqlite')
cursor=connection.cursor()
cursor.execute(query2)
rows=cursor.fetchall()
for x in rows:
    print(x)


# In[ ]:


#Write function takes as an input for movie 
#getid()

