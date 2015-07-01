# !/usr/
import cgi, cgitb,requests, re

cgitb.enable()
form = cgi.FieldStorage()
print form.getvalue("data")


def returnColors(text):
    return ["blue", "green"]


