import pandas as pd # pip install pandas
from binascii import unhexlify
import datetime
from configparser import ConfigParser
import sqlalchemy #pip install sqlalchemy
import mysql.connector #pip installl mysql-connector
from sqlalchemy.types import VARCHAR, DATETIME
import schedule #pip install schedule 
import time
import serial

def readandwritetoDB():

    # Opdrag vanaf paragraaf 5 in seriepoort handleiding
    bytestosend = '7E3235303034363432453030324646464430360D'

    # Stuur data 9600 baud.  Dit moet eers teen hierdie spoed gestuur word
    with serial.Serial('/dev/ttyUSB1', 9600, timeout=5.0) as ser:
        x = ser.write(unhexlify(bytestosend)) # Stuur opdrag na die battery
        
        uitstring = ser.read(5000)
        uitstringhex = uitstring.hex()
    print(uitstringhex)
    #uitstringhex = "7e3235303134363030323038363030303130463044393530443942304432363044394330444130304439443044393230443135304442343044393730443942304441323044423030444130304441353036304236343042354430423633304236303042383230423743303030304342353332373130303332373130303030343237313030303030353542413030303042323941453041440d"

    # pip install sqlalchemy
    # pip install PyMySQL

    bytebreakdown=pd.read_csv("bytebreakdownTSPbat.csv")

    # Haal veranderlike uit die hex string en return decimal
    def haalveranderlikeuithex(uitstringhex,bytenommer,bytelengte):
        veranderlike=unhexlify(uitstringhex[(2*bytenommer)-2:(bytenommer*2)+(bytelengte*2)-2])
        return veranderlike

    for ind, row in bytebreakdown.iterrows():
        try:
            bytebreakdown.loc[ind,'result'] = int(haalveranderlikeuithex(uitstringhex,row['beginbyte'],row['bytelengte']).decode("utf-8"),16)
        except:
            bytebreakdown.loc[ind,'result'] = str(haalveranderlikeuithex(uitstringhex,row['beginbyte'],row['bytelengte']).decode("utf-8"))

    postdf=bytebreakdown.drop(['beginbyte','bytelengte'],axis =1)

    begintyd = str(datetime.datetime.now())

    #haal kolomname uit postdf
    y=postdf.columns[0]
    x=postdf.columns[1]

    datedf = pd.DataFrame({y:['datetime'],x:[begintyd]})
    klientID = pd.DataFrame({y:['klientid'],x:['12345678']})
    batteryID = pd.DataFrame({y:['batteryid'],x:['987654321']})

    aangepastedb=datedf.append(klientID, ignore_index=True).append(batteryID, ignore_index=True)
    
    finaltodb=aangepastedb.append(postdf,ignore_index=True).set_index(y).transpose()

    parser = ConfigParser()
    parser.read('config.ini')

    host = parser.get('db','db_host')
    port = int(parser.get('db','db_port'),10)
    name = parser.get('db','db_name')
    user = parser.get('db','db_user')
    password = parser.get('db','db_password')

    db_url='mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(user,password,host,port,name)

    engine = sqlalchemy.create_engine(db_url)

    begintyd = str(datetime.datetime.now())

    #haal kolomname uit postdf
    y=postdf.columns[0]
    x=postdf.columns[1]

    datedf = pd.DataFrame({y:['datetime'],x:[begintyd]})

    finaltodb.to_sql('Battery_Info', con=engine, if_exists='append', index=False)

schedule.every(10).seconds.do(readandwritetoDB)

while 1:
    schedule.run_pending()
    time.sleep(1)