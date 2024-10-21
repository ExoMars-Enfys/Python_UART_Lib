
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
        , "\n |       02      | Last  Error              |", HK_Reading[2].hex()
        , "\n |       03      | Power Status             |", HK_Reading[3].hex()
        , "\n |       04      | Motor Error              |", HK_Reading[8].hex()
        , "\n |     05--06    | Motor Absolute Steps     |", HK_Reading[9].hex(), HK_Reading[10].hex()
        , "\n |     07--08    | Motor Relative Steps     |", HK_Reading[11].hex(), HK_Reading[12].hex()
        , "\n |       09      | Motor Status Flags       |", HK_Reading[13].hex()
        , "\n |     10--11    | Motor Guard Time         |", HK_Reading[14].hex(), HK_Reading[15].hex()
        , "\n |       12      | Motor PWM Duty Cycle     |", HK_Reading[16].hex()
        , "\n |     13--14    | Motor PWM Rate           |", HK_Reading[17].hex(), HK_Reading[18].hex()
        , "\n |       15      | Motor RecVal             |", HK_Reading[19].hex()
        , "\n |     16--17    | Motor SPIspSel           |", HK_Reading[20].hex(), HK_Reading[21].hex()
        , "\n |     18--19    | Motor Current            |", HK_Reading[22].hex(), HK_Reading[23].hex()
        , "\n |       21      | Motor Speed              |", HK_Reading[24].hex()
        , "\n |       22      | Motor Error Mask         |", HK_Reading[25].hex()
        , "\n |       23      | Motor Recirc             |", HK_Reading[26].hex()
        , "\n --------------------------------------------------------\n")
    return

def Housekeeping_stream(response,filename):
    HK_Reading = ["00"] *(int(len(response)/2)+1)
    for i in range(0, int(len(response)/2)+1): 
        HK_Reading[i] = response[i:i+1]
    with open(filename + ".txt",'a') as file:     
            file.write("\n" + str(HK_Reading) + "  ---  " + datetime.now().strftime("%d-%m-%Y, %H:%M:%S.%f") + "\n")
    return