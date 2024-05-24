import sys
from time import sleep
def typewrite(text,speed):
         for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                sleep(speed)     