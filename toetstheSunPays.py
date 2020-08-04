#%%

# Toets basiese skryf na die seriepoort
import serial
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
ser.close()

#%%
from binascii import unhexlify

# Opdrag vanaf paragraaf 5 in seriepoort handleiding
bytestosend = '7E3235303034363432453030323031464433310D'

# Stuur data 1200 baud.  Dit moet eers teen hierdie spoed gestuur word
with serial.Serial('/dev/ttyUSB0', 9600, timeout=5.0) as ser:
    x = ser.write(unhexlify(bytestosend)) # Stuur opdrag na die battery
    uitstring = ser.read(5000)
    a = uitstring.hex()

# Druk die greepstring (bytestring)
print('Greepstring')
print(uitstring)
print('Hex string')
print(a)
# %%