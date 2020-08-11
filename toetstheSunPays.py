#%%

# Toets basiese skryf na die seriepoort
import serial
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
ser.close()

#%% Definieer die nodige funksies

def twos_complement(hexstr,bits):
    # Verander die heksadesimale getal na 'n heelgetal met 'n teken oftewel 'n "signed integer"
    # In 'n n-greep twee komplement getallevoorstelling, het die grepe die waardes:
    # greep 0 = 2^0
    # bit 1 = 2^1
    # bit n-2 = -2^(n-2)
    # bit n-1 = -2n-1
    #
    # Maar greep n-1 het waarde 2^(n-1) wanneer dit geen teken het nie, dus is die getal 2^n te hoog.
    # Trek dus 2^n af indien greep n-1 'n waarde het

    value = int(hexstr,16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    
    return value

def uitsetGetalHeksString(insetstring):
    # Neem die insetstring van die battery ontvang en kry die ASCII waarde daarvan
    getalinheks = bytearray.fromhex(insetstring).decode()
    # getalinheks word nou omgeskakel na 'n desimale waarde wat gebruik kan word.
    uitsetgetal = int(getalinheks, 16)
    
    return uitsetgetal

def uitsetGetalHeksStringSignInt(insetstring):
    # Neem die insetstring van die battery ontvang en kry die ASCII waarde daarvan
    getalinheks = bytearray.fromhex(insetstring).decode()
    # getalinheks word nou omgeskakel na 'n desimale waarde wat gebruik kan word.
    uitsetgetal = twos_complement(getalinheks, 16)
    
    return uitsetgetal










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

print(a[246:254])
print(uitsetGetalHeksString(a[246:254]))

print(a[210:218])
print(uitsetGetalHeksStringSignInt(a[210:218]))