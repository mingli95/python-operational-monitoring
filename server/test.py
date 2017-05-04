# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

import db_connect
import init_sql

# sql = "select * from yunwei.systeminfo where address='192.168.1.191';"

# print len(db_connect.Db(sql).Select())
#

# print init_sql.init_table().systeminfo()

sql = init_sql.init_table().systeminfo()
db_connect.Db(sql).Create()