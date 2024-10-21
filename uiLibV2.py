import os
from uart_comms import uart_Packager
from timer import load
from time import sleep
from timer  import progressbar_move
from fileHandler import fileWriter
from hk import Housekeeping_stream
from operator import*
import keyboard
#from video_handler import videostart

output = ""
port=""
inputCmd = ""
response =""
HK_Reading = ""
speed = 0.005

def UI(output,hk) :
    

    cmd = ["00"] *7
    exit_flag = ""
    
    cmd[0] = input("\nEnter the Command ID\n" 
        + "\nAvailable Options: " 
        + "\n --------------------------------------------------------"
        + "\n | CMD ID | Command Description                   |"
        + "\n --------------------------------------------------------"
        + "\n |   P    | Go to Parked Position                 |"
        + "\n |   00   |  Request Housekeeping                 |"
        + "\n |   01   |  Clear Errors                         |"
        + "\n |   04   |  Power Controls                       |"
        + "\n |   05   |  Heater Controls                      |"
        + "\n |   06   |  Set Mechanism SP                     |"
        + "\n |   07   |  Set Detector SP                      |"
        + "\n |   0A   |  Set Motor Drive Parameters           |"
        + "\n |   0B   |  Set Motor Drive Guards               |"
        + "\n |   0C   |  Set Motor Monitor Limits             |"
        + "\n |   0D   |  Set Motor Error Masks                |"
        + "\n |   10   |  Move Motor Forwards                  |"
        + "\n |   11   |  Move Motor Backwards                 |"
        + "\n |   12   |  Move Motor to Absolute Position      |"
        + "\n |   13   |  Drive Motor to Chosen End Switch     |"
        + "\n |   15   |  Homing and Calibration               |"
        + "\n |   1F   |  Request Science Reading              |"
        + "\n ------------------------------------------------------ --\n")
    match cmd[0]:
        case "P" : 
            print("\n Now moving to pasrked position, 5mm from Base Stop ")
            output = "121B1300000000"
            
        case "00" :
            print("\n No further parameters required. Now Requesting Housekeeping from Artix 7")
            output = "".join(cmd)
            hk = True
            
        case "01" :
            print("\n No further parameters required. Now Clearing all Errors on Artix 7")
            output = "".join(cmd) 
        
        case "04":
            os.system('cls')
            cmd[1] = input("\n Enter the Power Control Bit Mask\n" 
                            + "\n Available Options Are:"
                            + "\n 01 Power Off"
                            + "\n 01 Power on Mechanism Board"
                            + "\n 02 Power on Detector Board"
                            + "\n 03 Power on Both\n")
            match cmd[1]:
                case "00":
                    print("\n Power on of Mechanism Board selected")
                case "01":
                    print("\n Power on of Detector Board selected")
                case _:
                    print("\n Not a valid input, please Try Again\n")
            output = "".join(cmd)         
       
        case "05":
            os.system('cls')
            cmd[1] = input("\n Enter the Heater Control Bit Mask\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Toggle Mechanism Board Heaters to *AUTO* "
                            + "\n 2. 01 Toggle Mechanism Board Heaters to *MANUAL* "
                            + "\n 3. 02 Toggle Detector Board Heaters to *AUTO* "
                            + "\n 4. 03 Toggle Detector Board Heaters to *MANUAL* "
                            + "\n 5. 04 Toggle All Board Heaters to *DISABLED* when doing a Science Reading\n")
            match cmd[1]:
                case "00":
                    print("\n Mechanism Board Heaters set to AUTO")
                case "01":
                    print("\n Mechanism Board Heaters set to MANUAL")
                case "02":
                    print("\n Detector Board Heaters set to AUTO")
                case "03":
                    print("\n Detector Board Heaters set to MANUAL")
                case "04":
                    print("\n All Heaters set to DISABLED during Science Readings")
                case _:
                    print("\n Not a valid input, please Try Again\n")
            output = "".join(cmd)    
       
        case "06":
                os.system('cls')
                cmd[1] = input("\n Enter the Mechanism Board Off SP in the form XXXX\n" 
                                + "\n Available Range is: 0001 - FFFF\n")
                extract = cmd[1]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'FFFF':
                        print("\n Setting Mechanism Board OFF SP to :" , cmd[1])
                        cmd[2] = cmd[1][2:4]
                        cmd[1] = cmd[1][0:2]
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                cmd[3] = input("\n Enter the Mechanism Board On SP in the form XXXX\n" 
                                + "\n Available Range is: 0001 - FFFF\n")
                extract = cmd[3]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'FFFF':
                        print("\n Setting Mechanism Board ON SP to :" , cmd[3])
                        cmd[4] = cmd[3][2:4]
                        cmd[3] = cmd[3][0:2]
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                output = "".join(cmd)  
       
        case "07":
                os.system('cls')
                cmd[1] = input("\n Enter the Detector Board Off SP in the form XXXX\n" 
                                + "\n Available Range is: 0001 - FFFF\n")
                extract = cmd[1]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'FFFF':
                        print("\n Setting Detector Board OFF SP to :" , cmd[1])
                        cmd[2] = cmd[1][2:4]
                        cmd[1] = cmd[1][0:2]
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                cmd[3] = input("\n Enter the Detector Board On SP in the form XXXX\n" 
                                + "\n Available Range is: 0001 - FFFF\n")
                extract = cmd[3]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'FFFF':
                        print("\n Setting Detector Board ON SP to :" , cmd[3])
                        cmd[4] = cmd[3][2:4]
                        cmd[3] = cmd[3][0:2]
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                output = "".join(cmd)    
       
        case "0A":
                    os.system("cls")
                    cmd[1] = input("\n Enter Maximum Current in the form XXXX \n" 
                        + "\n Available Range is 0000 - F000\n")
                    extract = cmd[1]
                    match extract:                
                        case extract if b'0001' <= bytes(extract, 'utf-8') <=b'F000':
                            print("\n Setting Mechanism Board Current :" , cmd[1])
                            cmd[2] = cmd[1][2:4]
                            cmd[1] = cmd[1][0:2]
                            
                    cmd[3] = input("\n Enter PWM Rate in the form XXXX \n" 
                            + "\n Available Range is 0000 - 000F\n")
                    extract = cmd[3]
                    match extract:                
                        case extract if b'0001' <= bytes(extract, 'utf-8') <=b'000F':
                            print("\n Setting Mechanism Board PWM Rate :" , cmd[3])
                            cmd[4] = cmd[3][2:4]
                            cmd[3] = cmd[3][0:2]
                        case _:
                            print("\n Not a valid input, please Try Again\n")
                            
                    cmd[5] = input("\n Enter Motor Speed in the form XX \n" 
                            + "\n Available Range is 01-0F:\n")
                    extract = cmd[5]
                    match extract:                
                        case extract if b'01' <= bytes(extract, 'utf-8') <=b'0F':
                            print("\n Set Speed to : " , cmd[5])
                        case _:
                            print("\n Not a valid input, please Try Again\n")
                            
                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Range 00-FF\n ")
                    extract = cmd[6]
                    match extract:                
                        case extract if b'01' <= bytes(extract, 'utf-8') <=b'FF':
                            print("\n Set PWM Duty to : " , cmd[6])
                        case _:
                            print("\n Not a valid input, please Try Again\n")
                    print("\n Now writing Motor Drive parameters as: "
                    + "\n     Current : " + cmd[1]
                    + "\n     Pwm Rate : " + cmd[3]
                    + "\n     Speed : " + cmd[5]
                    + "\n     PWM Duty : " + cmd[6])
                                                     
                    output = "".join(cmd)        
       
        case "0B":
            os.system("cls")
            cmd[1] = input("\n Enter Recirculation Value in the Form XX \n" 
                    + "\n Available Range is 01-0F:\n")
            extract = cmd[1]
            match extract:                
                case extract if b'01' <= bytes(extract, 'utf-8') <=b'0F':
                    print("\n Set Recirculation to : " , cmd[1])
                case _:
                    print("\n Not a valid input, please Try Again\n")

            cmd[2] = input("\n Enter Guard Time in the form XXXX \n" 
                + "\n Available Range is 0000 - F000\n")
            extract = cmd[1]
            match extract:                
                case extract if b'0001' <= bytes(extract, 'utf-8') <=b'F000':
                    print("\n Setting Mechanism Board Current Guard Time :" , cmd[2])
                    cmd[3] = cmd[2][2:4]
                    cmd[2] = cmd[2][0:2]
                    
                case _:
                    print("\n Not a valid input, please Try Again\n")

            cmd[4] = input("\n Enter the RecVal \n" 
                            + "\n Available Range 00-FF\n ")
            extract = cmd[4]
            match extract:                
                case extract if b'01' <= bytes(extract, 'utf-8') <=b'FF':
                    print("\n Set RecVal to : " , cmd[4])
                case _:
                    print("\n Not a valid input, please Try Again\n")

            cmd[5] = input("\n Enter SPI Speed in the form XXXX \n" 
                    + "\n Available Range is 0000 - 000F\n")
            extract = cmd[5]
            match extract:                
                case extract if b'0001' <= bytes(extract, 'utf-8') <=b'000F':
                    print("\n Setting Mechanism Board SPI Speed :" , cmd[5])
                    cmd[6] = cmd[5][2:4]
                    cmd[5] = cmd[5][0:2]
            print("\n Now writing Guard parameters as: "
                    + "\n     Recirculation : " + cmd[1]
                    + "\n     GuardTime : " + cmd[2]
                    + "\n     RecVal : " + cmd[4]
                    + "\n     Spi Speed : " + cmd[5])                                   
            output = "".join(cmd)                 
       
        case "0C" :
            print("\n No further parameters required. Now Clearing all Errors on Artix 7")
            output = "0C320032000A0".join(cmd) 
        
        case "0D" :
            print("\n No further parameters required. Now Clearing all Errors on Artix 7")
            output = "".join(cmd) 

        case "10":
                os.system('cls')
                cmd[1] = input("\n Enter the Steps in the form XXXX\n" 
                                + "\n Available Range is: 0001 - 20EF\n")
                extract = cmd[1]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'FFFF':
                        print("\n Moving Forward" , cmd[1], "steps")
                        cmd[2] = cmd[1][2:4]
                        cmd[1] = cmd[1][0:2]
                        print("\n",cmd[1],"\n",cmd[2])
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                output = "".join(cmd)

        case "11":
                os.system('cls')
                cmd[1] = input("\n Enter the Steps in the form XXXX\n" 
                                + "\n Available Range is: 0001 - 20EF\n")
                extract = cmd[1]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'FFFF':
                        print("\n Moving Backwards" , cmd[1], "steps")
                        cmd[2] = cmd[1][2:4]
                        cmd[1] = cmd[1][0:2]
                        print("\n",cmd[1],"\n",cmd[2])
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                output = "".join(cmd)    

        case "12":
                os.system('cls')
                cmd[1] = input("\n Enter the Absolute position in the form XXXX\n" 
                                + "\n Available Range is: 0001 - 20EF\n")
                extract = cmd[1]
                match extract:                
                    case extract if b'0001' <= bytes(extract, 'utf-8') <=b'20EF':
                        print("\n Moving To" , cmd[1])
                        cmd[2] = cmd[1][2:4]
                        cmd[1] = cmd[1][0:2]
                        print("\n",cmd[1],"\n",cmd[2])
                    case _:
                        print("\n Not a valid input, please Try Again\n")
                output = "".join(cmd)    

        case "13":
            os.system('cls')
            cmd[1] = input("\n Enter homing parameters"
                           + "xxx - 1xx - Direction, x1x - Calibration, xx1 Homing"
                           + "\n05 home to base"
                           + "\n01 home to outer"
                           + "\n07 home to base with Cal"
                           + "\n03 home to outer with Cal")
            # match cmd[1]:
            #     case "00":
            #         print("\n Move to Outer End stop ")
            #     case "01":
            #         print("\n Move to Inner End stop")
            #     case "02":
            #         print("\n Move to Parked Position")
            #     case _:
            #         print("\n Not a valid input, please Try Again\n")
            output = "".join(cmd)   

        case "15" :
            halt = input("\n Would you like to hold or unhold the motor? (Y = Hold / N = Unhold) \n")
            match halt:
                case "Y":
                    print("\n -------- MOTOR HALTED! -------- \n")
                    output = "15010000000000"
                case "N":
                    print("\n -------- MOTOR RELEASED! -------- \n")
                    output = "15000000000000"
                case _:
                    print("\n Not a valid input, please Try Again\n")

        case "1F":
            os.system('cls')
            cmd[1] = input("\n Enter the Number of samples per packet in the form XX" 
                            + "\n Available Range is: 01 - FF\n")
            extract = cmd[1]
            match extract:                
                case extract if b'01' <= bytes(extract, 'utf-8') <=b'FF':
                    print("\n Set Number of samples to : " , cmd[1])
                case _:
                    print("\n Not a valid input, please Try Again\n")
                    
            cmd[2] = input("\n Enter the delay between samples" 
                            + "\n Available Range is: 01 - FF\n")
            extract = cmd[2]
            match extract:                
                case extract if b'01' <= bytes(extract, 'utf-8') <=b'FF':
                    print("\n Set Number of samples to : " , cmd[2])
                case _:
                    print("\n Not a valid input, please Try Again\n")
            output = "".join(cmd)    
        case _:
                    print("\n Not a valid input, please Try Again\n") 

    return (output,hk)

def Freewill(port,hk):    
    cmdInput,hk = UI(output,hk)
    uart_Packager(response,port,hk,cmdInput)
    

def Sequences(port):   
    cmd = ["00"] *7
    nominal_current = "61A8"
    nominal_pwm_rate = "00001"
    nominal_speed = "0F"
    nominal_pwm_duty = "FF"
    nominal_recirc = "03"
    nominal_guardtime = "0064" 
    nominal_recval = "38"
    nominal_spi = "0005"
    current = "30D4"
    pwm_rate = "0009"
    speed = "0C"
    pwm_duty = "7F"
    recirc = "00"
    guardtime = "00FA" 
    recval = "A0"
    spi = "00A0"
    absMax = "3200"
    relMax="3200"
    backoff = "00A0" 
    current_steps = ""
    sequence = input("\nSelect which sequence you would like to carry out\n" 
                            + "\n Available Options Are:"
                            + "\n N. Assert Nominal Parameters"
                            + "\n 1. Full Sweep at Full Speed * 5 times "
                            + "\n 2. Full Sweep in steps of 200μm with 300ms wait between each stop"
                            + "\n 3. Forward Steps "
                            + "\n 4. Backward Steps"
                            + "\n 5. Current Test \n")
    match sequence:
        case "N"  :
            print("\n Now writing Nominal Motor Drive parameters as: "
            + "\n     Current : " + nominal_current
            + "\n     Pwm Rate : " + nominal_pwm_rate
            + "\n     Current : " + nominal_speed
            + "\n     Current : " + nominal_pwm_duty)
            output = "".join("0A" + nominal_current + nominal_pwm_rate + nominal_speed + nominal_pwm_duty)
            uart_Packager(response,port,hk = False,cmdInput=output)
            print("\n Now writing Nominal Guard parameters as: "
            + "\n     Recirculation : " + nominal_recirc
            + "\n     GuardTime : " + nominal_guardtime
            + "\n     RecVal : " + nominal_recval
            + "\n     Spi Speed : " + nominal_spi)
            output = "".join("0B" + nominal_recirc + nominal_guardtime + nominal_recval + nominal_spi)
            uart_Packager(response,port,hk = False,cmdInput=output)
            print("\n Now writing Nominal Limit parameters as: "
                + "\n     Absolute Limit : " + absMax
                + "\n     Relative Limit : " + relMax
                + "\n     Back-Off : " + backoff)
            output = "".join("0C" + absMax + relMax + backoff)
            uart_Packager(response,port,hk = False,cmdInput=output)
        case "P"  :
            print("\n Now writing Nominal Motor Drive parameters as: "
            + "\n     Current : " + current
            + "\n     Pwm Rate : " + pwm_rate
            + "\n     Current : " + speed
            + "\n     Current : " + pwm_duty)
            output = "".join("0A" + current + pwm_rate + speed + pwm_duty)
            uart_Packager(response,port,hk = False,cmdInput=output)
            print("\n Now writing Nominal Guard parameters as: "
            + "\n     Recirculation : " + recirc
            + "\n     GuardTime : " + guardtime
            + "\n     RecVal : " + recval
            + "\n     Spi Speed : " + spi)
            output = "".join("0B" + recirc + guardtime + recval + spi)
            uart_Packager(response,port,hk = False,cmdInput=output)
            print("\n Now writing Nominal Limit parameters as: "
                + "\n     Absolute Limit : " + absMax
                + "\n     Relative Limit : " + relMax
                + "\n     Back-Off : " + backoff)
            output = "".join("0C" + absMax + relMax + backoff)
            uart_Packager(response,port,hk = False,cmdInput=output)
        case "1":
            filename = input("\n Please enter the Filename Prefix for the Video and Text Files\n")
            fileWriter(filename,"HK Data File for test : ")
            fileWriter(filename,filename)
            uart_Packager(response,port,hk = False,cmdInput= "0A61A800060FFF") #Setting nominal motor drive parameters
            uart_Packager(response,port,hk = False,cmdInput= "0B7F0064380005") #Setting nominal motor guard parameters
            uart_Packager(response,port,hk = False,cmdInput= "0C3200320000A0") #Setting Limits
            fileWriter(filename,"\n\n\nHK Packet before Movement : ")
            Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file
            for i in range(0,5):
                # load(0.0834)
                print("\nAttempt " , i + 1 , " of 5 \n")
                fileWriter(filename,"\n\nSweep #" + str(i+1))
                fileWriter(filename,"\n Outer to Base")      
                print("Driving to Base\n")
                # keyboard.wait('enter')
                uart_Packager(response,port,hk = False,cmdInput= "10219000000000") #Driving to base stop
                progressbar_move(response,port,filename = "",i_Range = 26,speed = 1)
                load(0.0834)                                
                Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file
                uart_Packager(response,port,hk = False,cmdInput= "01000000000000") #Driving to base stop
                Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file
                print("Driving to Outer\n")
                fileWriter(filename,"\nBase to Outer")
                # keyboard.wait('enter')
                uart_Packager(response,port,hk = False,cmdInput= "11219000000000") #Driving to outer stop                
                Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file
                progressbar_move(response,port,filename = "",i_Range = 28,speed = 1)
            print("\n Now Finished Test Sequence \n")
        case "2":
            # filename = input("\n Please enter the Filename Prefix for the Video and Text Files\n")
            # fileWriter(filename,"HK Data File for test : ")
            # fileWriter(filename,filename)
            uart_Packager(response,port,hk = False,cmdInput= "0A61A800060FFF") #Setting nominal motor drive parameters
            uart_Packager(response,port,hk = False,cmdInput= "0B7F0064380005") #Setting nominal motor guard parameters
            uart_Packager(response,port,hk = False,cmdInput= "0C3200320000A0") #Setting Limits
            # fileWriter(filename,"\n\n\nHK Packet before Movement : ")
            # Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file   
            print("Driving to Base\n")
            for i in range(134): 
                uart_Packager(response,port,hk = False,cmdInput= "10004000000000")
            load(0.0834)
            uart_Packager(response,port,hk = False,cmdInput= "11219000000000") #Driving to outer stop     
            # for i in range(54):
            #     keyboard.wait('enter')                  
            #     fileWriter(filename, str(i+1))              
            #     Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file   
            #     uart_Packager(response,port,hk = False,cmdInput= "1000A000000000")
            #     sleep(0.001)
            #     Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename) #Writing HK to file   
            load(0.0834)
            print("\n Now Finished Test Sequence \n")
                
            
        case "3":                   
            while(1):
                cmd[0] = "10"
                steps = cmd[1] = input(" --- Enter the amount of steps forward you want to move (Press ENTER to exit) ---")      
                print(cmd[1])  
                # hk= True
                # uart_Packager(response,port,hk,cmdInput="00000000000000" )    
                match steps:
                    case steps if (b'0001' <= bytes(steps, 'utf-8') <=b'FFFF'):
                            print("\n Moving Forward" , cmd[1], "steps")
                            cmd[2] = cmd[1][2:4]
                            cmd[1] = cmd[1][0:2]
                            print("\n",cmd[1],"\n",cmd[2])
                            hk=False
                            uart_Packager(response,port,hk,cmdInput="".join(cmd) )
                    case _:
                        print("Not Valid")
                        Sequences(port)
        case "4":                   
            while(1):
                cmd[0] = "11"
                steps = cmd[1] = input(" --- Enter the amount of steps forward you want to move (Press ENTER to exitt) ---")                   
                hk= True
                uart_Packager(response,port,hk,cmdInput="00000000000000" )         
                match steps:
                    case steps if (b'0001' <= bytes(steps, 'utf-8') <=b'FFFF'):
                            print("\n Moving Forward" , cmd[1], "steps")
                            cmd[2] = cmd[1][2:4]
                            cmd[1] = cmd[1][0:2]
                            print("\n",cmd[1],"\n",cmd[2])
                            hk=False
                            uart_Packager(response,port,hk,cmdInput="".join(cmd) )
                    case _:
                        print("Not Valid")
                        Sequences(port)

        case "5":
            filename = input("\n Please enter the Filename Prefix for the Video and Text Files\n")
            fileWriter(filename,"HK Data File for test : ")
            fileWriter(filename,filename)
            test_current = "1800"
            uart_Packager(response,port,hk = False,cmdInput= "".join("0A" + test_current + nominal_pwm_rate + nominal_speed + nominal_pwm_duty)) #Setting nominal motor drive parameters
            uart_Packager(response,port,hk = False,cmdInput= "0B7F0064380005") #Setting nominal motor guard parameters            
            uart_Packager(response,port,hk = False,cmdInput= "0C3200320000A0") #Setting Limits
            fileWriter(filename,"\n\n\nHK Packet before Movement : ")
            Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename)
            for i in range(10):
                print("\nAttempting to Move at Current = " + test_current)                
                print("".join("0A" + test_current + nominal_pwm_rate + nominal_speed + nominal_pwm_duty))
                uart_Packager(response,port,hk = False,cmdInput= "".join("0A" + test_current + nominal_pwm_rate + nominal_speed + nominal_pwm_duty)) #Setting nominal motor drive parameters
                uart_Packager(response,port,hk = False,cmdInput="10018000000000")
                uart_Packager(response,port,hk = True,cmdInput= "00000000000000")           
                progressbar_move(response,port,filename,i_Range = 5,speed = 0.5)
                motorMoved = input("\n Has the motor moved? Y/N")
                match motorMoved:
                    case "Y":
                        fileWriter(filename,"\nMotor has moved at " + test_current)
                        progressbar_move(response,port,filename,i_Range = 5,speed = 0.5)
                    case "N":                        
                        fileWriter(filename,"\nMotor stalled at " + test_current)                        
                        test_current = input("\n whats the next current step you would like?")
        case _:
            exit()