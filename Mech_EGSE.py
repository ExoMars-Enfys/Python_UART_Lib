#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#----------------EGSE w/ Artix 7 CMD Interpreter--------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#

#--------------------------Module Imports---------------------------#
from crc8Function import crc8Calculate
import serial
import os
import uart_comms
from time import sleep
from timer import load
from uiLibV2 import UI
from typewriter import typewrite
from binascii import unhexlify
#-------------------------Initialisation----------------------------#
output = ""
port=""
inputCmd = ""
response =""
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
    typewrite("----------------------------------------------\n---ExoMars Rosalind Franklin Rover - Enfys---\n-----Mech Board Artix 7 CMD Interpreter-----\n----------Giorgos Kollakides - MSSL---------\n\n\n")
    typewrite("\n----------Welcome. Now starting EGSE Program---------")
    sleep(1)
    def mainLoop():
        cmdInput = UI(output)
        typewrite(text = ("\n You have chosen the following command : ",cmdInput))
        typewrite("\n Now parsing and adding crc8 parity frame at the end of the packet\n")
        HashedInput = crc8Calculate(cmdInput)    
        load(0.05)
        uart_comms.uart_Send(HashedInput,port)    
        load(0.05)
        uart_comms.uart_Receive(response,port)
        # load(10)
        sleep(1)
        inputCmd = input("\n Would you like to run another test? Y/N \n \n")
        match inputCmd:
            case "Y":
                mainLoop()
            case "N" :
                inputCmd = input("\n Would you like to Exit the program? Y/N \n \n")
                match inputCmd:
                    case "Y":
                        typewrite("\n Now exiting. ~~~Goodbye~~~")
                        exit()
                    case "N" :
                        typewrite("\n Restarting Program")
                        main()
                    case _:
                        print("\n Not a valid input, please Try Again\n")
            case _:
                print("\n Not a valid input, please Try Again\n")
        return
    
    inputCmd = input("\n Would you like to initialise the UART connection to ARTIX 7? Y/N \n \n")
    match inputCmd:
        case "Y":
            uart_comms.uart_openport(port)
            mainLoop()
        case "N" :
            typewrite("\n Restarting Program")
            main()
        case _:
            print("\n Not a valid input, please Try Again\n")
    return
while(1):
    main()                    