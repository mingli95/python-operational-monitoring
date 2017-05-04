# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing
import psutil,socket
class SystemInfo(object):
    def __init__(self):
        pass
    # 获取网卡名称和其ip地址，不包括回环(return 网卡名和ip地址)
    def get_netcard(self):
        netcard_info = []
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    netcard_info.append((k, item[1]))
        return netcard_info

    # 主机基本系统信息(系统版本-centos)
    def base_info(self):
        sys_info = {}
        f = open('/etc/redhat-release')
        sys_version = f.readlines()
        f.close()
        sys_info['system_model'] = sys_version[0]
        f = open('/proc/version')
        lines = f.readlines()
        f.close()
        line = lines[0].split()
        sys_info['kernel_version'] = 'kernel '+line[2]
        sys_info['hostname'] = socket.gethostname()
        return sys_info

    # cpu信息（读取/proc/cpuinfo，以每核为字典，返回列表。）
    def cpu_stat(self):
        cpu = []
        cpu_info={}
        cpuinfo = {}
        f = open("/proc/cpuinfo")
        lines = f.readlines()
        f.close()
        for line in lines:
            if line == '\n':
                cpu.append(cpuinfo)
                cpuinfo = {}
            if len(line) < 2: continue
            name = line.split(':')[0].rstrip()
            var = line.split(':')[1]
            cpuinfo[name] = var
        cpu_info['cpu_num']=len(cpu)
        cpu_info['cpu_model']=cpu[0]['model name']
        return cpu_info

    # 内存信息 / meminfo (return total,used,free)
    def memory_stat(self):
        mem = {}
        mem1 = {}
        f = open("/proc/meminfo")
        lines = f.readlines()
        f.close()
        for line in lines:
            if len(line) < 2: continue
            name = line.split(':')[0]
            var = line.split(':')[1].split()[0]
            mem[name] = long(var) / 1024
        mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
        mem1['MemTotal'] = str(mem['MemTotal'])+"M"
        mem1['MemUsed'] = str(mem['MemUsed'])+"M"
        mem1['MemFree'] = str(mem['MemFree'])+"M"
        return mem1
    # 负载信息 / loadavg (返回1，5，15分钟负载信息)
    def load_stat(self):
        loadavg = {}
        f = open("/proc/loadavg")
        con = f.read().split()
        f.close()
        loadavg['lavg_1'] = con[0]
        loadavg['lavg_5'] = con[1]
        loadavg['lavg_15'] = con[2]
        # loadavg['nr'] = con[3]
        # loadavg['last_pid'] = con[4]
        return loadavg
    # 运转时间 / Uptime (返回day,hour,minute,second)
    def uptime_stat(self):
        uptime = {}
        f = open("/proc/uptime")
        con = f.read().split()
        f.close()
        all_sec = float(con[0])
        MINUTE, HOUR, DAY = 60, 3600, 86400
        uptime['day'] = int(all_sec / DAY)
        uptime['hour'] = int((all_sec % DAY) / HOUR)
        uptime['minute'] = int((all_sec % HOUR) / MINUTE)
        uptime['second'] = int(all_sec % MINUTE)
        # uptime['Free rate'] = float(con[1]) / float(con[0])
        return uptime
    # 获取网卡流量信息 /proc/net/dev
    def net_stat(self):
        net = []
        f = open("/proc/net/dev")
        lines = f.readlines()
        f.close()
        for line in lines[2:]:
            con = line.split()
            intf = dict(
                zip(
                    ('interface', 'ReceiveBytes', 'ReceivePackets',
                     'ReceiveErrs', 'ReceiveDrop', 'ReceiveFifo',
                     'ReceiveFrames', 'ReceiveCompressed', 'ReceiveMulticast',
                     'TransmitBytes', 'TransmitPackets', 'TransmitErrs',
                     'TransmitDrop', 'TransmitFifo', 'TransmitFrames',
                     'TransmitCompressed', 'TransmitMulticast'),
                    (con[0].rstrip(":"), int(con[1]), int(con[2]),
                     int(con[3]), int(con[4]), int(con[5]),
                     int(con[6]), int(con[7]), int(con[8]),
                     int(con[9]), int(con[10]), int(con[11]),
                     int(con[12]), int(con[13]), int(con[14]),
                     int(con[15]), int(con[16]),)
                )
            )

            net.append(intf)
        return net
    # 磁盘空间使用
    def disk_stat(self):
        import os
        hd = {}
        disk = os.statvfs("/")
        hd['available'] = disk.f_bsize * disk.f_bavail/1024/1024/1024
        hd['capacity'] = disk.f_bsize * disk.f_blocks/1024/1024/1024
        hd['used'] = disk.f_bsize * disk.f_bfree/1024/1024/1024
        return hd

# if __name__ == '__main__':

def Insert_many():
    main = SystemInfo()
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
    return many
    # print main.net_stat()
    # print main.disk_stat()
