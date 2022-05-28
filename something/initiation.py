# init

from board import SCL, SDA
import busio

from adafruit_pca9685 import  PCA9685

i2c_bus = busio.I2C(SCL,SDA)

pca = PCA9685(i2c_bus)
pca.frequency = 60

pca.channels[3].duty_cycle = 0x7FFF