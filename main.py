import machine
import onewire
import ds18x20
import time

ds_pin = machine.Pin(28)

ow = onewire.OneWire(ds_pin)
ds = ds18x20.DS18X20(ow)

roms = ds.scan()

while True:
    ds.convert_temp()
    time.sleep_ms(750)

    for rom in roms:
        print("Temperature:", ds.read_temp(rom), "°C")

    time.sleep(1)

