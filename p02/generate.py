import os
import glob
from pathlib import PureWindowsPath

# Path
# Get the relative path of the current file with:
# os.path.relpath(__file__)
# Get the directory name with:
# os.path.dirname()
path = os.path.dirname(os.path.relpath(__file__))

# Get the Windows path in order to get the Posix Path
p = PureWindowsPath(os.path.dirname(__file__))

# Image formats
extensions = ['png', 'jpg', 'jpeg', 'gif']

# Read files
f = open(os.path.join(path, 'index.html'), 'w')
t = open(os.path.join(path, 'titulo.txt'), 'r')
d = open(os.path.join(path, 'descripcion.txt'), 'r')
c = open(os.path.join(path, 'campo3.txt'), 'r')

titulo = t.read()
descripcion = d.read()
campo3 = c.read()

t.close()
d.close()
c.close()

# Save all images from directory
files = []
[files.extend(glob.glob(p.as_posix() + '/batch/*.' + e)) for e in extensions]

# Concatenate images
imagenes = ''
for file in files:
    imagenes += '<div class="gallery-image"><img src="./batch/' + os.path.basename(file) + '" class="image"></div>\n'

# Format text in HTML document

pagina = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> """+titulo+"""</title>
    <link rel="stylesheet" href="./css/style.css">
</head>

<body>
    <h1>\n""" + titulo + """\n</h1>

    <p class="parrafo">\n""" + descripcion + """\n</p>

    <p class="campo">\n""" + campo3 + """\n</p>
    <!-- Popup -->
    <div class="popup">
        
        <!-- Top bar -->
        <div class="top-bar">
            <p class="image-name">1.png</p>
            <span class="close-btn"></span>
        </div>

        <!-- Arrows -->
        <button class="arrow-btn left-arrow"><img src="./img/arrow.png" alt=""  class="arrow"></button>
        <button class="arrow-btn right-arrow"><img src="./img/arrow.png" alt="" class="arrow"></button>
        <!-- image -->
        <img src="img/1.png" class="large-image" alt="">
        <!-- image-init -->
        <h2 class="index">01</h1>
    </div>


    <div class="gallery">
        """+imagenes+"""
    </div>
    <script src="./js/app.js"></script>
</body>

</html>
"""

f.write(pagina)
f.close()
