import json
from six.moves import urllib
url = urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos")
data = json.loads(url.read().decode())
for item in data:
    url = item['url']
    thumbnailUrl = item['thumbnailUrl']
    urllib.request.urlretrieve(url, "/tmp/samp")
    urllib.request.urlretrieve(thumbnailUrl, "/tmp/samp")
    break
   

