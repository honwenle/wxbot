#coding=utf-8

from urllib import request
import re

def downloadPage(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = request.Request(url = url, headers = headers)
    h = request.urlopen(req)
    return h.read()

def downloadImg(content):
    pattern = r'src="(.+?\.jpg)'
    m = re.compile(pattern)
    content = content.decode('utf-8')
    urls = re.findall(m, content)

    for i, url in enumerate(urls):
        print(url)
        try:
            request.urlretrieve('http://www.quanjing.com/'+url, "pics/%s.jpg" % (i, ))
        except Exception:
            print(Exception)

content = downloadPage("http://www.quanjing.com/?audience=151316")
downloadImg(content)

'''
# Note
urllib2是py2才有的，在py3里变成了urllib.request
py3得到的html是需要解码的，一般是utf-8
有些网站不允许爬虫，也许会返回HTTP 502，可以先初始化一个带header的request.Request伪装成浏览器
'''