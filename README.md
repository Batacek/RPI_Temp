# RPI Temperature
Temperature measurement with RPI and temperature sensor using OneWire communication

# Physical Connection
The initial step is to connect the temperature sensor, which uses OneWire communication, to your RPI Pico.
<br>
<br>
<img src="temp.jpg" height=159 width=252> <img src="rpi_right.jpg" height=159 width=252>
<br>
<br>
Black is for GND<br>
Red is for VCC (5V)<br>
Yellow is for OW Communication (Pin 28)<br>
A resistor with a value of 6.04 KOhm is used to connect VCC and OW.<br>
<br>
The colors of the wires on the temperature sensor should be identical. Each wire should be connected to a corresponding wire of the same color (black to black, etc.). If a different temperature sensor is being used, the provided documentation should be read to ascertain the correct wiring procedure.
