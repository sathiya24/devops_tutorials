import os
import urllib.request, json
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:
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
    urllib.request.urlretrieve(url, "/home/sathya/Downloads/python.png"+ uniquename)
    urllib.request.urlretrieve(thumbnailUrl, "/home/sathya/Downloads/python.png"+ uniquename1)
