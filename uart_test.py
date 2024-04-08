#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#--------------Mech Board Artix 7 CMD Interpreter-------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#
import serial
from time import sleep
import sys
import crc8
import os
from Mech_EGSE import UI
from binascii import unhexlify

#-------------------------Initialisation----------------------------#
portnum = "COM4"                                                                        #Serial Port initialisation

exit_flag =0
cmdInput = ''
responseCMD= b''
i =0
filename = ""
time = 0
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
def load(time):
        for i in range(25):
                sys.stdout.write("-")
                sys.stdout.flush()
                sleep(time)
#--------------------CRC8 Parity Generator--------------------------#
def crc8Calculate(cmdInput) :        
        hash = crc8.crc8()
        # print("\nThe Packet to be Parity checked : " ,cmdInput, type(cmdInput))
        # load(0.005)
        hash.update(cmdInput)
        # print("\nType check : " ,cmdInput, type(cmdInput))
        crc8Frame = hash.digest()
        # print("\nCRC is {} ({})".format(crc8Frame, type(crc8Frame)) )
        # load(0.005)
        return crc8Frame 
#-----------------Repetitive Function--------------------------#
def cmdGetter(cmdInput):
        # cmdInput = UI(output)
        cmdInput = unhexlify(cmdInput)
        # print("\nAttempting to Write to Artix 7")
        # load(0.005)  
        HashedInput = cmdInput + crc8Calculate(cmdInput)
        cmdsent = port.write(HashedInput)                                   #Initialise Transmission and Transmission Counter Incrementation
        # print("\nSent" , cmdsent, "bytes in the form :", HashedInput.hex(), type(HashedInput))
        # load(0.005)
        responseCMD = port.read(42)                                             #Read the Response from the Artix7
        print("\n Response from Artix 7 :", responseCMD.hex())                  #Output the Response from the Artix 7 to the user
        # if len(responseCMD) == 0:
        #                 print("NO RESPONSE FROM ARTIX 7 ***ERROR***")
        #                 exit_flag = 1
        #                 exit()  #Raise program end exit flag
        # return exit_flag        

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
                cmd = ["00"] *7
        cmd[0] = input("\nEnter the Test ID\n" 
                        + "\nAvailable Options: " 
                        + "\n 1.  01 Full Sweep (Base to Outer)"
                        + "\n 2.  02 Drive to Base End Stop and do 10 * 1mm sweeps"
                        + "\n 3.  03 Drive to Outer End Stop and do 10 * 1mm sweeps"
                        + "\n 4.  04 Drive back to Base"
                        + "\n 5.  05 Drive back to Outer\n")
        match cmd[0]:
                case "01" :
                        print("\n Now attempting test number 1. Full Sweep")
                        for i in range (0,2):
                                print("\n Driving to Base End stop for homing")
                                cmdGetter(cmdInput = '0AA000000C0F7F')
                                cmdGetter(cmdInput = '1020EE00000000')                         
                                load(1.15)                                
                                cmdGetter(cmdInput = '00000000000000')
                                cmdGetter(cmdInput = '1120EE00000000')                         
                                load(1.15)                                
                                cmdGetter(cmdInput = '00000000000000')
                        # load(0.08)             
                        # print("\n Driving to Outer End stop for full sweep")                        
                        # load(0.08)            
                        # cmdGetter(cmdInput = '110FFF00000000')
                case "02" :
                        print("\n Now attempting test number 2. Drive to Base End Stop and do 10 * 1mm sweeps")
                        print("\n Driving to Base End stop for homing")
                        cmdGetter(cmdInput = '0AA000000C0F7F')
                        load(0.08)                        
                        cmdGetter(cmdInput = '1753000000000') 
                        load(0.08)                        
                        cmdGetter(cmdInput = '1000C000000000')
                        load(0.08)
                        cmdGetter(cmdInput = '11000000000000' )         
                        print("\n Full 10 * 1mm Sweep")
                        for i in range(0,49):
                                print("\n\n\n\n\n\n\n Now attempting move number : " , i+1)
                                cmdGetter(cmdInput = '10004000000000')
                                cmdGetter(cmdInput = '11000000000000')
                                load(0.08)
                        cmdGetter(cmdInput = '10000000000000')
                        load(0.08)                        
                        cmdGetter(cmdInput = '11753000000000')
                case "05":
                        print("\n Driving to Outer End stop")
                        cmdGetter(cmdInput = '0A600000060F7F')
                        cmdGetter(cmdInput = '112FFF00000000')   
        # elif exit_flag == 1:        
        #         typewrite(text)
        #         print("\nPort", port.portstr, "Failed to Open")                         #Port Connection error
        #         port.close()
        #         exit()