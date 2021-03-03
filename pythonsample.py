import os
from PIL import Image
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
    urllib.request.urlretrieve(url, "/home/sathya/Downloads/" + uniquename)
    urllib.request.urlretrieve(thumbnailUrl, "/home/sathya/Downloads/" + uniquename1)
    im = Image.open("/home/sathya/Downloads/" + uniquename)
    im1 = Image.open("/home/sathya/Downloads/" + uniquename1)
    new_width = (im.size[0] * 2)
    new_height = (im.size[1] * 2)
    new_width1 = (im1.size[0] * 2)
    new_height1 = (im1.size[1] * 2)
    new_size = im.resize((new_height, new_width))
    new_size1 = im1.resize((new_height1, new_width1))
    break


