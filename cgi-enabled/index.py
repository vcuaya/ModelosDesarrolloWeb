#!/usr/bin/python3

from http import cookies
from math import floor
import os
import cgi
from re import A
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
# Rows and columns
rows = 4
cols = 5
total = rows * cols
# Cookie
C = cookies.SimpleCookie()
exist = os.environ.get('HTTP_COOKIE')
cards = ""
attempts = 0
matched = 0
score = 0

def table(flipped, cards):
    board = cards
    for x in range(total):
        if not flipped[x]:
            board[x] = '200px-NAP-01_Back.png'
    board.reverse()
    # String to append
    string = "\n"
    for i in range(rows):
        string += '\t<tr>\n'
        for j in range(cols):
            aux = board.pop()
            if aux == '200px-NAP-01_Back.png':
                string += '\t\t<td><a href="./cookie.py?card=' + str(i*cols+j) + \
                    '"><img class="img-thumbnail img-fluid" src="./../p04/img/200px-NAP-01_Back.png"></a></td>\n'
            else:
                string += '\t\t<td><img class="img-thumbnail img-fluid" src="./../p04/img/' + \
                    aux + '"></td>\n'
        string += '\t</tr>\n'
    return string

def template(title, table, attempts, matched, score):
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
                    <th class="text-center tfoot-font-border" colspan="2">Intentos """ + str(attempts) + """</th>
                    <th class="text-center tfoot-font-border" colspan="2">Aciertos """ + str(matched) + """</th>
                    <th class="text-center tfoot-font-border" colspan="1">%""" + str(score) + """</th>
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

def initialFlipped(total):
    flipped = []
    for i in range(total):
        flipped.append(None)
    return flipped

def flip(card, board):
    enumerate(board)
    board[card] = True
    return board

def noFlip(card, board):
    enumerate(board)
    board[card] = False
    return board

def initialCookie(total):
    string = ""
    for i in range(total):
        string += "0"
    return string

def getCookie(cookie):
    flipped = initialFlipped(total)
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

def getCards():
    # Get images from images module
    aux = img.get()

    # Shuffle aux array
    # random.shuffle(aux)

    # Cards array for use in the boardgame
    basenames = []

    # Append images into cards
    for x in range(int(total/2)):
        basenames.append(aux.pop())

    # Duplicate cards array
    basenames.extend(basenames)

    # Shuffle cards array
    # random.shuffle(basenames)

    return basenames

def initialBoard(total):
    board = []
    for i in range(total):
        board.append(False)
    return board

def getScore(matched, attempts):
    if matched == 0:
        return 0
    else:
        return floor((matched / (matched + attempts))*100)

# Loading cards
cards = getCards()

if not exist:
    C['board'] = initialCookie(total)
    C['card1'] = ""
    C['card2'] = ""
    C['matched'] = "0"
    C['attempts'] = "0"
    print(C)
else:
    C.load(exist)

if card is None:
    board = initialBoard(total)
    images = table(board, cards)
    score = 0

else:
    # Get cookie values
    cookie = C['board'].value
    card1 = C['card1'].value
    card2 = C['card2'].value
    matched = int(C['matched'].value)
    attempts = int(C['attempts'].value)

    board = getCookie(cookie)
    newBoard = flip(int(card), board)

    if card1 == "" and card2 == "":
        C['card1'] = card
    if len(card1) != 0 and card2 == "":
        C['card2'] = card

    if len(card1) != 0 and len(card2) != 0:
        if cards[int(card1)] == cards[int(card2)]:
            matched += 1
            score = getScore(matched, attempts)
            board = getCookie(cookie)
            newBoard = flip(int(card1), board)
            newBoard = flip(int(card2), newBoard)
            C['board'] = setCookie(newBoard)
            C['card1'] = ""
            C['card2'] = ""
            C['matched'] = str(matched)
            C['attempts'] = str(attempts)
            print(C)
            images = table(newBoard, cards)
        else:
            attempts += 1
            score = getScore(matched, attempts)
            board = getCookie(cookie)
            newBoard = noFlip(int(card1), board)
            newBoard = noFlip(int(card2), newBoard)
            C['board'] = setCookie(board)
            C['card1'] = ""
            C['card2'] = ""
            C['attempts'] = str(attempts)
            C['matched'] = str(matched)
            print(C)
            images = table(newBoard, cards)
    else:
        score = getScore(matched, attempts)
        C['board'] = setCookie(newBoard)
        C['attempts'] = str(attempts)
        C['matched'] = str(matched)
        print(C)
        images = table(newBoard, cards)

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

template("Golden Stars Memorama", images, attempts, matched, score)
