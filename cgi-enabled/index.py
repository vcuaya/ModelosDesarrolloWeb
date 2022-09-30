#!/usr/bin/python3

import os
import cgi
import sys
import random

# Get path to my module
scriptPath = os.path.dirname(__file__)
modulePath = os.path.join(scriptPath, '..', 'p04', 'img')
sys.path.append(modulePath)
import images as img
# To get all images
# images.get()

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

# Variable to get values from send it form
#form = cgi.FieldStorage()
#page = form.getvalue("page")

# Format text in HTML document
def template(title, table):
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
  <table>
    <thead>
      <tr>
        <th colspan="5">Golden Stars Memorama</th>
      </tr>
    </thead>
    <tbody>
    """ + table + """
    </tbody>
      <tfoot>
        <tr>
          <th colspan="5">Puntaje</th>
        </tr>
      </tfoot>
    </table>
  <script src="./<p00>/js/script.js"></script>
</body>

</html>
""")


def table():
    # Get images from images module
    aux = img.get()

    # Shuffle aux array
    random.shuffle(aux)

    # Cards array for use in the boardgame
    cards = []

    # Append images into cards
    for x in range(10):
        cards.append(aux.pop())

    # Duplicate cards array
    cards.extend(cards)

    # Shuffle cards array
    random.shuffle(cards)

    # String to append
    answer = ""
    for i in range(4):
        answer += '<tr>\n'
        for j in range(5):
            answer += str(cards.pop())
        answer += '</tr>\n'

    return answer

t=table()

template("CGI", t)
