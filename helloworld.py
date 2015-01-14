import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World! Revised locally. Will attempt to sync with github.com’)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
