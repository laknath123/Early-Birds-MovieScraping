# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:29:38 2020

@author: Cathy Chen
"""
#import the necessary library for webscraping
import requests
from bs4 import BeautifulSoup
import re

#replace the movieid with the input generated movieid
getid = 'tt0086250'

#define the function to find the USA gross and Worldwide cumulative gross for the input movie
def boxOffice(id):
    url = (f'https://www.imdb.com/title/{id}')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    movie = soup.find(id='titleDetails')
    movie_name = movie.find_all(class_='inline')
    box_office = []
    for i in movie_name:
        #use the regular expression to narrow down the search for box office
        if re.search(r'\$.*', i.find_next('div').text) != None:             
            if re.search(r'Gross.*', i.find_next('div').text) != None:           
                box_office.append(i.find_next("div").text.strip())    
    if len(box_office) == 0:
        return 'Sorry, no box office information is available'
    else:
        #eliminate the situation of redundancy
        final_office = []
        for i in box_office:
            if i not in final_office:
                final_office.append(i)
        for i in final_office:             
            print(i)
    
boxOffice(getid)


#define the function to find actor names and it's corresponding characteristics name
def Actors(id):
    url = (f'https://www.imdb.com/title/{id}')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    actor = soup.find(id = 'titleCast')
    actor_name = actor.find_all('a')
    actor_name_s = list(actor_name)
    actor_name_s1 = [str(i) for i in actor_name_s]
    actors_temp = []
    #use the regular expression to narrow down the search for the actor name and character name
    pattern1 = r'[\/name\/nm][0-9]{7}[\/\"\> ].+[\n\<\/a\>]'
    pattern2 = r'[A-Z]'
    for i in actor_name_s1:
        a = i.split('=')
        for b in a:
            if re.search(pattern1,b) != None:
                if re.search(pattern2, b) != None:
                    w = b[b.find('>')+1:b.find('<')]
                    #store the matchings to the list
                    actors_temp.append(w)
    #store the actor name and character name into the list 
    actors = []
    character = []
    for i in actors_temp:
        if '\n' in i:
            i = i.strip()
            actors.append(i)
        else:
            character.append(i) 
    #create a dictionary to store actor name and character name together
    search = dict(zip(actors,character))
    return search

#print out the actor name and its corresponding character name
for key, value in Actors(getid).items():
    print(f'Actor Name: {key} -- Character Name: {value}')

#for i in movieid:
    #print(Actors(i))
    

