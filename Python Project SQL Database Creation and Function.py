#!/usr/bin/env python
# coding: utf-8

# In[95]:


import sqlite3
import pandas as pd 
import random 

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


# In[34]:


#Get Average Rating For Movies
query= "SELECT m.title, round(avg(rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=m.movieId WHERE r.movieid IN ('2059.0') GROUP BY m.movieId, m.title"
connection=sqlite3.connect('movies-main3.sqlite')
cursor=connection.cursor()
cursor.execute(query)
rows=cursor.fetchall()
for x in rows:
    print(x)


# In[158]:


#Get movieId from name
def get_Avg_Movie_Rating():
    movie_title_df=dflist[1]
    movietitle=input("Enter a movie title: ")
    results=list(movie_title_df[movie_title_df['title'].str.match(movietitle)]['movieId'])
    query2= "SELECT m.title, round(avg(rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN ("
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
        print('Title: '+ x[0][:-6])
        print('Year: ' + x[0][-5:-1])
        print('Average User Rating: '+ str(x[1]) + "/5 Stars")
        
get_Avg_Movie_Rating()


# In[157]:


def getListByGenre():
    moviegen=input("Enter Genre(s) to search for: ")
    number=int(input("How many movies would you like?"))
    if len(moviegen.split())>1:
        movie_re="["
        for x in range(len(moviegen.split())):
            movie_re+=moviegen.split()[x]
            if x < len(moviegen.split())-1:
                movie_re+="/"
        movie_re+="]"
    else:
        movie_re=moviegen
    movie_genre_df=dflist[1]
    result=list(movie_genre_df[movie_genre_df['genres'].str.match(movie_re)]['movieId'])
    rand_selections=[]
    for x in range(number):
        rand_selections.append(result[random.randrange(0,len(result))])

    query2= "SELECT m.title, m.genres, round(avg(r.rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN ("
    for x in range(len(rand_selections)):
        if x < len(rand_selections)-1:
            query2+=str(rand_selections[x])+","
        else:
            query2+=str(rand_selections[x])+")"
    query2+=" GROUP BY m.movieId, m.title"

    connection=sqlite3.connect('movies-main2.sqlite')
    cursor=connection.cursor()
    cursor.execute(query2)
    rows=cursor.fetchall()
    for x in rows:
        print('Title: '+ x[0][:-6])
        print('Year: ' + x[0][-5:-1])
        print('Average User Rating: '+ str(x[2]) + "/5 Stars")
        print('Genre Tags: '+ x[1])

getListByGenre()


# In[155]:


#Write function takes as an input for movie 
#getid() tt0 + imdb
def getid():
    movie_title=input("Enter a movie title:")
    movie_id_df=dflist[1]
    links=dflist[0]
    result=list(movie_id_df[movie_id_df['title'].str.match(movie_title)]['movieId'])
    query2= "SELECT l.imdbId FROM links l JOIN movies m ON CAST(l.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN ("
    for x in range(len(result)):
        if x < len(result)-1:
            query2+=str(result[x])+","
        else:
            query2+=str(result[x])+")"   
    connection=sqlite3.connect('movies-main2.sqlite')
    cursor=connection.cursor()
    cursor.execute(query2)
    rows=cursor.fetchall()
    imdbids=[]
    for x in rows:
        if len(x[0])==7:
            imdbids.append('tt00'+str((x[0][:-2])))
        else:
            imdbids.append('tt0'+str((x[0][:-2])))
    return imdbids

y=getid()

for x in y:
    print("https://www.imdb.com/title/"+x)


# In[129]:


dflist[0]


# In[ ]:




