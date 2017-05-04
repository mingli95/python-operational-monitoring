# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing
import db_connect

class init_table:
    def __init__(self):
        pass
    def systeminfo(self):
        sql = """CREATE TABLE If Not Exists yunwei.systeminfo (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `netname` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `kernel` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `system` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cpunum` int(11) DEFAULT NULL,
  `cpumodel` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

        """
        return sql
    def hostinfo(self):
        sql="""
        CREATE TABLE if not EXISTS `yunwei`.`hostinfo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `memtotal` VARCHAR(45) NULL,
  `memused` VARCHAR(45) NULL,
  `memfree` VARCHAR(45) NULL,
  `lavg1` VARCHAR(45) NULL,
  `lavg5` VARCHAR(45) NULL,
  `lavg15` VARCHAR(45) NULL,
  `uptime` VARCHAR(45) NULL,
  `datetime` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));
        """
        return sql

if __name__ == "__main__":
    main=init_table()
    db_connect.Db(main.systeminfo()).Create()
    db_connect.Db(main.hostinfo()).Create()
