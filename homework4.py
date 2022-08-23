from test12 import colors
from time import sleep
for i in range(5):
    for color in colors:
     sleep(1)
     print(color + "\n"*7)
     