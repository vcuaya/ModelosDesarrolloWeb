#!/usr/bin/env python3

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

# Format text in HTML document
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

plantilla("CGI")
