#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#----------------EGSE w/ Artix 7 CMD Interpreter--------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#

#--------------------------Module Imports---------------------------#
import serial
from time import sleep
from timer import load
from uiLibV2 import UI
from uiLibV2 import Freewill
from uiLibV2 import Sequences
from uart_comms import uart_Packager
from typewriter import typewrite
from datetime import datetime
from timer import progressbar_move
#-------------------------Initialisation----------------------------#
output = ""
port=""
inputCmd = ""
response =""
filename = ""
speed = 0.005
#---------------------FPGA Boot and Connect-------------------------#
port = serial.Serial(port = "COM9",                                                    #Serial Port Initialisation
                    baudrate=115200,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_ODD,
                    stopbits = serial.STOPBITS_ONE,
                    timeout = 0.5)
port.flushOutput()                                                                      #Port Flushing to clear port
port.flushInput()
#-------------------------Main Function-----------------------------#
def main():
    print("----------------------------------------------\n---ExoMars Rosalind Franklin Rover - Enfys---\n-----Mech Board Artix 7 CMD Interpreter-----\n----------Giorgos Kollakides - MSSL---------\n\n")
    typewrite("\n----------Welcome. Now starting EGSE Program---------\n",speed)
    print(datetime.now())
    load(0.0417)
    print(datetime.now())
    def mainLoop():
        startupcmd = input("\n Please choose the type of run you would like to carry out"
                       +"\n Available options are: "
                       +"\n 1. Run Free-Will Commands"
                       +"\n 2. Run Testbench Sequences"
                       +"\n 0. Exit Program\n")
        match startupcmd :
            case "1" :
                Freewill(port,hk=False)
            case "2":
                motorpos = input("\n---Is the Motor currently positioned at the outer stop? (Y/N)---\n")
                match motorpos:
                    case "Y":
                        Sequences(port)
                    case "N":
                        typewrite("\n----------Now Resetting Motor for start of test sequencing---------\n",speed)
                        uart_Packager(response,port,hk = False,cmdInput= "0A61A800060FFF") #Setting nominal motor drive parameters
                        uart_Packager(response,port,hk = False,cmdInput= "0B7F0064380005") #Setting nominal motor guard parameters
                        uart_Packager(response,port,hk = False,cmdInput= "0C3200320000A0") #Setting Limits
                        sleep(0.05)
                        uart_Packager(response,port,hk = False,cmdInput= "13010000000000") #Driving to Outer Stop
                        progressbar_move(response,port,filename,i_Range = 26,speed = 0.4)
                        Sequences(port)
            
            case "0" :
                exit_flag = input("\n Are you sure you want to exit? Y/N")
                match exit_flag:
                    case"Y":
                        print("~~~Goodbye~~~")
                        exit()
                    case"N":
                        UI(output)
            case _:
                print("\n Not a valid input, please Try Again\n")
        sleep(1)
        return
    mainLoop()
    return
   
while(1):
    main()                    