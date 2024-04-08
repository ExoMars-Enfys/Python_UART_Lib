import serial
import os
from timer import load
from typewriter import typewrite
port = ""
def uart_initialiser(port):
    port = serial.Serial(port = "COM6",                                                    #Serial Port Initialisation
                    baudrate=115200,
                    bytesize = serial.EIGHTBITS,
                    parity = serial.PARITY_ODD,
                    stopbits = serial.STOPBITS_ONE,
                    timeout = 0.5)
    port.flushOutput()                                                                      #Port Flushing to clear port
    port.flushInput()
    return port

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
            typewrite(text = ("\n Port ", port.portstr, " failed to open!"))
            typewrite("\n Now Retrying to Initialise port")
            uart_openport(port)
    return port

def uart_Send (HashedInput,port):
    print("\nAttempting to Write to Artix 7")
    load(0.005)  
    cmdsent = port.write(HashedInput)            
    print ("\n Now Sending Packet : ", HashedInput, " of size ", cmdsent)
    return
       
def uart_Receive(response,port) :
    response = port.read(42)                                             #Read the Response from the Artix7
    print("\n Response from Artix 7 :", response.hex())                  #Output the Response from the Artix 7 to the user
    return response