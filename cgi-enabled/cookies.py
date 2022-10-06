#!/usr/bin/python3

from http import cookies
import os
import cgi
import sys
import random

# Get path to my module
scriptPath = os.path.dirname(__file__)
modulePath = os.path.join(scriptPath, '..', 'p04', 'img')
sys.path.append(modulePath)
import images as img

# Variable to get values from send it form
form = cgi.FieldStorage()
card = form.getvalue("card")

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
    <script src="./p04/js/script.js"></script>
</body>

</html>
""")


def getCards():
    # Get images from images module
    aux = img.get()

    # Shuffle aux array
    # random.shuffle(aux)

    # Cards array for use in the boardgame
    basenames = []

    # Append images into cards
    for x in range(2):
        basenames.append(aux.pop())

    # Duplicate cards array
    basenames.extend(basenames)

    # Shuffle cards array
    # random.shuffle(basenames)

    return basenames


def table(flipped, cards):
    board = cards
    for x in range(4):
        if not flipped[x]:
            board[x] = '200px-NAP-01_Back.png'
    board.reverse()
    # String to append
    string = "\n"
    for i in range(1):
        string += '\t<tr>\n'
        for j in range(4):
            aux = board.pop()
            if aux == '200px-NAP-01_Back.png':
                string += '\t\t<td><a href="./cookies.py?card=' + str(j) + \
                    '"><img class="img-thumbnail img-fluid" src="./../p04/img/200px-NAP-01_Back.png"></a></td>\n'
            else:
                string += '\t\t<td><img class="img-thumbnail img-fluid" src="./../p04/img/' + \
                    aux + '"></td>\n'
        string += '\t</tr>\n'
    return string


def flip(card, board):
    enumerate(board)
    board[card] = True
    return board


def getCookie(cookie):
    flipped = [None, None, None, None]
    for i, element in enumerate(cookie):
        if cookie[i] == "0":
            flipped[i] = False
        elif cookie[i] == "1":
            flipped[i] = True
    return flipped


def setCookie(board):
    flipped = ""
    for i, element in enumerate(board):
        if board[i] == False:
            flipped += "0"
        elif board[i] == True:
            flipped += "1"
    return flipped


C = cookies.SimpleCookie()
exist = os.environ.get('HTTP_COOKIE')
cards = getCards()

if not exist:
    C['board'] = "0000"
    print(C)
else:
    C.load(exist)

if card is None:
    board = [False, False, False, False]
    images = table(board, cards)

else:
    cookie = C['board'].value
    board = getCookie(cookie)
    newBoard = flip(int(card), board)
    C['board'] = setCookie(newBoard)
    print(C)
    images = table(newBoard, cards)

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

template("Golden Stars Memorama", images)
