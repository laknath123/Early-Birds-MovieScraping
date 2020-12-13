#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sqlite3
import pandas as pd 
import random 

def read_df_create_sqldb(filename):
    db=pd.read_csv(filename) #read in csv file as pandas dataframe
    create_query="""CREATE TABLE """  + filename[:-4] + """ ("""  #generate SQL Create Query based on the attributes of the table
    for x in range(len(db.columns)): #write create query using for loop to get all columns
        if x < len(db.columns)-1: 
            create_query+= db.columns[x] + " VarCHAR2(20), "
        else:    
            create_query+=db.columns[x]+ " VarCHAR2(20))"
        try: #create a database file based on filename, test connection
            connection = sqlite3.connect("movies-main2.sqlite") #connect to cursor create main movie database object
            cursor=connection.cursor()
        except: 
            print("Database Connection Error")
    cursor.execute(create_query) #connect to cursor execute create query  
    insertquery='INSERT INTO '+ filename[:-4] #Write insert query using for loop to get all columns
    for x in range(len(db.columns)):
        if x==0:
            insertquery+=' VALUES(?,' 
        elif x<(len(db.columns)-1):
            insertquery+='?,'
        else:
            insertquery+='?)'   
    cursor.executemany(insertquery,db.values.tolist()) #Run insert query along with values from the df converted to a list
    connection.commit()
    return db


# In[10]:


tablenames=["links.csv", "movies.csv", "ratings2.csv","tags.csv"] #list of tables needed to make database
dflist=[] #list of dataframes to store resulting dfs
for x in tablenames:
    results=read_df_create_sqldb(x) #execute function for each filename
    dflist.append(results) #store results in df


# In[11]:


#Get Average Rating For Movies
query= "SELECT m.title, round(avg(rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=m.movieId WHERE r.movieid IN ('2059.0') GROUP BY m.movieId, m.title"
connection=sqlite3.connect('movies-main3.sqlite')
cursor=connection.cursor()
cursor.execute(query)
rows=cursor.fetchall()
for x in rows:
    print(x)


# In[12]:


#Get movieId from name
def get_Avg_Movie_Rating():
    movie_title_df=dflist[1] #grab movies df from list of dfs
    movietitle=input("Enter a movie title: ") #ask user for movie to search for
    results=list(movie_title_df[movie_title_df['title'].str.match(movietitle)]['movieId']) #find movie ids of all movies that match the RE expression given by user
    query2= "SELECT m.title, round(avg(rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN (" #write sql query to fetch movie and average rating from database 
    for x in range(len(results)): #use for loop to add to SQL query WHERE clause to only get movies found in our earlier search
        if x < len(results)-1:
            query2+=str(results[x])+","
        else:
            query2+=str(results[x])+")"
    
    query2+=" GROUP BY m.movieId, m.title"

    connection=sqlite3.connect('movies-main2.sqlite') #connect to database
    cursor=connection.cursor() 
    cursor.execute(query2) #execute the above query
    rows=cursor.fetchall() #fetch rows 
    for x in rows: #for each result print it in a formatted fashion
        print('Title: '+ x[0][:-6])
        print('Year: ' + x[0][-5:-1])
        print('Average User Rating: '+ str(x[1]) + "/5 Stars")
        
get_Avg_Movie_Rating()


# In[13]:


def getListByGenre():
    moviegen=input("Enter Genre(s) to search for: ") #ask user for genre(s) to search for 
    number=int(input("How many movies would you like?")) #ask user for number of results to return 
    if len(moviegen.split())>1: #create RE to search for one or more genres
        movie_re="["
        for x in range(len(moviegen.split())):
            movie_re+=moviegen.split()[x]
            if x < len(moviegen.split())-1:
                movie_re+="/"
        movie_re+="]"
    else:
        movie_re=moviegen
    movie_genre_df=dflist[1] #grab movies df from list
    result=list(movie_genre_df[movie_genre_df['genres'].str.match(movie_re)]['movieId']) #find movie ids of all movies that match the RE expression given by user
    rand_selections=[]
    for x in range(number): # generate the number of specified random numbers to randomly pick x number of movies of that genre
        rand_selections.append(result[random.randrange(0,len(result))])

    query2= "SELECT m.title, m.genres, round(avg(r.rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN (" #write SQL query to get the movie title, genre and average rating from our database
    for x in range(len(rand_selections)): #for loop to append the ids of rand selected movies
        if x < len(rand_selections)-1:
            query2+=str(rand_selections[x])+","
        else:
            query2+=str(rand_selections[x])+")"
    query2+=" GROUP BY m.movieId, m.title"

    connection=sqlite3.connect('movies-main2.sqlite') #connect to database
    cursor=connection.cursor() 
    cursor.execute(query2) #run the created query 
    rows=cursor.fetchall() #fetch rows
    for x in rows: #print formatted results
        print('Title: '+ x[0][:-6])
        print('Year: ' + x[0][-5:-1])
        print('Average User Rating: '+ str(x[2]) + "/5 Stars")
        print('Genre Tags: '+ x[1])

getListByGenre()


# In[14]:


#Write function takes as an input for movie 
#getid() tt0 + imdb
def getid():
    movie_title=input("Enter a movie title:") #Prompt user for a movie title
    movie_id_df=dflist[1]  #grab movie database objects
    result=list(movie_id_df[movie_id_df['title'].str.match(movie_title)]['movieId']) #match user input to the title section of movie dataframe return resulting movieid(s)
    query2= "SELECT l.imdbId FROM links l JOIN movies m ON CAST(l.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN (" #write SQL query to return imdbid
    for x in range(len(result)): #add id or ids to the WHERE clause of SQL query
        if x < len(result)-1:
            query2+=str(result[x])+","
        else:
            query2+=str(result[x])+")"   
    connection=sqlite3.connect('movies-main2.sqlite') #connect to database
    cursor=connection.cursor()
    cursor.execute(query2) #run query 
    rows=cursor.fetchall() #fetch results 
    imdbids=[]
    for x in rows: #for each result format it correctly by adding Imdb syntax and leading zeros
        if len(x[0])==7:
            imdbids.append('tt00'+str((x[0][:-2])))
        else:
            imdbids.append('tt0'+str((x[0][:-2])))
    return imdbids #return list of correctly formatted IMDB ids. 

y=getid()

for x in y:
    print("https://www.imdb.com/title/"+x)


# In[40]:


def getListByRating():
    moviegen=input("Enter Genre(s) to search for: ") #ask user for genre(s) to search for 
    number=int(input("How many movies would you like?")) #ask user for rating threshold 
    ratings=input("Enter Minimum Rating to Include Between (1-5)")
    if len(moviegen.split())>1: #create RE to search for one or more genres
        movie_re="["
        for x in range(len(moviegen.split())):
            movie_re+=moviegen.split()[x]
            if x < len(moviegen.split())-1:
                movie_re+="/"
        movie_re+="]"
    else:
        movie_re=moviegen
    movie_genre_df=dflist[1] #grab movies df from list
    result=list(movie_genre_df[movie_genre_df['genres'].str.match(movie_re)]['movieId']) #find movie ids of all movies that match the RE expression given by user
    query2= "SELECT m.title, m.genres, round(avg(r.rating),2) FROM ratings2 r JOIN movies m ON CAST(r.movieId as INT)=CAST(m.movieId as INT) WHERE m.movieid IN (" #write SQL query to get the movie title, genre and average rating from our database
    for x in range(len(result)): #for loop to append the ids of rand selected movies
        if x < len(result)-1:
            query2+=str(result[x])+","
        else:
            query2+=str(result[x])+")"
    query2+=" GROUP BY m.movieId, m.title HAVING avg(r.rating) >" + ratings
    connection=sqlite3.connect('movies-main2.sqlite') #connect to database
    cursor=connection.cursor() 
    cursor.execute(query2) #run the created query 
    rows=cursor.fetchall() #fetch rows
    rand_selections=[]
    for x in range(int(number)): # generate the number of specified random numbers to randomly pick x number of movies of that genre
        rand_selections.append(random.randrange(0,len(rows)))
    print(rand_selections)
    for x in rand_selections: #print formatted results
        print('Title: '+ rows[x][0][:-6])
        print('Year: ' + rows[x][0][-5:-1])
        print('Average User Rating: '+ str(rows[x][2]) + "/5 Stars")
        print('Genre Tags: '+ rows[x][1])

getListByRating()


# In[ ]:




