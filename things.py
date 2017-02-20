# -*- coding: utf-8 -*-
# things.py

# Let's get this party started!
import falcon
from evalnn import evaluation

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):

    def __init__(self):      
        self.eva = evaluation()

    def on_get(self, req, resp,question):
        code = 0
        jsondata = '{"desc":[' 
        (desc,category) = self.eva.prediction(question);

        for result in desc:
            if len(result)!=0:
                jsondata = jsondata+'{"name":"'+result+'"},'
            if result == "需要更多描述":
                code = 1

        jsondata = jsondata[:-1] + '],"category":['

        for result in category:
            if result == "需要更多描述":
                code = 1
            if len(result)!=0:
                jsondata = jsondata+'{"name":"'+result+'"},'


        if len(category) == 0:
            jsondata = jsondata + '],"code":"'
        else:
            jsondata = jsondata[:-1] + '],"code":"'

        jsondata = jsondata + str(code) + '"}'
        
        resp.status = falcon.HTTP_200  

        resp.body = jsondata
        

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/api/things/{question}', things)