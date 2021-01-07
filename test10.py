from __future__ import print_function

import hid
import time

# enumerate USB devices

for d in hid.enumerate():
    keys = list(d.keys())
    keys.sort()
    for key in keys:
        print("%s : %s" % (key, d[key]))
    print()

# try opening a device, then perform write and read

try:
    print("Opening the device")

    h = hid.device()


    def I2C_Cancel():
        buf = [0x00, 0x10]
        buf = buf + [0 for i in range(65 - len(buf))]
        buf[2 + 1] = 0x10  # Cancel current I2C/SMBus transfer (sub-command)
        h.write(buf)
        h.read(65)

    h.open(0x04d8,0x00dd)  

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    #h.set_nonblocking(1)

    # write some data to the device
    print("RESET the CHIP")

    strku = "00 70 AB CD EF  00 00 00 00"
    print(strku)
    h.write(bytearray.fromhex(strku))
    time.sleep(2)

    h.close()


    print("Open Device Again !")


    h = hid.device()
    h.open(0x04d8,0x00dd) 

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    #h.set_nonblocking(1)




    def I2C_Init(speed=100000):  # speed = 100000
        #self.MCP2221_I2C_SLEEP = float(os.environ.get("MCP2221_I2C_SLEEP", 0))
        #buf = self.compile_packet([0x00, 0x10])
        buf = [0x00, 0x10]
        buf = buf + [0 for i in range(65 - len(buf))]
        buf[2 + 1] = 0x00  # Cancel current I2C/SMBus transfer (sub-command)
        buf[3 + 1] = 0x20  # Set I2C/SMBus communication speed (sub-command)
        # The I2C/SMBus system clock divider that will be used to establish the communication speed
        buf[4 + 1] = int((12000000 / speed) - 3)
        h.write(buf)
        rbuf = h.read(65)
        # print("Init")
        if (rbuf[22] == 0):
            raise RuntimeError("SCL is low.")
        if (rbuf[23] == 0):
            raise RuntimeError("SDA is low.")

    I2C_Init()


    # write some data to the device
    print("I2C device WAKE UP !!!")

    strku = "00 90 05 00 C0 00 00 00 00"
    print(strku)
    h.write(bytearray.fromhex(strku))
    #time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)

    time.sleep(0.50)

    I2C_Cancel()
    #I2C_Init()

    time.sleep(0.50)
    #setelah wake, harus di I2C_Cancel


    #get config , perhatikan I2C slave address adalah 60 + 1 = 61 (odd)
    strku = "00 91 FF 00 C1"
    print(strku)
    h.write(bytearray.fromhex(strku))

    #time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))

    time.sleep(0.05)
    strku = "00 40 00 00 00"

    print(strku)
    h.write(bytearray.fromhex(strku))
    # wait
    #time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        #print(' '.join(hex(x) for x in d))
        print(' '.join(['%02x' % b for b in d]))





    time.sleep(0.50)

    I2C_Cancel()
    I2C_Init()

    time.sleep(0.50)

    print("COMMAND (more than 64 bytes result)  !!!")


    strku = "00 90 08 00 C0 03 07 40 04 02 00 85 07"

    print(strku)
    h.write(bytearray.fromhex(strku))


    # wait
    #time.sleep(0.05)

    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))


    time.sleep(0.50)

    I2C_Cancel()

    time.sleep(0.05)


    strku = "00 91 3c 00 C1"

    print(strku)
    h.write(bytearray.fromhex(strku))
    # wait
    #time.sleep(0.05)
    # read back the answer
    print("Read the result data, first 60 bytes")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))
    time.sleep(0.05)
    strku = "00 40 00 00 00"
    print(strku)
    h.write(bytearray.fromhex(strku))
    # read back the answer
    print("Read the data")
    d = h.read(128)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))


    time.sleep(0.05)


    strku = "00 91 3c 00 C1"

    print(strku)
    h.write(bytearray.fromhex(strku))
    # wait
    #time.sleep(0.05)
    # read back the answer
    print("Read the result data, second 60 bytes ")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))
    time.sleep(0.05)
    strku = "00 40 00 00 00"
    print(strku)
    h.write(bytearray.fromhex(strku))
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))


    time.sleep(0.50)

    I2C_Cancel()
    I2C_Init()

    time.sleep(0.50)



    print("WAKE UP !!!")

    strku = "00 90 05 00 C0 00 00 00 00"

    print(strku)
    h.write(bytearray.fromhex(strku))
    #time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)

    time.sleep(0.50)

    I2C_Cancel()
    #I2C_Init()

    time.sleep(0.50)

    #get config , perhatikan I2C slave address adalah 60 + 1 = 61 (odd)
    #time.sleep(0.05)
    strku = "00 91 FF 00 C1"
    print(strku)
    h.write(bytearray.fromhex(strku))

    #time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))


    time.sleep(0.05)
    strku = "00 40 00 00 00"
    
    print(strku)
    h.write(bytearray.fromhex(strku))
    # wait
    #time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        #print(' '.join(hex(x) for x in d))
        print(' '.join(['%02x' % b for b in d]))





    # wait
    time.sleep(0.50)

    I2C_Cancel()
    I2C_Init()

    time.sleep(0.50)



    print(" ")
    print(" ")
    print("Multiple Write")
    print("First Chunk, data length tetap 0x48")

    strku  = "00 90 48 00 C0 0347162300002b7e151628aed2a6abf7158809cf4f3c6be163d42b623e70d164fa145db1d4637058710b58e1e665d3d2f5b465176403114443fa8e96"
    #strku  = "00 90 48 00 C0 0347162300002b7e151628aed2a6abf7158809cf4f3c6be163d42b623e70d164fa145db1d4637058710b58e1e665d3d2f5b465176403114443fa8e9614845ec7296cd13bc9dc6452"

    print(strku)
    h.write(bytearray.fromhex(strku))
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))

    #perhatikan time.sleep. perlu, namun sangat singkat
    time.sleep(0.01)

    print("Second Chunk  sisa nya ")

    
    strku  = "00 90 0c 00 C0 14845ec7296cd13bc9dc6452"


    print(strku)
    h.write(bytearray.fromhex(strku))
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))



    time.sleep(0.05)

    I2C_Cancel()
    #I2C_Init()


    #time.sleep(0.50)


    strku = "00 91 3c 00 C1"

    print(strku)
    h.write(bytearray.fromhex(strku))
    # wait
    time.sleep(0.05)
    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))


    time.sleep(0.50)
    strku = "00 40 00 00 00"
    print(strku)
    h.write(bytearray.fromhex(strku))

    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))


    time.sleep(0.50)
    strku = "00 40 00 00 00"
    print(strku)
    h.write(bytearray.fromhex(strku))

    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))



    time.sleep(0.50)

    I2C_Cancel()

    time.sleep(0.05)





    print(" ")
    print(" ")
    print(" ")




    time.sleep(0.50)

    I2C_Cancel()

    time.sleep(0.50)


    strku = "00 91 01 00 ED F9"
    print(strku)
    h.write(bytearray.fromhex(strku))


    # wait
    #time.sleep(0.05)

    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))

    time.sleep(0.05)
    strku = "00 40 00 00 00"

    print(strku)
    h.write(bytearray.fromhex(strku))


    # wait
    #time.sleep(0.05)

    # read back the answer
    print("Read the data")
    d = h.read(65)
    if d:
        #print(d)
        print(' '.join(['%02x' % b for b in d]))





    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")
