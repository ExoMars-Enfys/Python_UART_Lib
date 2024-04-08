import sys
from time import sleep
def typewrite(text):
         for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                sleep(0.005)     