# Battery4_8kW
Seriepoort kommunikasie vir die 4.8kWh litium ioon (LiFePO4) van theSunPays battery om die SOC te monitor.



## RS-232 formaat van seriepoort van battery

Hier is die ASCII tabel.  Die battery stuur en ontvang data in Heksadesimale getalle, maar dit gebruik die heksadesimale waarde van die ASCII tabel.

![asciifull](asciifull.gif)

Voorbeeld uit paragraaf 5 van RS-232 handleiding van die battery:

Stuur volgende string HEX getalle na die battery:

`7E 32 30 30 31 34 36 34 32 45 30 30 32 30 31 46 44 33 35 0D`
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

`7e3235303134363030323038363030303130463044393830443938304431463044394330444134304441313044393630443132304442413044393830443942304441333044423230444135304441413036304235413042353530423531304235353042363330423631303030304342363932373130303332373130303030343237313030303030353434443030303041464131453039390d`


`7E 32 30 30 31 34 36 30 30 43 30 36 45 31 31 30 31 30
46 30 44 34 35 30 44 34 34 30 44 34 35 30 44 34 34 30 44 34 35 30 44 34
34 30 44 33 45 30 44 34 35 30 44 34 41 30 44 34 41 30 44 34 42 30 44 34
41 30 44 34 41 30 44 34 41 30 44 34 41 30 35 30 42 43 33 30 42 43 33 30
42 43 33 30 42 43 44 30 42 43 44 30 30 30 30 43 37 32 35 42 46 36 38 30
32 43 33 35 30 30 30 30 32 45 35 35 33 0D`

Die oorblywende energie in die battery word gegee deur:

`42 46 36 38`

in die string wat teruggestuur word hierbo.  Die volledige analise van die string hierbo word gegee in die Pylontech RS232 handleiding in paragraaf 5.

Die getalle hierbo is die heksadesimale waardes van die ASCII tabel.  Dus is `42`eintlik die string `B.`  Net so is die hele string dan:  `BF68`

Hierdie string is 'n heksadesimale getal wat nou teruggelei kan word na 'n desimale getal.  `BF68H` waar `H`  die heksadesimale getal beteken, is `49000`.  Hierdie getal is die waarde in mAh van die battery.  Dus om die orige energie in kWh te bereken word die volgende berekening gedoen:

$Energie = \frac{49000mAh}{1000} \times 48V = 2352W = 2.352kW$

Hierdie berekening neem aan dit is 'n 48V battery.

Dus is die lading persentasie (die "State of Charge" of SOC) gelyk aan:

$SOC = \frac{2.352W}{2400W} = 0.98 = 98\%$

Hierdie berekening neem aan dit is 'n 2.4kWh battery oftewel die Pylontech US2000.



### 