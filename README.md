# MOVIE-TRAILER 
This project explains the use of a Movie object class in Python to connect to a webpage, in which it makes us to see the list of 
favourite movies and by clicking on the poster of selected movie it will connect to the movie trailer of that movie on youtube. This
project includes CSS and jQuery to display the webpage.

# How to design:
First we create a html file and we apply CSS to it for looking good. 
Put that HTML code inside python file named freshtomatoes.py file.

# For running the project on server side:
Here we are using three python files for running the program on serverside.
They are media.py, center.py, freshtomatoes.py

# MEDIA.PY
The movie class in the movie.py creates a data structure to store your favorite movies, including movie title,image url and youtube link to the movie trailer.

# CENTER.PY
This is the main file which creates instances to connect to the trailers of the movie on the server side.In this file it connects to the
media.py and freshtomatoes.py files to open the web page and after running this file in server side an html file is created.

# FRESHTOMATOES.PY
This file has a function called open_movies_Page, which has list of movie trailer links and it contains the html code in it to connect to
the webpage.

