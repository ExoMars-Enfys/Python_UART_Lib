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

def uart_Packager(response,port,hk,cmdInput):
    port.write(crc8Calculate(cmdInput))
    response = port.read(72)
    print(bytes(response).hex())
    if hk == True:
        Housekeeping_Parser(response)
    return response
