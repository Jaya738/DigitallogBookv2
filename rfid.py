#! /usr/bin/env python3
import serial
import time
import sys
import serial.tools.list_ports
# Python code to Insert RFID data into MongoDB 
from pymongo import MongoClient 
def scan():
    ports = list(serial.tools.list_ports.comports())
    flag=0
    
    for p in ports:
        q=str(p).split(" - ")
        a=q[1]
        print(a[:len(q)-2])
        if(str(a[:len(q[1])-1])=="ttyACM"):
            flag=1
            str1=q[0]
    if(flag==1):
        return str1
    else:
        return "RFID device not found"
if __name__=='__main__':
    str2=scan()
    print(str2)
    try:
        conn = MongoClient()
        print("Connected successfully!!!") 
    except:
        print("Could not connect to MongoDB") 
    db = conn.StudentLog
    collection = db.RFID_Data
    if(str2 != "RFID device not found"):
        ser = serial.Serial(str2, 9600, timeout=0)
        while 1:
            try:
                line = ser.readline().decode('utf-8')[:-1]
                if line:
                    print(line)
                    RFID_Data = {
                        "id":line
                        }
                    rec_id1 = collection.insert_one(RFID_Data)
                    print("Added Record to DB",rec_id1," ") 
                time.sleep(1)
            except ser.SerialTimeoutException:
                print('Data could not be read')
                time.sleep(1)
    else:
        print(str2)
  
