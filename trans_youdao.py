import http.client
import hashlib
import urllib
import random

appid = '35521a68930f2c2b'
secretKey = 'XHHhDaOY4pC7rkw7SRnX1lSI4JaxEEcI'

 
httpClient = None
myurl = '/api'
q = 'apple'
fromLang = 'EN'
toLang = 'zh_CHS'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = hashlib.md5(sign.encode(encoding='utf-8'))
sign = m1.hexdigest()
myurl = myurl+'?appKey='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = http.client.HTTPConnection('openapi.youdao.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print(response.read())
except Exception:
    print(Exception)
finally:
    if httpClient:
        httpClient.close()
