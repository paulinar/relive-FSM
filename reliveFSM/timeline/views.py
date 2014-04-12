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

# def index(request):
# 	template = get_template("templates/timeline.html")
# 	return HttpResponse(template.render(Context({'foo':'bar'})))

def query(q, fl="id"):
	url = "{base_url}?".format(base_url=HACKFSM_BASEURL) + \
			urllib.urlencode({'q':q,
							  'fl':fl,
							  'wt':'json',
							  'rows':30,
							  'app_id':HACKFSM_ID,
							  'app_key':HACKFSM_KEY})
	r = requests.get(url)
	return r.json()

# def search(request, search_query=""):
# 	if query == "":
# 		print "Empty Query"
# 		return

# 	# result = query(q="fsmTitle:Savio")['response']
# 	result = query(q=search_query)['response']
# 	return HttpResponse(json.dumps(result), content_type="application/json")

def search(request):
	print "in search"
	if 'q' in request.GET:
		result = query(q=request.GET['q'],fl="fsmTitle,fsmRelatedTitle,fsmDateCreated,fsmImageUrl")['response']
		return HttpResponse(json.dumps(result), content_type="application/json")
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

def index(request):
	return render(request, "templates/timeline.html")

# def timeline(request):
# 	print "in timeline"
# 	if 'q' in request.GET:
# 		result = query(q=request.GET['q'], fl="fsmTitle, fsmTypeOfResource, fsmDateCreated, fsmImageUrl")['response']
# 		return HttpResponse(json.dumps(result), content_type="application/json")
# 	else:
# 		message = 'You submitted an empty form.'
# 	return HttpResponse(message)