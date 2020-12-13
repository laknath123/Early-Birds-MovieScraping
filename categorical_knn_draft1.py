# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:27:10 2020

@author: Sophia
"""


import pandas as pd
import numpy as np

#importing the data
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv("filepath", names=r_cols, usecols=range(3))
ratings.head()


#group by MOVIE ID *CAN CHANGE THIS*
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
movieProperties.head()

# normalized number of ratings
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
movieNormalizedNumRatings.head()


#get genre
movieDict = {}
with open(r'FILEPATH') as f:
    temp = ''
    for line in f:
        line.decode(encoding = 'utf-8')
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), 
                              movieNormalizedNumRatings.loc[movieID].get('size'), 
                              movieProperties.loc[movieID].rating.get('mean'))
        
        
# finding distance between two movies
from scipy import spatial

def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance
    
ComputeDistance(movieDict[2], movieDict[4])



# code to compute difference 
import operator

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))
    
avgRating /= K

# compare to the average rating of 10 nearest neighbors
avgRating






