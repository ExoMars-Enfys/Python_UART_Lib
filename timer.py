from time import sleep
from progress.spinner import MoonSpinner
from alive_progress import alive_bar
from uart_comms import uart_Packager
from typewriter import typewrite

def load(speed):
    with MoonSpinner('Loading  ') as bar:
        for i in range(25):
            sleep(speed)
            bar.next()


def progressbar_move(i_Range,speed):
    with alive_bar(i_Range) as bar:   # default setting
        for i in range(i_Range):
            sleep(speed)
            bar()