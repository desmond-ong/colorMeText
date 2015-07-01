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
#from annotator import SentimentAnnotator
#from colorPicker import colorPicker

# def colorPicker(scores):
# 	colors = []
# 	for score in scores:
# 		if score == 0 or score == 5:
# 			colors.append("gray")
# 		elif score < 5 and score > 4:
# 			colors.append("#FF5050")
# 		elif score <= 4 and score > 3:
# 			colors.append("red")
# 		elif score <= 3 and score > 2:
# 			colors.append("mediumred")
# 		elif score <= 2 and score >= 1:
# 			colors.append("darkred")
# 		elif score < 5 and score > 6:
# 			colors.append("#3366FF")
# 		elif score <= 6 and score > 7:
# 			colors.append("blue")
# 		elif score <= 7 and score > 8:
# 			colors.append("mediumblue")
# 		elif score <= 8 and score >= 9:
# 			colors.append("darkblue")
# 	return colors

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
#result['message'] = myAnnotator.annotate(d['param'], "anything"))
result['message'] = d['param'].upper() 
#join(",").(colorPicker([4, 6]))
#d['param'].upper() 


result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

