import os
def UI(output):
    nominal_current = "61A8"
    nominal_pwm_rate = "0006"
    nominal_speed = "08"
    nominal_pwm_duty = "FF"
    nominal_recirc = "7F"
    nominal_guardtime = "0064"
    nominal_recval = "38"
    nominal_spi = "0005"


    cmd = ["00"] *7
    startupcmd = ""
    exit_flag = ""
    startupcmd = input("\n Please choose the type of run you would like to carry out"
                       +"\n Available options are: "
                       +"\n 1. Run Free-Will Commands"
                       +"\n 2. Run Testbench Sequences"
                       +"\n 0. Exit Program\n")
    match startupcmd :
        case "1" :
            cmd[0] = input("\nEnter the Command ID\n" 
                + "\nAvailable Options: " 
                + "\n --------------------------------------------------------"
                + "\n | CMD ID | Command Description                   |"
                + "\n --------------------------------------------------------"
                + "\n |   N    | Initialise Nominal Motor Drive Values |"
                + "\n |   G    | Initialise Nominal Guard Values       |"
                + "\n |   00   |  Request Housekeeping                 |"
                + "\n |   01   |  Clear Errors                         |"
                + "\n |   04   |  Power Controls                       |"
                + "\n |   05   |  Heater Controls                      |"
                + "\n |   06   |  Set Mechanism SP                     |"
                + "\n |   07   |  Set Detector SP                      |"
                + "\n |   0A   |  Set Motor Drive Parameters           |"
                + "\n |   0B   |  Set Motor Drive Guards               |"
                + "\n |   0C   |  Set Motor Monitor Limits             |"
                + "\n |   10   |  Move Motor Forwards                  |"
                + "\n |   11   |  Move Motor Backwards                 |"
                + "\n |   12   |  Move Motor to Absolute Position      |"
                + "\n |   13   |  Drive Motor to Chosen End Switch     |"
                + "\n |   15   |  Halt all Motor Movement              |"
                + "\n |   1F   |  Request Science Reading              |"
                + "\n --------------------------------------------------------\n")
            match cmd[0]:
                case "N"  :
                    print("\n Now writing Nominal Motor Drive parameters as: "
                    + "\n     Current : " + nominal_current
                    + "\n     Pwm Rate : " + nominal_pwm_rate
                    + "\n     Current : " + nominal_speed
                    + "\n     Current : " + nominal_pwm_duty)
                    output = "".join("0A" + nominal_current + nominal_pwm_rate + nominal_speed + nominal_pwm_duty)
                case "G"  :
                    print("\n Now writing Nominal Guard parameters as: "
                    + "\n     Recirculation : " + nominal_recirc
                    + "\n     GuardTime : " + nominal_guardtime
                    + "\n     RecVal : " + nominal_recval
                    + "\n     Spi Speed : " + nominal_spi)
                    output = "".join("0B" + nominal_recirc + nominal_guardtime + nominal_recval + nominal_spi)
                case "00" :
                    print("\n No further parameters required. Now Requesting Housekeeping from Artix 7")
                    output = "".join(cmd) 
                    
                case "01" :
                    print("\n No further parameters required. Now Clearing all Errors on Artix 7")
                    output = "".join(cmd) 

                case "04":
                    os.system('cls')
                    cmd[1] = input("\n Enter the Power Control Bit Mask\n" 
                                    + "\n Available Options Are:"
                                    + "\n 1. 00 Power on Mechanism Board"
                                    + "\n 2. 01 Power on Detector Board\n")
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
                    print("\n Now writing Motor Drive parameters as: "
                    + "\n     Current : " + nominal_current
                    + "\n     Pwm Rate : " + nominal_pwm_rate
                    + "\n     Current : " + nominal_speed
                    + "\n     Current : " + nominal_pwm_duty)                                
                    output = "".join(cmd)                 
                  
                case "0B":
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
                    print("\n Now writing Guard parameters as: "
                    + "\n     Recirculation : " + cmd[1]
                    + "\n     GuardTime : " + cmd[2]
                    + "\n     RecVal : " + cmd[4]
                    + "\n     Spi Speed : " + cmd[5])                                    
                    output = "".join(cmd)        

                case "10":
                        os.system('cls')
                        cmd[1] = input("\n Enter the Steps in the form XXXX\n" 
                                        + "\n Available Range is: 0001 - 20EF\n")
                        extract = cmd[1]
                        match extract:                
                            case extract if b'0001' <= bytes(extract, 'utf-8') <=b'20EF':
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
                            case extract if b'0001' <= bytes(extract, 'utf-8') <=b'20EF':
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
                            cmd[1] = input("\nSelect which End stop to move to\n" 
                                            + "\n Available Options Are:"
                                            + "\n 1. 00 Move to Outer End stop "
                                            + "\n 2. 01 Move to Inner End stop"
                                            + "\n 3. 02 Move to Parked Position\n")
                            match cmd[1]:
                                case "00":
                                    print("\n Move to Outer End stop ")
                                case "01":
                                    print("\n Move to Inner End stop")
                                case "02":
                                    print("\n Move to Parked Position")
                                case _:
                                    print("\n Not a valid input, please Try Again\n")
                            output = "".join(cmd)    
                case "15" :
                    print("\n -------- MOTOR HALTED! -------- \n")
                    cmd[1] = "00"
                    cmd[6] = "00"
                    output = "".join(cmd)

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

        case "2":
            print("Do things here")
        case "0" :
            exit_flag = input("\n Are you sure you want to exit? Y/N")
            match exit_flag:
                case"Y":
                    print("~~~Goodbye~~~")
                    exit()
                case"N":
                    UI(output)
        case _:
            print("\n Not a valid input, please Try Again\n")
    return (output)