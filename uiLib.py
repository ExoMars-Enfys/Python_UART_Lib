#-----Initialise Variables -----#
import os
def UI(output):
    cmd = ["00"] *7
    cmd[0] = input("\nEnter the Command ID\n" 
                + "\nAvailable Options: " 
                + "\n 1.  00 Request Housekeeping"
                + "\n 2.  01 Clear Errors"
                + "\n 3.  04 Power Controls"
                + "\n 4.  05 Heater Controls"
                + "\n 5.  06 Set Mechanism SP"
                + "\n 6.  07 Set Detector SP"
                + "\n 7.  0A Set Motor Drive Parameters"
                + "\n 8.  0B Set Motor Drive Guards"
                + "\n 9.  0C Set Motor Monitor Limits"
                + "\n 10. 10 Move Motor Forwards"
                + "\n 11. 11 Move Motor Backwards"
                + "\n 12. 12 Move Motor to Absolute Position"
                + "\n 13. 13 Drive Motor to Chosen End Switch"
                + "\n 14. 1C Configure UART Baudrate"
                + "\n 15. 1F Request Science Reading\n")
    match cmd[0]:
        case "00" :
            print("\n No further parameters required. Now Requesting Housekeeping from Artix 7")
            output = b'\x00\x00\x00\x00\x00\x00\x00'
            os.system('cls')
        case "01" :
            print("\n No further parameters required. Now Clearing all Errors on Artix 7")
            output = b'\x01\x00\x00\x00\x00\x00\x00'
            os.system('cls')
        case "04":
            os.system('cls')
            cmd[1] = input("\n Enter the Power Control Bit Mask\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Power on Mechanism Board"
                            + "\n 2. 01 Power on Detector Board\n")
            match cmd[1]:
                case "00":
                    print("\n Power on of Mechanism Board selected")
                    output = b'\x04\x00\x00\x00\x00\x00\x00'
                case "01":
                    print("\n Power on of Detector Board selected")
                    output = b'\x04\x01\x00\x00\x00\x00\x00'
                case _:
                    print("\n Not a valid input, please Try Again")
                    UI(output)
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
                    output = b'\x05\x00\x00\x00\x00\x00\x00'
                case "01":
                    print("\n Mechanism Board Heaters set to MANUAL")
                    output = b'\x05\x01\x00\x00\x00\x00\x00'
                case "02":
                    print("\n Detector Board Heaters set to AUTO")                    
                    output = b'\x05\x02\x00\x00\x00\x00\x00'
                case "03":
                    print("\n Detector Board Heaters set to MANUAL")                    
                    output = b'\x05\x03\x00\x00\x00\x00\x00'
                case "04":
                    print("\n All Heaters set to DISABLED during Science Readings")
                    output = b'\x05\x04\x00\x00\x00\x00\x00'
                case _:
                    print("\n Not a valid input, please Try Again")
                    UI(output)
        case "0A":
            os.system("cls")
            cmd[2] = input("\n Enter Maximum Current\n" 
                + "\n Available Options Are:"
                + "\n 1. 6000 Set Max Current to 56.2mA "
                + "\n 2. 8000 Set Max Current to 74.9mA"
                + "\n 1. A000 Set Max Current to 93.7mA \n ")
            match cmd[2]:
                case "6000":
                    print("\n Set Max Current to 93.7mA")
                    cmd[4] = input("\n Enter the PWM Rate\n" 
                                        + "\n Available Options Are:"                            
                                        + "\n 1. 0006 Set PWM Rate to 35.9μs "
                                        + "\n 2. 000B Set PWM Rate to 61.44μs "
                                        + "\n 3. 000C Set PWM Rate to 66.56μs \n")
                    match cmd[4]:
                        case "0006":
                            print("\n Set PWM Rate to 35.9μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x06\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x06\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x06\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x06\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x06\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x06\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case "000B":
                            print("\n Set PWM Rate to 61.44μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x0B\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x0B\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x0B\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x0B\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x0B\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x0B\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case "000C":
                            print("\n Set PWM Rate to 66.56μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x0C\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x0C\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x0C\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x0C\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x60\x00\x00\x0C\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x60\x00\x00\x0C\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)  
                case "8000":
                    print("\n Set Max Current to 93.7mA")
                    cmd[4] = input("\n Enter the PWM Rate\n" 
                                        + "\n Available Options Are:"                            
                                        + "\n 1. 0006 Set PWM Rate to 35.9μs "
                                        + "\n 2. 000B Set PWM Rate to 61.44μs "
                                        + "\n 3. 000C Set PWM Rate to 66.56μs \n")
                    match cmd[4]:
                        case "0006":
                            print("\n Set PWM Rate to 35.9μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x06\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x06\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x06\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x06\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x06\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x06\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case "000B":
                            print("\n Set PWM Rate to 61.44μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x0B\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x0B\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x0B\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x0B\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x0B\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x0B\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case "000C":
                            print("\n Set PWM Rate to 66.56μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x0C\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x0C\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x0C\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x0C\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\x80\x00\x00\x0C\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\x80\x00\x00\x0C\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)  
                case "A000":
                    print("\n Set Max Current to 93.7mA")
                    cmd[4] = input("\n Enter the PWM Rate\n" 
                                        + "\n Available Options Are:"                            
                                        + "\n 1. 0006 Set PWM Rate to 35.9μs "
                                        + "\n 2. 000B Set PWM Rate to 61.44μs "
                                        + "\n 3. 000C Set PWM Rate to 66.56μs \n")
                    match cmd[4]:
                        case "0006":
                            print("\n Set PWM Rate to 35.9μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x06\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x06\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x06\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x06\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x06\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x06\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case "000B":
                            print("\n Set PWM Rate to 61.44μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x0B\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x0B\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x0B\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x0B\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x0B\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x0B\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case "000C":
                            print("\n Set PWM Rate to 66.56μs")
                            cmd[5] = input("\n Enter the Motor Speed\n" 
                                                + "\n Available Options Are:"                            
                                                + "\n 1. 04 Set Speed to 04 "
                                                + "\n 2. 0A Set Speed to 0A "
                                                + "\n 3. 0F Set Speed to 0F \n")
                            match cmd[5]:
                                case "04":
                                    print("\nSet Speed to 04")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x0C\x04\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x0C\x04\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0A":
                                    print("\nSet Speed to 0A")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x0C\x0A\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x0C\x0A\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case "0F":
                                    print("\nSet Speed to 0F")
                                    cmd[6] = input("\n Enter the PWM Duty\n" 
                                    + "\n Available Options Are:"                            
                                    + "\n 1. 34 Set PWM Duty to 20% "
                                    + "\n 2. 7F Set PWM Duty to 50% ")
                                    match cmd[6]:
                                        case "34":
                                            print("\n Set PWM Duty to 20%")
                                            output = b'\x0A\xA0\x00\x00\x0C\x0F\x34'
                                        case "7F":
                                            print("\n Set PWM Duty to 50%")
                                            output = b'\x0A\xA0\x00\x00\x0C\x0F\x7F'
                                        case _:
                                            print("\n Not a valid input, please Try Again")
                                            UI(output)
                                case _:
                                    print("\n Not a valid input, please Try Again")
                                    UI(output)        
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)  
                case _:
                    print("\n Not a valid input, please Try Again")
                    UI(output)
        case "10":
            os.system('cls')
            cmd[1] = input("\n Enter the Steps MSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Set MSB to 00 "
                            + "\n 2. 08 Set MSB to 08 "
                            + "\n 3. 0F Set MSB to 0F \n")
            match cmd[1]:
                case "00":
                    print("\n Set Motor MSB to 00")

                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 88 Set LSB to 88 "
                            + "\n 2. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "88":
                            print("\n Set Motor LSB to 00")
                            output = b'\x10\x00\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor LSB to 08")
                            output = b'\x10\x00\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "08":
                    print("\n Set Motor MSB to 08")
                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set LSB to 00 "
                            + "\n 2. 88 Set LSB to 88 "
                            + "\n 3. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set Motor LSB to 00")
                            output = b'\x10\x08\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set Motor LSB to 88")
                            output = b'\x10\x08\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor LSB to FF")
                            output = b'\x10\x08\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "0F":
                    print("\n Set Motor MSB to 0F")
                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set LSB to 00 "
                            + "\n 2. 88 Set LSB to 88 "
                            + "\n 3. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set Motor LSB to 00")
                            output = b'\x10\x0F\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set Motor LSB to 88")
                            output = b'\x10\x0F\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor LSB to FF")
                            output = b'\x10\x0F\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case _:
                        print("\n Not a valid input, please Try Again")
                        UI(output)        
        case "11":
            os.system('cls')
            cmd[1] = input("\n Enter the Steps MSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Set MSB to 00 "
                            + "\n 2. 08 Set MSB to 08 "
                            + "\n 3. 0F Set MSB to 0F \n")
            match cmd[1]:
                case "00":
                    print("\n Set Motor MSB to 00")

                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 88 Set LSB to 88 "
                            + "\n 2. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "88":
                            print("\n Set Motor LSB to 00")
                            output = b'\x11\x00\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor LSB to 08")
                            output = b'\x11\x00\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "08":
                    print("\n Set Motor MSB to 08")
                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set LSB to 00 "
                            + "\n 2. 88 Set LSB to 88 "
                            + "\n 3. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set Motor LSB to 00")
                            output = b'\x11\x08\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set Motor LSB to 88")
                            output = b'\x11\x08\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor LSB to FF")
                            output = b'\x11\x08\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "0F":
                    print("\n Set Motor MSB to 0F")
                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set LSB to 00 "
                            + "\n 2. 88 Set LSB to 88 "
                            + "\n 3. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set Motor LSB to 00")
                            output = b'\x11\x0F\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set Motor LSB to 88")
                            output = b'\x11\x0F\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor LSB to FF")
                            output = b'\x11\x0F\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)        
        case "12":
            os.system('cls')
            cmd[1] = input("\n Enter the Absolute Position MSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Set MSB to 00 "
                            + "\n 2. 08 Set MSB to 08 "
                            + "\n 3. 0F Set MSB to 0F \n")
            match cmd[1]:
                case "00":
                    print("\n Set Motor Absolute Position MSB to 00")

                    cmd[2] = input("\n Enter the Absolute Position LSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 88 Set LSB to 88 "
                            + "\n 2. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "88":
                            print("\n Set Motor Absolute Position LSB to 00")
                            output = b'\x12\x00\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor Absolute Position LSB to 08")
                            output = b'\x12\x00\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "01":
                    print("\n Set Motor Absolute Position MSB to 08")
                    cmd[2] = input("\n Enter the Absolute Position LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set LSB to 00 "
                            + "\n 2. 88 Set LSB to 88 "
                            + "\n 3. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set Motor Absolute Position LSB to 00")
                            output = b'\x12\x08\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set Motor Absolute Position LSB to 88")
                            output = b'\x12\x08\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor Absolute Position LSB to FF")
                            output = b'\x12\x08\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "02":
                    print("\n Set Motor Absolute Position MSB to 0F")
                    cmd[2] = input("\n Enter the Absolute Position LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set LSB to 00 "
                            + "\n 2. 88 Set LSB to 88 "
                            + "\n 3. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set Motor Absolute Position LSB to 00")
                            output = b'\x12\x0F\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set Motor Absolute Position LSB to 88")
                            output = b'\x12\x0F\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set Motor Absolute PositionLSB to FF")
                            output = b'\x12\x0F\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)        
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
                            output = b'\x13\x00\x00\x00\x00\x00\x00'
                        case "01":
                            print("\n Move to Inner End stop")
                            output = b'\x13\x01\x00\x00\x00\x00\x00'
                        case "02":
                            print("\n Move to Parked Position")                    
                            output = b'\x13\x02\x00\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
        case "1C":
                    os.system('cls')
                    cmd[1] = input("\nSelect UART BaudRate\n" 
                                    + "\n Available Options Are:"
                                    + "\n 1. 00 9600 Bauds "
                                    + "\n 2. 01 57600 Bauds"
                                    + "\n 3. 02 115200 Bauds\n")
                    match cmd[1]:
                        case "00":
                            print("\n 9600 Bauds ")
                            output = b'\x1C\x00\x00\x00\x00\x00\x00'
                        case "01":
                            print("\n 57600 Bauds")
                            output = b'\x1C\x01\x00\x00\x00\x00\x00'
                        case "02":
                            print("\n 115200 Bauds")                    
                            output = b'\x1C\x02\x00\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
        case "1F":
            os.system('cls')
            cmd[1] = input("\n Enter the Number of samples per packet\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Set Number of samples to 00 "
                            + "\n 2. 08 Set Number of samples to 08 "
                            + "\n 3. 0F Set Number of samples to 0F \n")
            match cmd[1]:
                case "00":
                    print("\n Set Number of samples to 00")

                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 88 Set LSB to 88 "
                            + "\n 2. FF Set LSB to FF \n")
                    match cmd[2]:
                        case "88":
                            print("\n Set delay to 88")
                            output = b'\x10\x00\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set delay to FF")
                            output = b'\x10\x00\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "01":
                    print("\n Set Number of samples  to 08")
                    cmd[2] = input("\n Enter the Steps LSB\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set delay to 00 "
                            + "\n 2. 88 Set delay to 88 "
                            + "\n 3. FF Set delay to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set delay to 00")
                            output = b'\x10\x08\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set delay to 88")
                            output = b'\x10\x08\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set delay to FF")
                            output = b'\x10\x08\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
                case "02":
                    print("\n Set Number of samples  to 0F")
                    cmd[2] = input("\n Enter the delay between samples\n" 
                            + "\n Available Options Are:"                            
                            + "\n 1. 00 Set delay to 00 "
                            + "\n 2. 88 Set delay to 88 "
                            + "\n 3. FF Set delay to FF \n")
                    match cmd[2]:
                        case "00":
                            print("\n Set delay to 00")
                            output = b'\x10\x0F\x00\x00\x00\x00\x00'
                        case "88":
                            print("\n Set delay to 88")
                            output = b'\x10\x0F\x88\x00\x00\x00\x00'
                        case "FF":
                            print("\n Set delay to FF")
                            output = b'\x10\x0F\xFF\x00\x00\x00\x00'
                        case _:
                            print("\n Not a valid input, please Try Again")
                            UI(output)
        case _:
                    print("\n Not a valid input, please Try Again")
                    UI(output)
    return output

# while 1:
#     output = b''
#     UI(output)     
#     exit
