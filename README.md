# Battery4_8kW
Seriepoort kommunikasie vir die 4.8kWh litium ioon (LiFePO4) van theSunPays battery om die SOC te monitor.



## RS-232 formaat van seriepoort van battery

Hier is die ASCII tabel.  Die battery stuur en ontvang data in Heksadesimale getalle, maar dit gebruik die heksadesimale waarde van die ASCII tabel.

![asciifull](asciifull.gif)

### Voorbeeld 1

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

`7E ` (SOI) [0:2]

`32 35 ` (VER, Weergawe 25H oftewel V2.5) [2:6]

`30 31` (ADR, Battery pak adres 01) [6:10]

`34 36 ` (CID1, 46H, Litium battery) [10:14]

`30 30 ` (RTN, 00H) [14:18]

`32 30 38 36 ` (Lengte van antwoord) [18:26]

`30 30 ` (DATAINFO) [26:30]

`30 31 ` (Batterypak nommer 01H) [30:34]

`30 46 ` (Aantal batteryselle M, 0FH in heksadesimaal, oftewel 15 Battery selle) [34:38]

`30 44 39 38 `  Battery sel millivolts 1, 0D98H of 3480 millivolts [38:46]

`30 44 39 38 `  Battery sel millivolts 2 [46:54]

`30 44 31 46 `  Battery sel millivolts 3 [54:62]

`30 44 39 43 ` Battery sel millivolts 4 [62:70]

`30 44 41 34 ` Battery sel millivolts 5 [70:78]

`30 44 41 31 ` Battery sel millivolts 6 [78:86]

`30 44 39 36 ` Battery sel millivolts 7 [86:94]

`30 44 31 32 ` Battery sel millivolts 8 [94:102]

`30 44 42 41 ` Battery sel millivolts 9 [102:110]

`30 44 39 38 ` Battery sel millivolts 10 [110:118]

`30 44 39 42 ` Battery sel millivolts 11 [118:126]

`30 44 41 33 ` Battery sel millivolts 12 [126:134]

`30 44 42 32 ` Battery sel millivolts 13 [134:142]

`30 44 41 35 ` Battery sel millivolts 14 [142:150]

`30 44 41 41 ` Battery sel millivolts 15 [150:158]

`30 36` Aantal termperatuur metings oftewel 6 metings [158:162]

`30 42 35 41 ` Temperatuur 1 [162:170]

`30 42 35 35 ` Temperatuur 2 0B55H, = 29.01 grade Celcius [170:178]

`30 42 35 31 ` [178:186]

`30 42 35 35 ` [186:194]

`30 42 36 33 ` [194:202]

`30 42 36 31 ` [202:210]

`30 30 30 30 ` Batterypak Stroom 0000H = 0 x 10milliAmpere = 0 mA. [210:218]

`43 42 36 39 ` Batterypak totale Volts (spanning) = CB69H, 52073 mV of 52.073V [218:226]

`32 37 31 30 ` Oorblywende kapasiteit 2710H = 100.00Ah [226:234]

`30 33 ` Sogenaamde "user defined number P", 03H [234:238]

`32 37 31 30` Battery pak volle kapasiteit 2710H, oftewel 100.00Ah [238:246]

`30 30 30 34` Aantal ontladingsiklusse, 0004H, oftewel 4 siklusse [246:254]

`32 37 31 30` Batterypak ontwerpskapasiteit, 2710H, oftewel 100.00Ah [254:262] 

`30 30 30 30` 

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


### Voorbeeld 2

Vra vir die laaste battery:

Met FF:

`7E3235303034363432453030324646464430360D`

7e3235303134363030323038363030303130463044323830443242304431303044324130443241304432373044323730443042304432413044323830443241304432413044324230443241304432383036304235383042353330423444304235313042354430423545303030304335333332373130303332373130303030343237313030303030353434443030303041464131453045390d


### Voorbeeld 3
