from random import random
import sys
import os

# Get path to mymodule
scriptPath = os.path.dirname(__file__)
modulePath = os.path.join(scriptPath, 'p04', 'img')
sys.path.append(modulePath)
import images

list = images.get()
random.shuffle(list)

print(list)
