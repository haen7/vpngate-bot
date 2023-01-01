import os
#from urllib2 import urlopen
from urllib.request import urlopen
import re,base64,csv,io



vpndata=urlopen("http://www.vpngate.net/api/iphone").read().decode('utf-8')
print(type(vpndata))
vpndata=vpndata.replace("*","")
vpnfile=io.StringIO(vpndata)
with vpnfile as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    next(reader)
    next(reader)
    for row in reader:
        try:
            if int(row[2])>1100000 and int(row[2])<4000000 and int(row[7])>0 and int(row[3])<20 :
                filename=row[5]+"-"+row[1]+".ovpn"
                print(filename)
                print(type(filename))
                config=base64.b64decode(row[14])
                print(type(config))
                file_like=io.BytesIO(config)
                print(type(file_like))
                print(type(file_like.read()))
                print(file_like)
                #print(config)
        except Exception as e:
            break
        else:
            pass
        finally:
            pass