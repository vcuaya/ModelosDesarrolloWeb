#!/usr/bin/python3

import cgi
import requests
from http import cookies

# Cookies
C = cookies.SimpleCookie()
C["fig"] = "newton"
C["sugar"] = "wafer"

session=requests.Session()
print(session.cookies.get_dict())
print(C)  # generate HTTP headers

# print(C.output())  # same thing

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')


def plantilla(title):
    print("""
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>""" + title + """</title>
  <link href="./<p00>/css/style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <p>Hello world</p>
  <script src="./<p00>/js/script.js"></script>
</body>

</html>
""")


""" C = cookies.SimpleCookie()
C.load("chips=ahoy; vienna=finger")  # load from a string (HTTP header)
print(C)

C = cookies.SimpleCookie()
C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=\\012;";')
print(C)

C = cookies.SimpleCookie()
C["oreo"] = "doublestuff"
C["oreo"]["path"] = "/"
print(C)

C = cookies.SimpleCookie()
C["twix"] = "none for you"
C["twix"].value
C = cookies.SimpleCookie()
C["number"] = 7  # equivalent to C["number"] = str(7)
C["string"] = "seven"
C["number"].value
C["string"].value
print(C)
 """