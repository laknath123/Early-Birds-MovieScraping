# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:11:05 2020

@author: Sophia
"""

import pandas as pd
import sqlite3
import pandas as pd 
import random 
import scipy.sparse
import re
from sklearn.neighbors import NearestNeighbors
from DBS import get_Avg_Movie_Rating, make_database, getListByGenre, recommend_movies, getListByRating
from omdbapi import plot_prompt, poster_prompt
from web_scrape import boxOffice, Actors


def menu():
    choice = -1
    while choice not in (0,1,2,3,4,5,6,7,8,9):
        choice = int(input('''
1. Get Movie Rating Based on Title
2. Get Movie Plot Summary 
3. Get Movie Box Office Statistics 
4. Get Movie Reccommendations
5. Get Movies By Rating 
6. Get Movies by Genre
7. Get All Cast Members
8. Get Movie Poster
0. Quit

Please select a choice from the number options above: ''').strip())
        if choice not in (0,1,2,3,4,5,6,7,8):
            print("\nOption not valid! Please select a valid option (0-6).")
    return choice

def main ():
    choice = -1
    while choice != 0:
        choice = menu()
        if choice == 1:
            get_Avg_Movie_Rating()
        elif choice == 2:
            plot_prompt()
        elif choice == 3:
            boxOffice()
        elif choice == 4:
            recommend_movies()
        elif choice == 5:
            getListByRating()
        elif choice == 6:
            getListByGenre()
        elif choice == 7:
            for key, value in Actors().items():
                print(f'Actor Name: {key} -- Character Name: {value}')
        elif choice == 8:
            poster_prompt()
    return ''

if __name__=='__main__':
 #store results in df
     make_database()   
     main()
