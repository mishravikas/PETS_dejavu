from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Link, Resource, Person
import datetime
from collections import OrderedDict
import base64
import hashlib

# Create your views here.
def serveScript(request):
	links = Link.objects.all()
	retVal = {}
	for l in links:
		if l.inUse:
			retVal[l.website] = l.url
	print(retVal)


	return render(request, 'app/sniffScript.js', {'links':retVal}, content_type="application/x-javascript")

def serveCf(request):
	res = Resource.objects.all()
	retVal = {}
	for l in res:
		if l.inUse:
			retVal[l.website] = l.url
	print(retVal)


	return render(request, 'app/cf.js', {'res':retVal}, content_type="application/x-javascript")


def index(request):
	is_firefox = False
	print(request.META['HTTP_USER_AGENT'])
	if 'Firefox' in request.META['HTTP_USER_AGENT'] or 'firefox' in request.META['HTTP_USER_AGENT']:
		is_firefox = True
	return render(request,'app/index.html',{'is_firefox':is_firefox})

def getDates(request):
	retVal = {}
	headers_list = json.loads(request.GET["headers"])

	links = Link.objects.all()


	secrets = {}
	ranks = {}
	vw = {}
	for l in links:
		if l.inUse:
			secrets[l.website] = l.secret
			ranks[l.website] = l.rank
			vw[l.website] = l.vw
	
	# print('---------')
	# print(secrets)


	for key,val in headers_list.items():
		retVal[key] = {}
		if key in secrets:
			split_headers = headers_list[key].split('\n')
			split_headers = [i.strip() for i in split_headers]
			if secrets[key] == 'expires':

				expires = [h for h in split_headers if 'expires' in h ][0].split('expires:')[1].strip()
				max_age = [h for h in split_headers if 'max-age' in h ][0].split('=')[1]
				# print(expires)
				# print(max_age)

				val_date = datetime.datetime.strptime(expires, '%a, %d %b %Y %H:%M:%S GMT') - datetime.timedelta(seconds=int(max_age))
				retVal[key]['date'] =val_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
				retVal[key]['rank'] = ranks[key]

				if vw[key] == 'max_age':
					retVal[key]['vw'] = normalize_seconds(int(max_age))





	# ordered_keys = sorted(retVal, key=lambda k: int(retVal[k]['rank']))
	# ret = {}
	# for k in ordered_keys:
	# 	ret[k] = retVal[k]


	ret = OrderedDict(sorted(retVal.items(), key=lambda x: int(x[1]['rank'])))

	return HttpResponse(json.dumps(ret), content_type="application/json")


def getID(request):
	print('-------------------------')
	# print(request)
	headers_list = json.loads(request.GET["headers"])
	print(headers_list)

	for key,val in headers_list.items():

		split_headers = headers_list[key].split('\n')
		split_headers = [i.strip() for i in split_headers]
	

		expires = [h for h in split_headers if 'expires' in h ][0].split('expires:')[1].strip()
		max_age = [h for h in split_headers if 'max-age' in h ][0].split('=')[1]

		to_encode = expires + max_age
		print('to_encode: %s' %to_encode)			

	
	hash = hashlib.sha1(to_encode.encode("UTF-8")).hexdigest()
	# print(hash)

	p,created = Person.objects.get_or_create(hash=hash)
	print('ID: %s' %p.id)
	print('------------------------')



	return HttpResponse(json.dumps(p.id), content_type="application/json")



def normalize_seconds(seconds: int) -> tuple:
    (days, remainder) = divmod(seconds, 86400)
    (hours, remainder) = divmod(remainder, 3600)
    (minutes, seconds) = divmod(remainder, 60)
    # print(days, hours, minutes, seconds)
    out = ''
    if days:
    	out += str(days) + ' days, '
    if hours:
    	out += str(hours) + ' hours, '
    if minutes:
    	out += str(minutes) + ' minutes, '
    if seconds:
    	out += str(seconds) + ' seconds'

    return out.rstrip().rstrip(',')

def track(request):
	is_firefox = False
	print(request.META['HTTP_USER_AGENT'])
	if 'Firefox' in request.META['HTTP_USER_AGENT'] or 'firefox' in request.META['HTTP_USER_AGENT']:
		is_firefox = True
	return render(request,'app/track.html',{'is_firefox':is_firefox})

def sniff(request):
	is_firefox = False
	print(request.META['HTTP_USER_AGENT'])
	if 'Firefox' in request.META['HTTP_USER_AGENT'] or 'firefox' in request.META['HTTP_USER_AGENT']:
		is_firefox = True
	return render(request, 'app/sniff.html',{'is_firefox':is_firefox})

