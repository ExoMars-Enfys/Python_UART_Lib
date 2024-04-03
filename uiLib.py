#-----Initialise Variables -----#
def UI():
    cmdID = "00"
    cmdParam1 = "00"
    cmdParam2 = "00"
    cmdParam3 = "00"
    cmdParam4 = "00"
    cmdParam5 = "00"
    cmdParam6 = "00"
    cmdID = input("\nEnter the Command ID\n" 
                + "\nPossible Options: " 
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
    match cmdID:
        case "00" :
            print("\n No further parameters required. Now Requesting Housekeeping from Artix 7")
        case "01" :
            print("\n No further parameters required. Now Clearing all Errors on Artix 7")
        case "04":
            cmdParam1 = input("\n Enter the Power Control Bit Mask\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Power on Mechanism Board"
                            + "\n 2. 01 Power on Detector Board\n")
            match cmdParam1:
                case "00":
                    print("\n Power on of Mechanism Board selected")
                case "01":
                    print("\n Power on of Detector Board selected")
                case _:
                    print("\n Not a valid input, please Try Again")
                    UI()
        case "05":
            cmdParam1 = input("\n Enter the Heater Control Bit Mask\n" 
                            + "\n Available Options Are:"
                            + "\n 1. 00 Toggle Mechanism Board Heaters to *AUTO* "
                            + "\n 2. 01 Toggle Mechanism Board Heaters to *MANUAL* "
                            + "\n 3. 02 Toggle Detector Board Heaters to *AUTO* "
                            + "\n 4. 03 Toggle Detector Board Heaters to *MANUAL* "
                            + "\n 5. 04 Toggle All Board Heaters to *DISABLED* when doing a Science Reading\n")
            match cmdParam1:
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
                    print("\n Not a valid input, please Try Again")
                    UI()
        case "10":
            cmdParam1 = input("\n Enter the Steps MSB\n" 
                            + "\n Available Range is 00 - 0F:\n")
            match cmdParam1:
                case cmdParam1 if b'00' <= bytes(cmdParam1,'utf-8') <= b'0F' :
                    print("\nSelected : " , cmdParam1, " for Steps MSB")
                case _:
                    print("\nInvalid Range Please Try Again\n")
                    UI()

            cmdParam2 = input("\n Enter the Steps LSB\n" 
                            + "\n Available Range is 00 - FF:\n")
            match cmdParam2:
                case cmdParam2 if b'00' <= bytes(cmdParam2,'utf-8') <= b'FF' :
                    print("\nSelected : " , cmdParam2, " for Steps LSB")
                case _:
                    print("\nInvalid Range Please Try Again\n")
                    UI()

    cmdInput = cmdID + cmdParam1 + cmdParam2 + cmdParam3 + cmdParam4 + cmdParam5 + cmdParam6
    cmdInput = bytes(cmdInput,'utf-8')
    return(cmdInput)