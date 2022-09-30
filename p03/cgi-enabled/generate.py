#!/usr/bin/env python3
import cgi
import os
import glob
from pathlib import PureWindowsPath

# Format text in HTML document
def plantilla(titulo, descripcion, campo, imagenes):
    print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>""" + titulo + """</title>
    <link rel="stylesheet" href="../css/style.css">
</head>

<body>
    <h1>\n""" + titulo + """\n</h1>

    <p class="parrafo">\n""" + descripcion + """\n</p>

    <p class="campo">\n""" + campo + """\n</p>
    
    <!-- Popup -->
    <div class="popup">
        
        <!-- Top bar -->
        <div class="top-bar">
            <p class="image-name">1.png</p>
            <span class="close-btn"></span>
        </div>

        <!-- Arrows -->
        <button class="arrow-btn left-arrow"><img src="../img/arrow.png" alt=""  class="arrow"></button>
        <button class="arrow-btn right-arrow"><img src="../img/arrow.png" alt="" class="arrow"></button>
        
        <!-- image -->
        <img src="img/1.png" class="large-image" alt="">
        
        <!-- image-init -->
        <h2 class="index">01</h1>
    </div>

    <div class="gallery">
        """ + imagenes + """
    </div>
    <script src="../js/app.js"></script>
</body>

</html>
""")


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

# Variable to get values from send it form
form = cgi.FieldStorage()

# titulo = form.getvalue("titulo")
# descripcion = form.getvalue("descripcion")
# campo = form.getvalue("campo")
page = form.getvalue("page")

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

# Save all images from directory
files = []

# Concatenate images using 3 options
imagenes = ''

if (str(page) == '1'):
    titulo = "Inmuebles Kaiser"
    descripcion = "Todas las casas se distinguen por tener un moderno diseño interior que aprovecha al máximo los espacios. Los colores, texturas y formas, tanto de fachadas como de interiores, se integran perfectamente con el entorno y permanecen atractivas con el paso del tiempo."
    campo = "Desde $ 1, 000 000.00"
    [files.extend(glob.glob(p.as_posix() + '/batch1/*.' + e))
     for e in extensions]
    for file in files:
        imagenes += '<div class="gallery-image"><img src="./batch1/' + \
            os.path.basename(file) + '" class="image"></div>\n'
    plantilla(titulo, descripcion, campo, imagenes)

elif (str(page) == '2'):
    titulo = "Autos Mars"
    descripcion = "Los Precios aquí establecidos, son de lista en Moneda Nacional de los Estados Unidos Mexicanos, aplica para CUPRA León MY 2023 en compra de contado e Impuesto al Valor Agregado (IVA), así como el Impuesto Sobre Autos Nuevos (ISAN cuando aplique). Estos precios únicamente son para el año modelo y versiones de los vehículos aquí mencionados y estarán vigentes del 01 al 30 de septiembre del 2022. Los precios pueden variar dependiendo de la versión y equipamiento del vehículo, por tal motivo para mayor información consulte a su Distribuidor autorizado CUPRA."
    campo = "$1 , 500 000.00"
    [files.extend(glob.glob(p.as_posix() + '/batch2/*.' + e))
     for e in extensions]
    for file in files:
        imagenes += '<div class="gallery-image"><img src="./batch2/' + \
            os.path.basename(file) + '" class="image"></div>\n'
    plantilla(titulo, descripcion, campo, imagenes)

elif (str(page) == '3'):
    titulo = "Paisajes"
    descripcion = "Los mejores paisajes que puedas ver desde tu equipo de computo"
    campo = "Descargar"
    [files.extend(glob.glob(p.as_posix() + '/batch3/*.' + e))
     for e in extensions]
    for file in files:
        imagenes += '<div class="gallery-image"><img src="./batch3/' + \
            os.path.basename(file) + '" class="image"></div>\n'
    plantilla(titulo, descripcion, campo, imagenes)
