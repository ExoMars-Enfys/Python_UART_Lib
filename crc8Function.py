import crc8
from binascii import unhexlify
def crc8Calculate(cmdInput) :
        cmdInput = unhexlify(cmdInput)
        hash = crc8.crc8()
        print(cmdInput, type(cmdInput))
        hash.update(cmdInput)
        crc8Frame = hash.digest()
        print("CRC is {} ({})".format(crc8Frame, type(crc8Frame)) )
        HashedInput = cmdInput + crc8Frame
        print(HashedInput)
        return HashedInput 