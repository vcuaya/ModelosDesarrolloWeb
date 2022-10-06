#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

titulo = form.getvalue("titulo")
descripcion = form.getvalue("descripcion")
campo = form.getvalue("campo")

# HTML is following
print('Content-Type: text/html')

# Leave a blank line
print('')

print (titulo + descripcion + campo + " desde Python")

#############################
#############################
