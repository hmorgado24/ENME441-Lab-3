#   To check address: sudo i2cdetect -y 1
import smbus

class PCF8591:

  bus = smbus.SMBus(1)

  def __init__(self, address):
    self.bus = smbus.SMBus(1)
    self.address = address
    self.chn = chn

  def read(self, chn): #channel
    try:
        self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
        self.bus.read_byte(self.address) # dummy read to start conversion
    except Exception as e:
        print ("Address: %s \n%s" % (self.address,e))
    return self.bus.read_byte(self.address)
    return self.bus.read_byte(self.chn)

class Joystick:

  def __init__(self, address, chn):
    self.adc = PCF8591(address, chn)
  
  def getX(self):
    return str(self.adc.read(chn))
  
  def getY(self):
    return str(self.adc.read(0x41))

while True:
  joystick = Joystick(0x48)
  print(joystick.getX() + ', ' + joystick.getY())