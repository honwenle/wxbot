import http.client
import hashlib
import urllib
import random

def trans(q, fromLang = 'en', toLang = 'zh'):
    appid = '20170918000083557'
    secretKey = 'W6gYqWj_CPQ9KiXSwxl0'
    
    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        response = httpClient.getresponse()
        res = response.read()
        res = eval(res.decode())
        return res
    except Exception:
        print(Exception)
    finally:
        if httpClient:
            httpClient.close()
