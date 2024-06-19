def Housekeeping_Parser(response):
    HK_Reading = ["00"] *(int(len(response)/2)+1)
    for i in range(0, int(len(response)/2)+1): 
        HK_Reading[i] = response[i:i+1]
        # print(HK_Reading[i].hex(), i,"\n""\n")
    # print(response.hex(), type(response))
    # print(HK_Reading)
    print("\n  Housekeeping Readings: " 
        , "\n --------------------------------------------------------"
        , "\n | Byte Position | Contents Description     | Value |"
        , "\n --------------------------------------------------------"
        , "\n |       00      | Command ID and Model ID  |", HK_Reading[0].hex()
        , "\n |       01      | Command Count            |", HK_Reading[1].hex()
        , "\n |       02      | Last Error               |", HK_Reading[2].hex()
        , "\n |       03      | Motor Error              |", HK_Reading[3].hex()
        , "\n |     04--05    | Motor Absolute Steps     |", HK_Reading[4].hex(), HK_Reading[5].hex()
        , "\n |     06--07    | Motor Relative Steps     |", HK_Reading[6].hex(), HK_Reading[7].hex()
        , "\n |       08      | Motor Status Flags       |", HK_Reading[8].hex()
        , "\n |     09--10    | Motor Guard Time         |", HK_Reading[9].hex(), HK_Reading[10].hex()
        , "\n |       11      | Motor PWM Duty Cycle     |", HK_Reading[11].hex()
        , "\n |     12--13    | Motor PWM Rate           |", HK_Reading[12].hex(), HK_Reading[13].hex()
        , "\n |       14      | Motor RecVal             |", HK_Reading[14].hex()
        , "\n |     15--16    | Motor SPIspSel           |", HK_Reading[15].hex(), HK_Reading[16].hex()
        , "\n |     17--18    | Motor Current            |", HK_Reading[17].hex(), HK_Reading[18].hex()
        , "\n |       19      | Motor  Speed             |", HK_Reading[19].hex()
        , "\n |       20      | Motor Error Mask         |", HK_Reading[20].hex()
        , "\n --------------------------------------------------------\n")
    return
    
# while(1):
#     Housekeeping_Parser(response = "07010060000000006500000000000000000000f0b0b1b2b3b40fff0fff0fff0fff0fff0fff0fff0fffa3")
#     exit()
