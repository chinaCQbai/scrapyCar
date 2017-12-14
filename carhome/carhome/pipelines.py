# -*- coding: utf-8 -*-

import MySQLdb
import redis

dbuser = ''
dbpass = ''
dbname = 'cardb'
dbhost = ''
dbport = '3306'


class CarListPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO carlist(soures,url,urlname) 
            VALUES ('易车',%s,%s)
            """, (item['url'], item['name'])
                                )
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CarInfoListPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO carInfolist(soures,sourelink,url,urlname) 
            VALUES ('易车',%s,%s,%s)
            """, (item['sourelink'],item['url'], item['name'])
                                )
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class testPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO test(testurl,testname) 
            VALUES (%s,%s)
            """, (item['url'], item['name'])
                                )
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class RedisPipeline(object):
    def __init__(self):
        self.redis=redis.Redis(host=dbhost,port=6379,db=0)

    def process_item(self, item, spider):
        self.redis.lpush('carInfoLink',item['url'])
        return item

class CarhomePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO BitautoCar(
            carid,url,treeurl,brand,brandurl,brandmodel4,brandmodel5,version,image,cyear,ctype,color,
            price1,price2,displacement,shiftgears,shifttype,clength,cwidth,cheight,wheelbase,
            mingrounddistance,motor,intaketype,maxhorsepower,maxpower,maxrpm,oiltype,oilsupply,
            tankvolume,drivetype,braketype,frontwheel,backwheel) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,( item['carid'],item['url'],item['treeurl'],item['brand'],item['brandurl'],
                   item['brandmodel4'],item['brandmodel5'],item['version'],item['image'],item['cyear'],
                   item['ctype'],item['color'],item['price1'],item['price2'],item['displacement'],
                   item['shiftgears'],item['shifttype'],item['clength'],item['cwidth'],item['cheight'],
                   item['wheelbase'],item['mingrounddistance'],item['motor'],item['intaketype'],
                   item['maxhorsepower'],item['maxpower'],item['maxrpm'],item['oiltype'],item['oilsupply'],
                   item['tankvolume'],item['drivetype'],item['braketype'],item['frontwheel'],item['backwheel']
                                 )
                                )

            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item
