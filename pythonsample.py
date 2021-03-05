import os
from PIL import Image
import json
from six.moves import urllib
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
    urllib.request.urlretrieve(url, "/tmp/" + uniquename)
    urllib.request.urlretrieve(thumbnailUrl, "/tmp/" + uniquename1)
    im = Image.open("/tmp/" + uniquename)
    im1 = Image.open("/tmp/" + uniquename1)
    new_width = (im.size[0] * 2)
    new_height = (im.size[1] * 2)
    new_width1 = (im1.size[0] * 2)
    new_height1 = (im1.size[1] * 2)
    new_size = im.resize((new_height, new_width))
    new_size1 = im1.resize((new_height1, new_width1))
    break


