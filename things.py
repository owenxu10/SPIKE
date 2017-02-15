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
        res = ''
        questionSet = get_question(question);
        for cate in questionSet:
        	res = res+cate
        resp.status = falcon.HTTP_200  # This is the default status

        resp.body = '{"message":"'+ cate +'"}'

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/api/things/{question}', things)