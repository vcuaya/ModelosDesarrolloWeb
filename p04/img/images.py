from email.mime import image
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

# Save all images from directory
files = []
[files.extend(glob.glob(p.as_posix() + '/*.' + e)) for e in extensions]

# Concatenate images
images = []
for file in files:
    images.append('<td><img src="./../p04/img/' + os.path.basename(file) + '"></td>\n')

# Returns the images array
def get():
    return images