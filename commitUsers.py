import json
import MySQLdb

#Author: Kazra

__SERVER__ = 'localhost'
__USERNAME__ = 'user'
__PASSWORD__ = 'password'
__DATABASE__ = 'database'
__WHITELIST__ = '/path/to/whitelist.json'

jsonData = open(__WHITELIST__).read()
data = json.loads(jsonData)

db = MySQLdb.connect(__SERVER__,__USERNAME__,__PASSWORD__,__DATABASE__)
cursor = db.cursor()

for x in range(0, totalItem):
    try:
        #Modify for your table structure, initial commit for asov: User, UUID, Approver, Approve Date, Last Login, Exempt from epiry.
        cursor.execute("INSERT INTO Users VALUES ('{0}','{1}','SYSTEM',NOW(),NOW(),0)".format(data[x]['name'],data[x]['uuid']))
        db.commit()
    except:
        db.rollback()
