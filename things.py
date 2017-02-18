# -*- coding: utf-8 -*-
# things.py

# Let's get this party started!
import falcon
from to_js import get_question

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):

    def on_get(self, req, resp,question):
        """Handles GET requests"""
        # {
        #     "results": [
        #         {
        #             "name": "Google"
        #         },
        #         {
        #             "name": "Baidu"
        #         },
        #         {
        #             "name": "SoSo"        
        #         }
        #     ]
        # }
        jsondata = '{"results":['        
        results = get_question(question);

        for result in results:
            jsondata = jsondata+'{"category":"'+result+'"},'

        jsondata = jsondata[:-1] + ']}'
        
        resp.status = falcon.HTTP_200  

        resp.body = jsondata
        

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/api/things/{question}', things)