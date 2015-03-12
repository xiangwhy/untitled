import urllib.request
import urllib.parse
import json


key = input("请输入:")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data = {}
data['type'] = 'AUTO'
data['i'] = key
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'utf-8'
data['typoResult'] = 'true'
head = {}
head['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0"
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data, head)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")
j = json.loads(html)
print(j['translateResult'][0][0]['tgt'])
print('收到的json:',html)

# print(req.headers)