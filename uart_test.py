#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#--------------Mech Board Artix 7 CMD Interpreter-------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#
import serial
from time import sleep
import sys
import crc8
import os
from uiLib import UI

#-------------------------Initialisation----------------------------#
portnum = "COM4"                                                                        #Serial Port initialisation
#cmdParam =   b'\x0A\x61\xA8\x00\x06\x0A\x7f'                                            #CMD to Artix7
#cmdInput =   b'100FFF00000000'
exit_flag =0
output = b''
responseCMD= b''
i =0
filename = ""
port = serial.Serial(port = portnum,                                                    #Serial Port Initialisation
                     baudrate=115200,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_ODD,
                     stopbits = serial.STOPBITS_ONE,
                     timeout = 0.5)
port.flushOutput()                                                                      #Port Flushing to clear port
port.flushInput()
text = "----------------------------------------------\n---ExoMars Rosalind Franklin Rover - Enfys---\n-----Mech Board Artix 7 CMD Interpreter-----\n----------Giorgos Kollakides - MSSL---------"
def typewrite(text):
         for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                sleep(0.005)       
def load():
        for i in range(25):
                sys.stdout.write("-")
                sys.stdout.flush()
                sleep(0.005)
#--------------------CRC8 Parity Generator--------------------------#
def crc8Calculate(cmdInput) :        
        hash = crc8.crc8()
        print("\nThe Packet to be Parity checked : " ,cmdInput, type(cmdInput))
        load()
        hash.update(cmdInput)
        crc8Frame = hash.digest()
        print("\nCRC is {} ({})".format(crc8Frame, type(crc8Frame)) )
        load()
        return crc8Frame 
#-----------------Repetitive Function--------------------------#
def cmdGetter(exit_flag):
        cmdInput = UI(output)
        print("\nAttempting to Write to Artix 7")
        load()  
        HashedInput = cmdInput + crc8Calculate(cmdInput)
        cmdsent = port.write(HashedInput)                                   #Initialise Transmission and Transmission Counter Incrementation
        print("\nSent" , cmdsent, "bytes in the form :", HashedInput.hex())
        load()
        responseCMD = port.read(42)                                             #Read the Response from the Artix7
        print("\n Response from Artix 7 :", responseCMD.hex())                  #Output the Response from the Artix 7 to the user
        if len(responseCMD) == 0:
                        print("NO RESPONSE FROM ARTIX 7 ***ERROR***")
                        exit_flag = 1
                        exit()  #Raise program end exit flag
        return exit_flag        

#--------------------File Functions--------------------------#
#def openCMDFile (filename):


#------------------------Main Function-----------------------------#
while(1):
        inFlag = input("\n Do you wish to Start? (Y/N)")
        match inFlag:
                case "Y":
                        typewrite("\nStarting Program")
                case "N":
                        typewrite("\nNow exiting Program")
                        typewrite("\nGoodbye :)")
                        exit()
        if (port.open and inFlag == "Y") :                                                                  #Check that the port is active
                os.system('cls')
                typewrite(text)
                print("\nArtix 7 Port open and connected to: " + port.portstr)         #Print Connection Message
                cmdGetter(exit_flag)
                inFlag = input("\n Do you wish to Continue? (Y/N)")
                match inFlag:
                        case "Y":
                                typewrite("\nRestarting Program")
                        case "N":
                                typewrite("\nNow exiting Program")
                                typewrite("\nGoodbye :)")
                                inFlag = ""
                                exit()
        elif exit_flag == 1:        
                typewrite(text)
                print("\nPort", port.portstr, "Failed to Open")                         #Port Connection error
                port.close()
                exit()