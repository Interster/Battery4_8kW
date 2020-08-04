# Battery4_8kW
Seriepoort kommunikasie vir die 4.8kWh litium ioon (LiFePO4) van theSunPays battery om die SOC te monitor.



## RS-232 formaat van seriepoort van battery

Hier is die ASCII tabel.  Die battery stuur en ontvang data in Heksadesimale getalle, maar dit gebruik die heksadesimale waarde van die ASCII tabel.

![asciifull](asciifull.gif)

Voorbeeld uit paragraaf 5 van RS-232 handleiding van die battery:

Stuur volgende string HEX getalle na die battery:

`7E 32 35 30 30 34 36 34 32 45 30 30 32 30 31 46 44 33 31 0D`

Dit beteken
`7E` - begin van data

`32 35` - 25 (oftewel weergawe 2.5) in ASCII dit is die weergawe (VER)

`30 30` - 30 is 'n 0 in ASCII in heks, dus 00.  Dit is die nommer van die batterypak.  In hierdie geval is dit adres 0 oftewel batterypak 0.

`34 36` - 34 is 'n 4 in ASCII in heks en 36 is 'n 6 in heks in ASCII, dus 46 en dit is die kode vir litium ioon batterye (CID1)

`34 32` - 42 dit is die kode vir analoog inligting vanaf battery (CID2)

`45 30 30 32` - LENGTH dit is die lengte van die data wat met 'n komplekse berekening bereken word

`30 31` - INFO Dit is die ASCII vir 01 wat beteken jy vra vir battery 1 se inligting.  In die opdrag stuur geval is dit 'n sekondêre opdrag

`46 44 33 31` - CHECKSUM  Dit is die toets som vir hierdie string data

`0D` - dit is die einde van die data oftewel "Carriage return"

Kry dan terug:

`7E ` (SOI)

`32 35 ` (VER, Weergawe 25H oftewel V2.5)

`30 31` (ADR, Battery pak adres 01)

`34 36 ` (CID1, 46H, Litium battery)

`30 30 ` (RTN, 00H)

`32 30 38 36 ` (Lengte van antwoord)

`30 30 ` (DATAINFO)

`30 31 ` (Batterypak nommer 01H)

`30 46 ` (Aantal batteryselle M, 0FH in heksadesimaal, oftewel 16 Battery selle)

`30 44 39 38 `  Battery sel millivolts 1, 0D98H of 3480 millivolts

`30 44 39 38 `  Battery sel millivolts 2

`30 44 31 46 `  Battery sel millivolts 3

`30 44 39 43 ` Battery sel millivolts 4

`30 44 41 34 ` Battery sel millivolts 5

`30 44 41 31 ` Battery sel millivolts 6

`30 44 39 36 ` Battery sel millivolts 7

`30 44 31 32 ` Battery sel millivolts 8

`30 44 42 41 ` Battery sel millivolts 9

`30 44 39 38 ` Battery sel millivolts 10

`30 44 39 42 ` Battery sel millivolts 11

`30 44 41 33 ` Battery sel millivolts 12

`30 44 42 32 ` Battery sel millivolts 13

`30 44 41 35 ` Battery sel millivolts 14

`30 44 41 41 ` Battery sel millivolts 15

`30 36 30 42 ` Battery sel millivolts 16

`35 41 ` 

`30 42 35 35 ` Temperatuur 1 0B55H, = 29.01 grade Celcius 

`30 42 35 31 `

`30 42 35 35 `

`30 42 36 33 `

`30 42 36 31 `

`30 30 30 30 ` Batterypak Stroom 0000H = 0 x 10milliAmpere = 0 mA.

`43 42 36 39 ` Batterypak totale Volts (spanning) = CB69H, 52073 mV of 52.073V

`32 37 31 30 ` Oorblywende kapasiteit 2710H = 100.00Ah

`30 33 ` Sogenaamde "user defined number P", 03H

`32 37 31 30` Battery pak volle kapasiteit 2710H, oftewel 100.00Ah

` 30 30 30 34` Aantal ontladingsiklusse, 0004H, oftewel 4 siklusse

` 32 37 31 30` Batterypak ontwerpskapasiteit, 2710H, oftewel 100.00Ah  

` 30 30 30 30` 

`35 34 34 44 ` 

`30 30 30 30 ` 

`41 46 41 31 ` 

`45 30 39 39 ` CHKSUM

`0D` EOI End of Information (Einde van inligting)





Die oorblywende energie in die battery word gegee deur:

`32 37 31 30 `  Oorblywende kapasiteit 2710H = 100.00Ah

in die string wat teruggestuur word hierbo.  Die volledige analise van die string hierbo word gegee in die battery handleiding in paragraaf 5.  Die analise hierbo is gedoen vanaf 'n meting op 4 Aug 2020.

Die getalle hierbo is die heksadesimale waardes van die ASCII tabel.  Dus is `32`eintlik die string `2.`  Net so is die hele string dan:  `2710`

Hierdie string is 'n heksadesimale getal wat nou teruggelei kan word na 'n desimale getal.  `2710H` waar `H`  die heksadesimale getal beteken, is `10000`.  Hierdie getal is die waarde in Ah x 100 van die battery.  Dus om die orige energie in kWh te bereken word die volgende berekening gedoen:

Onthou dat die volle battery (hierdie was twee 4.8kWh batterye in parallel) 'n 100Ah kapasiteit het.
$$
SOC = \frac{100Ah}{100Ah} = 1 = 100\%
$$
Die battery was dus vol.