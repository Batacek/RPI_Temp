import machine
import onewire
import ds18x20
import time

ts_pin = machine.Pin(28)
builtin_ts_pin = machine.ADC(4)

s = ds18x20.DS18X20(onewire.OneWire(ts_pin))
bts = builtin_ts_pin.read_u16() * (3.3 / 65535)

roms = s.scan()

while True:
    s.convert_temp()
    time.sleep_ms(750)

    for rom in roms:
        print("Temperature (Sensor):	", s.read_temp(rom), "°C")
    print("Temperature (Built-in):	", (27 - (bts - 0.706) / 0.001721), "°C")


    time.sleep_ms(250)
