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
# Change the path to the directory you want posters to be saved to
#os.chdir('C:\\Users\\lakna\\OneDrive\\Desktop\\Early-Birds-MovieScraping')


#User input function
# The user input function has to return




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
