#!/usr/bin/env python

import requests
import json
import datetime

x=1
z=1
URL = 'https://edit.meridianapps.com/api/locations/locationId/beacons'
filename = str('meredian'+ datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S')+".csv")
f = open(filename, 'w')

while URL:
	response = requests.get(URL)
	assert response.status_code == 200
	for repo in response.json()['results']:
		if z==1:
			for header in repo:
				s = str(header+",")
				f.write (s)
			f.write ("\n")
			z=0
		for inrepo in repo:
			s=str(str(repo[inrepo])+",")
			f.write (s)
		f.write ("\n")
	URL=response.json()['next']
	print ("saving page (",x,")")
	x=x+1
