# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:42:07 2020

@author: lakna
"""
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