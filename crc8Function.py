def crc8Calculate(cmdInput) :
        hash = crc8.crc8()
        print(cmdInput, type(cmdInput))
        hash.update(cmdInput)
        crc8Frame = hash.digest()
        print("CRC is {} ({})".format(crc8Frame, type(crc8Frame)) )
        return crc8Frame 