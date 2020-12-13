# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:25:07 2020

@author: lakna
"""
# Required Library's
import json
import requests
import urllib
import os
os.chdir('C:\\Users\\lakna\\OneDrive\\Desktop\\Early-Birds-MovieScraping')
#Change the path to the directory you want posters to be saved to


#User input function
# The user input function has to return


def plot_prompt():
    u_selection=input("Do you want to know movie plot [Y/N] :")
    if u_selection=='Y':
        ID=getid()      # If the user enters Y. I will call the getid 
        movie_plot(ID)  # function which returns an imbd ID and store it in the ID variable
    else:               # then my movie_plot function will use that ID to return the plot
        pass # else we need this to return to the menu options
            
def poster_prompt():
    u_selection=input("Do you want a image of the movie poster [Y/N] :")
    if u_selection=='Y':
        ID=getid()      # If the user enters Y. I will call the getid 
        movie_poster(ID)  # function which returns an imbd ID and store it in the ID variable
    else:               # then my movie_poster function will use that ID to return the movie poster
        pass # else we need this to return to the menu options
    

def movie_plot(ID):
    x = {'Content-Type': 'application/json'}
    url ='http://www.omdbapi.com/?i='+ID+'&apikey=9fc8c547'
    response = requests.get(url, headers = x)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        print('The Plot for',data['Title'])
        print(data['Plot'])
    else:
        "response failed"
        
def movie_poster(ID):
    x = {'Content-Type': 'application/json'}
    url ='http://www.omdbapi.com/?i='+ID+'&apikey=9fc8c547'
    response = requests.get(url, headers = x)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        image_url=data['Poster']
        title=data['Title']
        urllib.request.urlretrieve(image_url, title+'.jpg')
    else:
        "response failed"
        
        
    
movie_plot('tt0386676')  # This is just a test id to check if the Id is working
   
movie_plot('tt4955642')
