import usb.core
import usb.util
import numpy
import sys

def xorShifted(left, right, shift):
    if(shift >= 0):
        return (numpy.uint32(left) ^ numpy.uint32(right)) >> numpy.uint32(shift)
    return (numpy.uint32(left) ^ numpy.uint32(right)) << numpy.uint32(-shift)

def genKey():
    key = (xorShifted(did[0], 0x4210005, 5) | xorShifted(did[0], 0x4210005, -0x1b))
    key = key ^ (xorShifted(did[1], 0x30041523, 3) | xorShifted(did[1], 0x30041523, -0x1d))
    key = key ^ (xorShifted(did[2], 0x6517bebe, 0xc) | xorShifted(did[2], 0x6517bebe, -0x14))
    for i in range (0, 100):
        key = key >> numpy.uint32(1) | (key ^ key >> numpy.uint32(0x1f) ^ (key & numpy.uint32(0x200000)) >> numpy.uint32(0x15) ^ (key & numpy.uint32(2)) >> numpy.uint32(1) ^ key & numpy.uint32(1)) << numpy.uint32(0x1f)
    
    return(key)


dev = usb.core.find(idVendor=0x046d, idProduct=0x1234)
if dev is None:
    print("No Joey Detected")
if dev is not None:
    print("Joey Connected\n")
    dev.set_configuration()
    dev.write(1,[0x80])  
    USBbuffer = dev.read(129,64)
    A=(USBbuffer[0])+ (USBbuffer[1]<<8) + (USBbuffer[2]<<16) + (USBbuffer[3]<<24)
    B=(USBbuffer[4]) + (USBbuffer[5]<<8) + (USBbuffer[6]<<16) + (USBbuffer[7]<<24)
    C=(USBbuffer[8]) + (USBbuffer[9]<<8)+(USBbuffer[10]<<16) + (USBbuffer[11]<<24)
    did = numpy.uint32(((A,B,C)))
    print("Device IDs:")
    print("Device ID: 1 =", hex(did[0]), "\nDevice ID: 2 =", hex(did[1]), "\nDevice ID: 3 =", hex(did[2]))
    print("Update Key: ", hex(genKey())[2:])
    input("Press enter to continue")
