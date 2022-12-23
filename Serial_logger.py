import logging
import logging.config
import threading
import time

import paho.mqtt.client as mqtt
import colorama
import serial
from colorama import Back, Fore, Style

logging.config.fileConfig('./logging.conf')
logger = logging.getLogger()

topic="AM/atom6"
def serwrite():
    pass
    # while 1:
    #     a=input()
    #     b=a+"\r\n"
    #     if  a=="now":
    #         b="\x1a"
    #     ser.write(b.encode('utf-8'))
        
def serread():
    while True:
        try: 
            lis=ports()
            ser = serial.Serial(
            port=lis[0],
            baudrate = 115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)
            client.connect(mqtt_ip, mqtt_port, 60)
            ser.write(b"AT\r\n")
            
            data=ser.readline()
            while True:
                x=ser.readline()
                bb=x.decode('utf-8')
                # if bb.startswith('['):
                if bb !="" and bb !="\r\n" :
                    # print(Fore.GREEN +"Received data from MC_Module: "+ bb + Style.RESET_ALL)
                    logger.info(bb)
                    #+QGNSSRD: $GNRMC,114319.000,A,1257.78865,N,08015.19073,E,1.04,78.34,221222,,,A,V*3E\
                    if len(bb) >79 and "$GNRMC," in bb:
                        Splitted_data =bb.split(",")
                        kph=(float(Splitted_data[7]) )*1.852
                        Msg='{{"Time":{},"Date":{},"Speed":{}}}'.format(Splitted_data[1],Splitted_data[9],str(kph))
                        client.publish(topic, Msg, qos=2)
        except Exception as e:
            logger.error("Error is {}".format(str(e)))
            time.sleep(1)       
def ports():
    lis=[]
    for vtr in range(0,12):
        tryPort='/dev/ttyUSB' +str(vtr)
        logger.info(tryPort)
        try:
            s = serial.Serial(port=tryPort, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
            logger.info ("++ found serial on {}".format( tryPort))
            bol=True
            lis.append(tryPort)
        except:
            logger.info ("-- no serial on {}".format( tryPort))
    return lis

if __name__=="__main__":
    mqtt_ip="broker.hivemq.com"
    mqtt_port=1883
    client = mqtt.Client()
    colorama.init()
    # t1=threading.Thread(target=serwrite)
    t2=threading.Thread(target=serread)
    # t1.start()
    t2.start()
    # t1.join()
    # t2.join()
            


