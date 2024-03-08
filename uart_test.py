#-------------------------------------------------------------------#
#------------ExoMars Rosalind Franklin Rover - Enfys----------------#
#--------------Mech Board Artix 7 CMD Interpreter-------------------#
#-------------------Giorgos Kollakides - MSSL-----------------------#
import serial
import time
import sys

#-------------------------Initialisation----------------------------#
portnum = "COM4"                                                                #Serial Port initialisation
portTest = b'\x01\x00\x00\x00\x00\x00\x00\xDF'                                  #CMD to Artix7
portResponseTest = b""                                                          #Initialising Response bytearray
isBytessent = 0                                                                 #Initialising Bytes sent check counter
exitflag = 0                                                                    #Initialising exitflag
port = serial.Serial(port = portnum,                                            #Serial Port open
                     baudrate=115200,
                     bytesize = serial.EIGHTBITS,
                     parity = serial.PARITY_ODD,
                     stopbits = serial.STOPBITS_ONE,
                     timeout= 10)
port.flushOutput()                                                              #Port Flushing to clear port
port.flushInput()

#------------------------Main Function-----------------------------#
while True:
        if port.open :                                                          #Check that the port is active
                print(" Port open and connected to: " + port.portstr)           #Print Connection Message
                isBytessent = port.write(portTest)                              #Initialise Transmission and Transmission Counter Incrementation
                print("Attempting to Write to Port")
                print("Command type : ", type(portTest))                        #Check the format and type of the bytearray being sent
                print("Sent" , isBytessent, "bytes in the form :", portTest)
                for i in range(15) :
                        print("-" , end =" ") ; time.sleep(0.05)
                portResponseTest = port.read(42)                                #Read the Response from the Artix7
                print("\n", portResponseTest.hex())                             #Output the Response from the Artix 7 to the user
                exitflag = 1                                                    #Raise program end exit flag

                if exitflag == 1:                                               #Exit Program
                        exit()
        else:
                print("Port", port.portstr, "Failed to Open")                   #Port Connection error
        port.close()
        exit()

