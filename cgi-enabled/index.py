#!/usr/bin/python3

import os
import cgi
import sys
import random
from http import cookies

# Get path to my module
scriptPath = os.path.dirname(__file__)
modulePath = os.path.join(scriptPath, '..', 'p04', 'img')
sys.path.append(modulePath)
import images as img

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
card = form.getvalue("card")
cookie = C["board"].value

# Format text in HTML document


def template(title, table):
    print("""
<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
	<title>""" + title + """</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  <link href="./../p04/css/style.css" rel="stylesheet" type="text/css" />
</head>

<body class="bg-dark">
	<div class="table-responsive">
		<table class="table table-dark">
			<thead>
				<tr>
					<th class="text-center thead-font-border" colspan="5">""" + title + """</th>
				</tr>
			</thead>
			<tbody>
    """ + table + """
			</tbody>
			<tfoot>
				<tr>
					<th class="text-center tfoot-font-border" colspan="2">Puntaje</th>
				</tr>
			</tfoot>
		</table>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
		integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
		crossorigin="anonymous"></script>
</body>

</html>
""")


def getCards():
    # Get images from images module
    aux = img.get()

    # Shuffle aux array
    random.shuffle(aux)

    # Cards array for use in the boardgame
    basenames = []

    # Append images into cards
    for x in range(10):
        basenames.append(aux.pop())

    # Duplicate cards array
    basenames.extend(basenames)

    # Shuffle cards array
    random.shuffle(basenames)

    return basenames


def table(flipped, cards):
    board = cards
    for x in range(20):
        if not flipped[x]:
            board[x] = '200px-NAP-01_Back.png'
    board.reverse()
    # String to append
    string = "\n"
    for i in range(4):
        string += '\t<tr>\n'
        for j in range(5):
            string += '\t\t'+'<td><img class="img-thumbnail img-fluid" src="./../p04/img/' + \
                str(board.pop())+'"></td>\n'
        string += '\t</tr>\n'
    return string


flipped = [
    False, False, False, False, False,
    False, False, False, False, False,
    False, False, False, False, False,
    False, False, False, False, False
]

for i, element in enumerate(cookie):
    if cookie[i] == "0":
        flipped[i] = False
    elif cookie[i] == "1":
        flipped[i] = True

# Tarjetas del tablero
cards = getCards()

# Imágenes para la plantilla
images = table(flipped, cards)

# Impresión de la página
template("Golden Stars Memorama", images)
