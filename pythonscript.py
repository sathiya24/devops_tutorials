import json
from six.moves import urllib
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:
     data = json.loads(url.read().decode())
for item in data:
    url = item['url']
    thumbnailUrl = item['thumbnailUrl']
    urllib.request.urlretrive(url, "/tmp/")
    urllib.request.urlretrive(thumbnail,"/tmp/")
   

