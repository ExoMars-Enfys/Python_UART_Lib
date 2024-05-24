#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#----------------EGSE w/ Artix 7 CMD Interpreter--------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#

#--------------------------Module Imports---------------------------#
import serial
from time import sleep
from uiLibV2 import UI
from uiLibV2 import Freewill
from typewriter import typewrite
#-------------------------Initialisation----------------------------#
output = ""
port=""
inputCmd = ""
response =""
speed = 0.005
#---------------------FPGA Boot and Connect-------------------------#
port = serial.Serial(port = "COM4",                                                    #Serial Port Initialisation
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
    sleep(0.3)
    def mainLoop():
        startupcmd = input("\n Please choose the type of run you would like to carry out"
                       +"\n Available options are: "
                       +"\n 1. Run Free-Will Commands"
                       +"\n 2. Run Testbench Sequences"
                       +"\n 0. Exit Program\n")
        match startupcmd :
            case "1" :
                Freewill(port)
            case "2":
                print("Do things here")
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