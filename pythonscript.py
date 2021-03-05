import urllib.request, json
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:
    data = json.loads(url.read().decode())
for item in data:
    url = item['url']
    thumbnailUrl = item['thumbnailUrl']
    urllib.request.urlretrieve(url, '/tmp/')
    urllib.request.urlretrieve(thumbnailUrl, '/home/sathya/Downloads/python')

