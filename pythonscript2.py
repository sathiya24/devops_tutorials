import os
import json
from six.moves import urllib
url = urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos")
data = json.loads(url.read().decode())
for item in data:
    url = item['url']
    thumbnailUrl = item['thumbnailUrl']
    uniquename = (os.path.basename(url))
    uniquename1 = (os.path.basename(thumbnailUrl))
    print()
    print(uniquename)
    print(uniquename1)
    print()
    urllib.request.urlretrieve(url, "/tmp/" + uniquename)
    urllib.request.urlretrieve(thumbnailUrl, "/tmp/" + uniquename1)
