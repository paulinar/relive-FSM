from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import logging
import requests
import json
import urllib
import urlparse

HACKFSM_ID = "1057a9b5"
HACKFSM_KEY = "8f05bb54b7b191e07748eac9aba8ffef"
HACKFSM_BASEURL = "https://apis.berkeley.edu/solr/fsm/select"

def index(request):
	template = get_template("templates/timeline.html")
	return HttpResponse(template.render(Context({'foo':'bar'})))

def query(q, fl="id"):
    url = "{base_url}?".format(base_url=HACKFSM_BASEURL) + \
            urllib.urlencode({'q':q,
                              'fl':fl,
                              'wt':'json',
                              'app_id':HACKFSM_ID,
                              'app_key':HACKFSM_KEY})
    r = requests.get(url)
    return r.json()

def search(request, search_query=""):
	if query == "":
		print "Empty Query"
		return

	# result = query(q="fsmTitle:Savio")['response']
	result = query(q=search_query)['response']
	return HttpResponse(json.dumps(result), content_type="application/json")