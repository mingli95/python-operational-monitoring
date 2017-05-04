# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing
import MySQLdb
class Db(object):
    def __init__(self,sql):
        self.sql = sql
        self.db = MySQLdb.connect("192.168.1.180", "liming", "asdasd123", "yunwei")
        self.cursor = self.db.cursor()
    def Insert(self):
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.cursor.close()
        self.db.close()

    def Select(self):
        self.cursor.execute(self.sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return results

    def Update(self):
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.cursor.close()
        self.db.close()
    def Create(self):
        self.cursor.execute(self.sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()

# if __name__ == "__main__":
#     data="INSERT INTO yunwei.systeminfo (netname,address,hostname,kernel,system,cpunum,cpumodel) VALUES ('eno16777728','192.168.1.190','localhost.localdomain','kernel 3.10.0-229.el7.x86_64','CentOS Linux release 7.1.1503 (Core) \n','4',' Intel(R) Core(TM) i3-3240 CPU @ 3.40GHz\n');"
#     Db(data).Insert()