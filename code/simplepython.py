#!/usr/bin/python

#import cgi, cgitb,requests, re

#cgitb.enable()
#form = cgi.FieldStorage()
#print form.getvalue("data")


#def returnColors(text):
#    return ["blue", "green"]

import sys, string
import json
import cgi
from annotator import SentimentAnnotator
import colorPicker

myAnnotator = SentimentAnnotator()

fs = cgi.FieldStorage()

# temp

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)
result['message'] = d['param'].upper() #myAnnotator.annotate(d['param'], "anything"))


result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

