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

def stepper_Sequence(response,port,i_Range, speed,  Steps):
    for i in range(5):
        print("\nAttempt " , i + 1 , " of 5 \n")
        with alive_bar(i_Range) as bar:   # default setting
            for i in range(i_Range):
                sleep(speed)
                bar()
                uart_Packager(response,port,hk = False,cmdInput= "10" + Steps + "00000000") #Driving to base stop
        typewrite("\n----------Now Resetting Motor for start of test sequencing---------\n",speed)
        uart_Packager(response,port,hk = False,cmdInput= "11210000000000") #Driving to base stop
        sleep(26)