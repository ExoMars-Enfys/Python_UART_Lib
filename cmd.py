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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
            case _:
                print("\n Not a valid input, please Try Again")
                UI()  
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
            case _:
                print("\n Not a valid input, please Try Again")
                UI()  
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
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
                                UI()
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
                                UI()
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
                                UI()
                    case _:
                        print("\n Not a valid input, please Try Again")
                        UI()        
            case _:
                print("\n Not a valid input, please Try Again")
                UI()  
    case _:
        print("\n Not a valid input, please Try Again")
        UI()
