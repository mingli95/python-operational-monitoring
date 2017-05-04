# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing
from main import *
import socket,json

def Insert_one():
    main = SystemInfo()
    one={}
    # 网口名称，ip地址(2个 netname address 不变)
    Net_name = main.get_netcard()
    one['Netname'] = Net_name[0][0]
    one['Address'] = Net_name[0][1]
    # 主机名，内核版本，系统版本(三个 hostname kernel system 不变)
    Sys_version = main.base_info()
    one['Hostname'] = Sys_version['hostname']
    one['Kernel'] = Sys_version['kernel_version']
    one['System'] = Sys_version['system_model']
    # cpu信息 (二个 cpunum cpumodel 不变)
    Cpu_info = main.cpu_stat()
    one['Cpunum'] = Cpu_info['cpu_num']
    one['Cpumodel'] = Cpu_info['cpu_model']
    dic = {}
    # sql="INSERT INTO yunwei.systeminfo (netname,address,hostname,kernel,system,cpunum,cpumodel) VALUES ('%s','%s','%s','%s','%s','%s','%s');"%(Netname,Address,Hostname,Kernel,System,Cpunum,Cpumodel)
    dic['sql']="INSERT INTO yunwei.systeminfo (netname,address,hostname,kernel,system,cpunum,cpumodel) VALUES ('%s','%s','%s','%s','%s','%s','%s');"%(one['Netname'],one['Address'],one['Hostname'],one['Kernel'],one['System'],one['Cpunum'],one['Cpumodel'])
    dic['tablename']="systeminfo"
    dic['address'] = one['Address']
    dic = json.dumps(dic)
    return dic
def Insert_many():
    main = SystemInfo()
    tablename="hostinfo"
    many={}
    #  内存信息(三个 memtotal memused memfree 变)
    Mem_info=main.memory_stat()
    many['Memtotal']=Mem_info['MemTotal']
    many['Memused']=Mem_info['MemUsed']
    many['Memfree']=Mem_info['MemFree']
    # 系统负载信息 (三个 lavg1 lavg5 lavg15 变)
    Load_info=main.load_stat()
    many['Lavg1']=Load_info['lavg_1']
    many['Lavg5']=Load_info['lavg_5']
    many['Lavg15']=Load_info['lavg_15']
    # 系统从开机到现在运行时间(一个 uptime 变)
    Uptime_info=main.uptime_stat()
    if Uptime_info['day'] == 0:
        Uptime="%s:%s:%s"%(Uptime_info['hour'],Uptime_info['minute'],Uptime_info['second'])
    else:
        Uptime="%sday %s:%s:%s"%(Uptime_info['day'],Uptime_info['hour'],Uptime_info['minute'],Uptime_info['second'])
    many['Uptime']=Uptime
    dic = {}
    dic['tablename']=tablename
    dic['sql']="INSERT INTO yunwei.hostinfo (memtotal,memused,memfree,lavg1,lavg5,lavg15,uptime) VALUES "\
                 "('%s','%s','%s','%s','%s','%s','%s');"\
                %(many['Memtotal'],many['Memused'],many['Memfree'],many['Lavg1'],many['Lavg5'],many['Lavg15'],many['Uptime'])
    dic = json.dumps(dic)
    return dic
def Clisock(data):
    HOST = "127.0.0.1"
    PORT = 5000
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i=0
    while i<1:
        mySocket.sendto(data, (HOST, PORT))

        # step 3: receive packet back from server
        packet, address = mySocket.recvfrom(1024)
        print packet
        i+=1

    mySocket.close()

if __name__ == "__main__":
    list=[Insert_one(),Insert_many()]
    for i in list:
        Clisock(i)


