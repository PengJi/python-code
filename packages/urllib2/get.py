# -*- coding: utf-8 -*-
import base64
import urllib2
import hmac
import hashlib
import datetime

apiurl = "http://10.22.38.62:8000/api/get_db_pwd?user=table_stat_user&db_name=table_stat"
uri = '/api/get_db_pwd'
gmtTime = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
string2Sign = "GET %s\n%s" % (uri, gmtTime)
secretId = "blade_dsn"
secretKey = "BSCHn3Jxv8limD3efKLwdewYyan8t3Bk"
signature = base64.encodestring(hmac.new(secretKey, string2Sign, hashlib.sha1).digest()).replace("\n", "")

headers={
    "Date": gmtTime,
    "Authorization": "MWS" + " " + secretId + ":" + signature,
}

request = urllib2.Request(apiurl, headers=headers)
response = urllib2.urlopen(request)
print response.read()