import json
from six.moves import urllib
url = urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos")
data = json.loads(url.read().decode())
for item in data:
    url = item['url']
    thumbnailUrl = item['thumbnailUrl']
    urllib.request.urlretrive(url, "/tmp/")
    urllib.request.urlretrive(thumbnail,"/tmp/")
   

