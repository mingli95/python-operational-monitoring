# -*- coding:utf-8 -*-
#Time:2017-4-27
#V1.0 单线程 同时只能处理一个客户端请求，后期改进。
#author:LiMing

import socket,json
import db_connect
HOST = "127.0.0.1"
PORT = 5000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mySocket.bind((HOST, PORT))
while 1:
    packet, address = mySocket.recvfrom(1024)
    packet1 = json.loads(packet)
    if packet1['tablename'] == "systeminfo":
        sql = "select * from yunwei.systeminfo where address='%s';"%(packet1['address'])
        if len(db_connect.Db(sql).Select()) == 0:
            db_connect.Db(packet1['sql']).Insert()
            mySocket.sendto(packet+" \n写入成功!", address)
            continue
        else:
            mySocket.sendto(packet+" \n已经存在无需写入!", address)
            continue
    if packet1['tablename'] == "hostinfo":
        db_connect.Db(packet1['sql']).Insert()
        mySocket.sendto(packet + " \n写入成功!", address)
        continue
    mySocket.sendto(packet, address)

mySocket.close()

