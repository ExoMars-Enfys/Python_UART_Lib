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
#cmdInput =   b'\x10\x0F\xFF\x00\x00\x00\x00'
i =0
filename = ""
port = serial.Serial(port = portnum,                                                    #Serial Port Initialisation
                     baudrate=115200,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_ODD,
                     stopbits = serial.STOPBITS_ONE,
                     timeout= 2)
port.flushOutput()                                                                      #Port Flushing to clear port
port.flushInput()
text = "----------------------------------------------\n---ExoMars Rosalind Franklin Rover - Enfys---\n-----Mech Board Artix 7 CMD Interpreter-----\n----------Giorgos Kollakides - MSSL---------"
def typewrite(text):
         for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                sleep(0.03)       
def load():
        for i in range(25):
                sys.stdout.write("-")
                sys.stdout.flush()
                sleep(0.03)
#--------------------CRC8 Parity Generator--------------------------#
def crc8Calculate(cmdInput) :        
        hash = crc8.crc8()
        print("\nThe Packet to be Parity checked : " ,cmdInput, type(cmdInput))
        load()
        hash.update(cmdInput)
        crc8Frame = hash.digest()
        print("\nCRC is {} ({})".format(crc8Frame.hex(), type(crc8Frame)) )
        load()
        return crc8Frame 

#--------------------File Functions--------------------------#
#def openCMDFile (filename):


#------------------------Main Function-----------------------------#
while(1):
        if port.open :                                                                  #Check that the port is active
                os.system('cls')
                typewrite(text)
                print("\nArtix 7 Port open and connected to: " + port.portstr)          #Print Connection Message
                cmdInput = UI()
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
                exitflag = 1                                                            #Raise program end exit flag

                if exitflag == 1:                                                       #Exit Program
                        exit()
        else:
                typewrite(text)
                print("\nPort", port.portstr, "Failed to Open")                         #Port Connection error
                port.close()
                exit()

