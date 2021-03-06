#   To check address: sudo i2cdetect -y 1
import smbus
import time

class PCF8591:

  bus = smbus.SMBus(1)

  def __init__(self, address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self, chn): #channel
    try:
        self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
        self.bus.read_byte(self.address) # dummy read to start conversion
    except Exception as e:
        print ("Address: %s \n%s" % (self.address,e))
    return self.bus.read_byte(self.address)

class Joystick:

  def __init__(self, address):
    self.adc = PCF8591(address)
  
  def getX(self):
    return str(self.adc.read(0x40))
  
  def getY(self):
    return str(self.adc.read(0x41))

while True:
  joystick = Joystick(0x48)
  print(joystick.getX() + ', ' + joystick.getY())
  time.sleep(.1)