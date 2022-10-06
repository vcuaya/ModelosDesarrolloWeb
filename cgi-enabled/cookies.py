#!/usr/bin/python3

from http import cookies
import cgi

# Create Cookie
C = cookies.SimpleCookie()
# Set Cookie
C["board"] = "00000000000000000000"
# Generate HTTP headers
print(C)

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

# Variable to get values from send it form
form = cgi.FieldStorage()
page = form.getvalue("page")

cookie = C["board"].value

print(cookie)
print()

C["board"] = "00000000000000011010"

print(C["board"].value)
