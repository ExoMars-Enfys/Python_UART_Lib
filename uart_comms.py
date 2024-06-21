import serial
import os
from time import sleep
from typewriter import typewrite
from hk import Housekeeping_Parser
from crc8Function import crc8Calculate
port = ""
speed = 0.005

def uart_openport(port):
    match port:
        case port if port.is_open == True:
            os.system('cls')
            print("\n---Now Connected to Artix 7 with settings: ---",
                "\n---Baudrate : " , port.baudrate , " Bauds",
                "\n---Bytesize : ",port.bytesize," Bits",
                "\n---Parity : ",port.parity,
                "\n---Timeout : ",port.timeout," Seconds")
        case port if  port.is_open == False:
            typewrite(text = ("\n Port ", port.portstr, " failed to open!"),speed=0.005)
            typewrite("\n Now Retrying to Initialise port",speed)
            uart_openport(port)
    return port

def uart_Send (HashedInput,port):
    #print("\nAttempting to Write to Artix 7")
    sleep(0.005)  
    cmdsent = port.write(HashedInput)            
   # print ("\n Now Sending Packet : ", HashedInput.hex(), " of size ", cmdsent)
    return
       
def uart_Receive(response,port) :
    response = port.read(50)                                             #Read the Response from the Artix7
    #print("\n Response from Artix 7 :", response.hex())                  #Output the Response from the Artix 7 to the user
    return response

def uart_Packager(response,port,hk,cmdInput):
    #typewrite(text = ("\n You have chosen the following command : "+ cmdInput),speed=0.005)
    #typewrite("\n Now parsing and adding crc8 parity frame at the end of the packet\n" ,speed = 0.005)
    HashedInput = crc8Calculate(cmdInput)    
    sleep(0.05)
    uart_Send(HashedInput,port)    
    sleep(0.05)
    response = uart_Receive(response,port)
    #print(response)
    if hk == True:
        Housekeeping_Parser(response)
    return