
from binascii import unhexlify
from datetime import datetime

def Housekeeping_Parser(response):
    HK_Reading = ["00"] *(int(len(response)/2)+1)
    for i in range(0, int(len(response)/2)+1): 
        HK_Reading[i] = response[i:i+1]
        
    print("\n  Housekeeping Readings: " 
        , "\n --------------------------------------------------------"
        , "\n | Byte Position | Contents Description     | Value |"
        , "\n --------------------------------------------------------"
        , "\n |       00      | Command ID and Model ID  |", HK_Reading[0].hex()
        , "\n |       01      | Command Count            |", HK_Reading[1].hex()
        , "\n |       02      | Last Error               |", HK_Reading[2].hex()
        , "\n |       03      | Motor Error              |", HK_Reading[9].hex()
        , "\n |     04--05    | Motor Absolute Steps     |", HK_Reading[10].hex(), HK_Reading[11].hex()
        , "\n |     06--07    | Motor Relative Steps     |", HK_Reading[12].hex(), HK_Reading[13].hex()
        , "\n |       08      | Motor Status Flags       |", HK_Reading[14].hex()
        , "\n |     09--10    | Motor Guard Time         |", HK_Reading[15].hex(), HK_Reading[16].hex()
        , "\n |       11      | Motor PWM Duty Cycle     |", HK_Reading[17].hex()
        , "\n |     12--13    | Motor PWM Rate           |", HK_Reading[18].hex(), HK_Reading[19].hex()
        , "\n |       14      | Motor RecVal             |", HK_Reading[20].hex()
        , "\n |     15--16    | Motor SPIspSel           |", HK_Reading[21].hex(), HK_Reading[22].hex()
        , "\n |     17--18    | Motor Current            |", HK_Reading[23].hex(), HK_Reading[24].hex()
        , "\n |       19      | Motor  Speed             |", HK_Reading[25].hex()
        , "\n |       20      | Motor Error Mask         |", HK_Reading[26].hex()
        , "\n --------------------------------------------------------\n")
    return

def Housekeeping_stream(response,filename):
    HK_Reading = ["00"] *(int(len(response)/2)+1)
    for i in range(0, int(len(response)/2)+1): 
        HK_Reading[i] = response[i:i+1]
    with open(filename + ".txt",'a') as file:     
            file.write("\n" + str(HK_Reading) + "  ---  " + datetime.now().strftime("%d-%m-%Y, %H:%M:%S.%f") + "\n")
    return