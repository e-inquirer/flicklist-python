import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = ["x-men1", "x-men2", "x-men3", "rocky1", "rocky2", "rocky3"]

        # TODO: randomly choose one of the movies, and return it
        index = random.randint(0, 5)

        return movieList[index]

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tomorrow's Movie</h1>"
        tomorrow_movie = self.getRandomMovie()

        content += "<h1>Tomorrow's Movie</h1>"
        content += "<p>" + tomorrow_movie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
