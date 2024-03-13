#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#--------------Mech Board Artix 7 CMD Interpreter-------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#
import serial
import time
import sys
import crc8

#-------------------------Initialisation----------------------------#
portnum = "COM4"                                                                #Serial Port initialisation
cmdInput =   b'\x1f\x00\x00\x00\x00\x00\x00'                                  #CMD to Artix7
responseCMD= b''                                                          #Initialising Response bytearray
isBytessent = 0                                                                 #Initialising Bytes sent check counter
exitflag = 0 
errorFlag = 0                                                                   #Initialising exitflag
hash
crc8Frame = ''
HashedInput = b''

port = serial.Serial(port = portnum,                                            #Serial Port open
                     baudrate=115200,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_ODD,
                     stopbits = serial.STOPBITS_ONE,
                     timeout= 0.5)
port.flushOutput()                                                              #Port Flushing to clear port
port.flushInput()


def crc8Calculate(cmdInput) :
        hash = crc8.crc8()
        print(cmdInput, type(cmdInput))
        hash.update(cmdInput)
        crc8Frame = hash.digest()
        crccheck = crc8Frame.hex()        
        print(crccheck)
        if crccheck.isalnum() == False:
                print("Error with the CRC Calculation try a different packet")
                print(crccheck)
                exit()
        else:
                print("CRC is {} ({})".format(crc8Frame, type(crc8Frame)) )
                return crc8Frame 

#------------------------Main Function-----------------------------#
while errorFlag == 0:
        if port.open :                                                          #Check that the port is active
                print(" Port open and connected to: " + port.portstr)           #Print Connection Message
                # if not int(crc8Calculate(cmdInput)) in range(0,255) :
                #         errorFlag =1
                #cnvrtInput = bytearray(cmdInput)
                HashedInput = cmdInput + crc8Calculate(cmdInput)
                print(HashedInput , type(HashedInput))
                isBytessent = port.write(HashedInput)                              #Initialise Transmission and Transmission Counter Incrementation
                print("Attempting to Write to Port")
                print("Command type : ", type(HashedInput))                        #Check the format and type of the bytearray being sent
                print("Sent" , isBytessent, "bytes in the form :", HashedInput.hex())
                responseCMD = port.read(42)                                #Read the Response from the Artix7
                print("\n", responseCMD.hex())                             #Output the Response from the Artix 7 to the user
                exitflag = 1                                                    #Raise program end exit flag

                if exitflag == 1:                                               #Exit Program
                        exit()
        else:
                print("Port", port.portstr, "Failed to Open")                   #Port Connection error
                port.close()
                exit()

