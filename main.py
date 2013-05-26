
import webapp2
import logging
import json

### This would be better suited in a separate file, but for ease of writing, let's put it here.

myHtml = """
<html>
<head>
    <script type="text/javascript" src="/static/script.js"></script>
<head>
<body onload="post()">
    <h1>This is how we send post data!!!</h1>

    <hr/>

    <div>Here's the response from the server:</div>
    <div id="response" style="color:red;"></div>
</body>
<html>
"""
class MainHandler(webapp2.RequestHandler):

    ## simply send the html template we created above to be rendered in the browser
    def get(self):
        self.response.write(myHtml)

class Poster(webapp2.RequestHandler):

    ## this will retrieve our post data from the client, then send a message back to the client
    def post(self):

        ## the body of the request holds the json object that was sent from the client
        ## documentation on the request object can be found on the webapp2 docs or on
        ## the webob docs:  http://goo.gl/WU38p

        data = self.request.body
        usableData = json.loads(data)
        logging.info(usableData['value'])

        ## send a response back to the client
        responseData = json.dumps({"serverMessage":"I'm From the Server"})
        self.response.write(responseData)

app = webapp2.WSGIApplication([('/poster', Poster),
                               ('/', MainHandler)
                              ], debug=True)
