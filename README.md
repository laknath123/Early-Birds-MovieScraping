# Early-Birds-MovieScraping
 There is no time like a pandemic to watch every single movie in the IMDB database. Our program allows users to filter through a database of movies, using key identifiers like title, genre, and ratings. The program also offers a recommendation feature based on the user’s favorite movie. This program generates pandas dataframes from csv files containing over 100,000 user ratings on over 1,700 movies. Using sqlite3 the program also builds a database to store this information in 3 separate tables. Users can query this database based on their preferences or can simply provide their favorite movie in order to get recommendations. Here the program uses scipy sparse matrices and sci kit learn nearest neighbor modules to build a k- nearest neighbor classifier that identifies and returns a specified number of recommendations. Users can also access additional information about many films. The program uses the Open Movie Database API to obtain plot summaries and movie posters. The program also accesses box office statistics and information about a movie’s cast using web scraping from IMDB. 

User Instructions
Step 1 - Download zip file from our github repository.
Step 2 - Open final.py
Step 3- If the packages are not available in your python environment, install them.
Step 4 - Run final.py
After completing step 3, The Menu should pop up, and the user should be able to access the following 9 options:

1 - Get movie information based on title
The user must enter a movie title spelled correctly with a capital first letter, and they can retrieve the movie information. 

2 - Get movie plot summary
The user must enter a movie title spelled correctly with a capital first letter, and they can retrieve the movie’s plot summary.

3 - Get movie box office statistics
The user must enter a movie title spelled correctly with a capital first letter, and they can retrieve the movie’s box office statistics.
     
4 - Get movie recommendations
The user must enter a movie title spelled correctly with a capital first letter and the number of recommendations they would like and they can be given recommendation.
5 - Get movies by rating
The user must enter a movie genre with a capital first letter, how many movies they would like to be listed and a movie rating between 1 and 5. 


6 - Get movies by genre
The user must input a genre spelled correctly with a capital first letter and  how many movies they would like to be listed.


7 - Get all cast members
The user must enter a movie title spelled correctly with a capital first letter, and they can retrieve the movie cast.


8 - Get movie poster
The user must enter a movie title spelled correctly with a capital first letter, and they can retrieve the movie poster in JPEG format from the folder.


0 - Quit
If the user wants to exit the program, they can press number 0.
Once the user quits they can no longer access the program.
