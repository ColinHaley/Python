import ConfigParser
from mcstatus import MinecraftServer
import MySQLdb

config = ConfigParser.RawConfigParser()
config.read('Authentication/WhitelistMaint.cfg')

__rconport__ = int(config.get('WhitelistMaint', 'rconport'))
__sqldatabase__ = config.get('WhitelistMaint','database')
__sqltable__ = config.get('WhitelistMaint','table')
__sqlusername__ = config.get('WhitelistMaint','Username')
__sqlpassword__ = config.get('WhitelistMaint','Password')
__sqlserver__ = 'localhost'

try:
	server = MinecraftServer('asov.info',__rconport__)
except:
	raise ValueError('Could not connect to remote host.')

players = server.query().players.names

#Mark edit location

queryPlayers = '('

for x in range(0, len(players)):
	queryPlayers += "'" + players[x] + "',"

queryPlayers = queryPlayers[:-1] + ')'

sqlquery = "Update " + __sqltable__ + " SET LastLogin = NOW() WHERE Username in " + queryPlayers

db = MySQLdb.connect(__sqlserver__,__sqlusername__,__sqlpassword__,__sqldatabase__)

cursor = db.cursor()

result = cursor.execute(sqlquery)

if (result > 0):
	db.commit()
else:
	db.rollback()

# end edit location
# Purpose of Fork - Add individual updates 
# NOT FUNCTIONAL YET!

for x in range(0,len(#whitelistimport)):
	if(data[x]['name'] <> in(queryPlayers)):
		#INSERT QUERY!


for x in range(0, len(players)):



	updateQuery = """begin tran
	update table with (serializable) set
	Update {0} SET LastLogin = NOW() Where Username = {1}
	
	if @@rowcount = 0
	begin
		Insert Into Whitelist VALUES ('')		
	end
commit tran""".format(__sqltable__, player[x])