#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#----------------EGSE w/ Artix 7 CMD Interpreter--------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#

#--------------------------Module Imports---------------------------#
from crc8Function import crc8Calculate
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

#-------------------------Main Function-----------------------------#
def main():
    typewrite("----------------------------------------------\n---ExoMars Rosalind Franklin Rover - Enfys---\n-----Mech Board Artix 7 CMD Interpreter-----\n----------Giorgos Kollakides - MSSL---------\n\n\n")
    typewrite("\n----------Welcome. Now starting EGSE Program---------")
    sleep(1)
    inputCmd = input("\n Would you like to initialise the UART connection to ARTIX 7? Y/N \n \n")
    match inputCmd:
        case "Y":
            uart_comms.uart_openport(port)
        case "N" :
            typewrite("\n Restarting Program")
            main()
    cmdInput = UI(output)
    typewrite(text = ("\n You have chosen the following command : ",cmdInput))
    typewrite("\n Now parsing and adding crc8 parity frame at the end of the packet")
    HashedInput = crc8Calculate(cmdInput)    
    load(0.05)
    uart_comms.uart_Send(HashedInput)    
    load(0.05)
    uart_comms.uart_Receive(response)
    load(10)
    

    return
while(1):
    main()
    exit()                    