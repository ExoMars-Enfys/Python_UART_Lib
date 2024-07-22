from time import sleep
from progress.spinner import MoonSpinner
from alive_progress import alive_bar
from uart_comms import uart_Packager
from typewriter import typewrite
from hk import Housekeeping_stream

def load(speed):
    with MoonSpinner('Loading  ') as bar:
        for i in range(60):
            sleep(speed)
            bar.next()


def progressbar_move(response,port,filename,i_Range,speed):
    with alive_bar(i_Range) as bar:   # default setting
        for i in range(i_Range):
            Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename)
            sleep(speed)
            bar()
            
