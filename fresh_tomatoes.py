import webbrowser
import os
import re
# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
    <html>
    <head>
    <title>Movie Trailers</title>
    <meta name = "viewport" content = "width=device-width,
    initial-scale = 1.0">

    <script src = "https://code.jquery.com/jquery-1.12.3.min.js"
        integrity = "sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin = "anonymous"></script>
        <link href = "https://fonts.googleapis.com/css?family=Courgette"
        rel = "stylesheet">
        <link rel = "stylesheet" href =
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link
href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
    rel = "stylesheet" type = "text/css" />

    <script src =
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeY").attr("src", "#");
            })
        })

        function changeVideo(id) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + id;
            $("#myVideo").modal("show");
         $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        }
    </script>
    <style>
        .container {
            flex-wrap: wrap;
            display: flex;
            flex: 10%;
            justify-content: center;
            background-color:paleturquoise;
        }

        body {
            margin: 0;
        }

        header {
            background-color: white;
            text-align: center;
            font-size: 40px;
        }
        img {
            height: 400px;
            width: 250px;
        }
        .m:hover,
        .m1:hover,
        .m2:hover,
        .m3:hover,
        .m4:hover,
        .m5:hover {
            background-color:white;
            visibility: visible;
            cursor: pointer;
        }

        .m,.m1,.m2,.m3,.m4,.m5 {

            padding-top: 15px;
            padding-left: 40px;
            padding-bottom: 30px;
            padding-right: 40px;
            background-color:paleturquoise;
        }

    </style>
    </head>'''
main_page_content = '''
<body>
    <header> Movie Trailers  </header>
    <main>
        <div class = "container">
            <div class = "m" onclick = "changeVideo('SbXIj2T-_uk')">
                <img src = "https://bit.ly/2s3BTo2">
                <figcaption style = "text-align: center;">
                    <b>Cars</b>
                </figcaption>
            </div>
            <div class = "m1" onclick = "changeVideo('n2igjYFojUo')">
                <img src = "https://bit.ly/2LlLlMn">
                <figcaption style = "text-align: center;">
                    <b>Fantastic Mr fox</b>
                </figcaption>
            </div>
            <div class = "m2" onclick = "changeVideo('SWspqy0hhqk')">
                <img src = "https://bit.ly/2IX5Q3L">
                <figcaption style = "text-align: center;">
                    <B>Alice in wonderland</B>
                </figcaption>
            </div>

            <div class="m3" onclick="changeVideo('GE5aHKJp6HI')">
                <img src = "https://bit.ly/2IDyYha">
                <figcaption style = "text-align: center;">
                    <B>SPY kids</B>
                </figcaption>
            </div>
            <div class = "m4" onclick = "changeVideo('81ll2B4zl1g')">
                <img src = "https://bit.ly/2rY67tp">
                <figcaption style = "text-align: center;">
                    <b>Rio 2</b>
                </figcaption>
            </div>
            <div class = "m5" onclick = "changeVideo('yhBpgqXwrt8')">
                <img src = "https://bit.ly/2kig68B">
                <figcaption style="text-align: center">
                    <b>The Smurfs</b>
                </figcaption>
            </div>
        </div>
        <div class = "modal fade" id = "myVideo" tabindex = "-1"
        role = "dialog" aria-labelledby = "myModalLabel">
            <div class = "modal-dialog" role = "document">
                <div class = "modal-content">
                    <div class = "modal-body">

                        <iframe id = "myframeY" width = "100%" height = "250px"
                        src = "" frameborder = "0" allowfullscreen></iframe>

                    </div>
                    <div class = "modal-footer">
                        <button type = "button" class = "btn btn-default"
                        data-dismiss = "modal">Close</button>
                    </div>
                </div>
            </div>
        </div>


    </main>
</html>
'''
# A single movie entry html template
movie_title_content = '''
<div class = "col-md-6 col-lg-4 movie-title text-center"
data-trailer-youtube-id = "{trailer_youtube_id}"
data-toggle = "modal" data-target="#trailer">
    <img src = "{poster_image_url}" width = "220" height = "342">
    <h2 style = "color:white;">{movie_title}</h2>
</div>
'''


def create_movie_titles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
                           r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
                           r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # Append the tile for the movie with its content filled in
        content += movie_title_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    '''Replace the placeholder for the movie tiles with
    the actual dynamically generated content'''
    rendered_content = main_page_content.format(
        movie_titles=create_movie_titles_content(movies))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    # open the output file in the browser
    url = os.path.abspath(output_file.name)

    webbrowser.open('file://' + url, new=2)
