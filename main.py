import machine
from machine import I2C, Pin
import onewire
import ds18x20
import time
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 39
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

ts_pin = machine.Pin(28)
builtin_ts_pin = machine.ADC(4)

s = ds18x20.DS18X20(onewire.OneWire(ts_pin))
bts = builtin_ts_pin.read_u16() * (3.3 / 65535)

roms = s.scan()

while True:
    s.convert_temp()
    time.sleep_ms(750)
    
    lcd.clear()
    lcd.move_to(0,0)

    for rom in roms:
        
        T1 = "Temp1:" + str(s.read_temp(rom)) + " C"
        T2 = "Temp2:" + str(-1 * (27 - (bts - 0.706) / 0.001721)) + " C"
        T3 = "Temp2:" + str(27 - (bts - 0.706) / 0.001721) + " C"
        
        print("Temperature (Sensor):	", s.read_temp(rom), "°C")
        lcd.putstr(str(T1))
    if ((27 - (bts - 0.706) / 0.001721) < 0):
        print("Temperature (Built-in):	", -1 * (27 - (bts - 0.706) / 0.001721), "°C")
        lcd.move_to(0,1)
        lcd.putstr(str(T2))
    elif ((27 - (bts - 0.706) / 0.001721) >= 0):
        print("Temperature (Built-in):	", (27 - (bts - 0.706) / 0.001721), "°C")
        lcd.move_to(0,1)
        lcd.putstr(str(T3))

    time.sleep_ms(250)
