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

def wysHeksString(insetstring):
    print('Heksadesimale ASCII waarde')
    print(insetstring)
    print('Heksadesimale string')
    getalinheks = bytearray.fromhex(insetstring).decode()
    print(getalinheks)
    print('Desimale string')
    print(int(getalinheks, 16))
    
    return 0

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


def skryfLogLynBattery(leesvanbattery):
    a = leesvanbattery
    
    #Stroom in milliAmpere/100.  Dus vermenigvuldig met 100 en deel deur 1000 om Ampere te kry
    stroom = uitsetGetalHeksStringSignInt(a[210:218])
    #Spanning in milliVolt van hele battery
    spanning = uitsetGetalHeksString(a[218:226])
    #Oorblywende energie in battery
    energieOor = uitsetGetalHeksString(a[226:234])
    # Totale energie in battery
    energietotaal = uitsetGetalHeksString(a[238:246])
    # Siklusse
    siklusse = uitsetGetalHeksString(a[246:254])
        
    uitsetloglyn = str(stroom) + ',' + str(spanning) + ',' + str(energieOor) + ',' + str(energietotaal) + ',' + str(siklusse)
    
    return uitsetloglyn


import datetime
import time
from binascii import unhexlify
import serial

# Log parameters
monsterfrekwensie = 30 # [sekondes]
totalesekondes = 24*60*60 # [sekondes]

# Opdrag vanaf paragraaf 5 in seriepoort handleiding:  Lees analoog data
bytestosend = '7E3235303034363432453030323031464433310D'

begintyd = datetime.datetime.now()

# Maak leer oop
leer = open('SunPays_' + str(datetime.date.today()) + '.log', 'w')
leer.write('DatumTyd, Stroom mA_100, Spanning mV, Energie oor mAh, Totale energie mAh, Siklusse\n')

while (datetime.datetime.now() - begintyd).seconds < totalesekondes:
    # Stuur data 9600 baud.  Dit moet eers teen hierdie spoed gestuur word
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=5.0) as ser:
        x = ser.write(unhexlify(bytestosend)) # Stuur opdrag na die battery
        uitstring = ser.read(5000)
        a = uitstring.hex()
        print(a)
    
    print(str(datetime.datetime.now()) + ' Log lesing')

    # Log data na leer
    leer.write(str(datetime.datetime.now()) + ',' + skryfLogLynBattery(a))
    leer.write('\n')
    time.sleep(monsterfrekwensie - 5)

leer.close()
