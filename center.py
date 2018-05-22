import media
import fresh_tomatoes

# Create instances of the Movie class to hold information of favourite movies
car = media.Movie("Cars", "racing", "https://bit.ly/2s3BTo2",
                  "https://www.youtube.com/embed/SbXIj2T-_uk")
fmf = media.Movie("Fantastic Mr Fox", "intelligence", "https://bit.ly/2LlLlMn",
                  "https://www.youtube.com/embed/n2igjYFojUo")
aiw = media.Movie("Alice in Wonderland", "queen friendship",
                  "https://bit.ly/2IX5Q3L",
                  "https://www.youtube.com/embed/SWspqy0hhqk")
sk = media.Movie("SPY kids", "flying kids", "https://bit.ly/2IDyYha",
                 "https://www.youtube.com/embed/GE5aHKJp6HI")
r2 = media.Movie("Rio 2", "bird talking", "https://bit.ly/2rY67tp",
                 "https://www.youtube.com/embed/81ll2B4zl1g")
ts = media.Movie("The Smurfs", " magical lillyputs", "https://bit.ly/2kig68B",
                 "https://www.youtube.com/embed/yhBpgqXwrt8")

# Add the instances to a list
movies = [car, fmf, aiw, sk, r2, ts]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
