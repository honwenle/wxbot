from urllib import request, parse
import json

def pinyin(string):
    showapi_appid="47105"
    showapi_sign="2ab06446f6944a1e98d03db25bf9c46e"
    url="http://route.showapi.com/99-38"
    send_data = parse.urlencode([('showapi_appid', showapi_appid),('showapi_sign', showapi_sign),('content', string)])
    req = request.Request(url)
    try:
        response = request.urlopen(req, data=send_data.encode('utf-8'), timeout = 10) # 10秒超时反馈
    except Exception as e:
        print(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)
    return result_json

print(pinyin('你好')['showapi_res_body']['data'])