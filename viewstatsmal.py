import sqlite3
import datetime

urls = []

def convTstamp(ts):
    i_ts = int(ts)
    dt = datetime.datetime.fromtimestamp(i_ts/1000)
    s_dt = str(dt)
    return s_dt[0:10]

def urlAdd(url):
    urls.append(url)
    return url

def urlCount(url):
    furl = urls.count(url)
    return furl
conn = sqlite3.connect('webstats.db')
print ("Opened database successfully")

#June 2016 = 1464739200
#June TimeStamp 1464739200
#July TimeStamp 1467346925
#August TimeStamp 1470013200

pages = "SELECT DISTINCT PAGEURL from RAWSTATS WHERE CLIENTIP LIKE '80.248.208.131%'"

cursor = conn.execute( pages )
for row in cursor:
    print (row)
conn.close()