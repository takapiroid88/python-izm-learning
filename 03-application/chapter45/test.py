# HTML文字列の取得
import urllib.request

url = 'https://www.python-izm.com'

htmldata = urllib.request.urlopen(url)
print(htmldata.read().decode('UTF-8'))

htmldata.close()