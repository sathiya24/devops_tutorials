#script for jq loop downloading 2 keys from json array into 2 folders

#!/bin/bash

wget --output-document=input.json 'https://jsonplaceholder.typicode.com/photos'
mkdir images8
mkdir thumbnails8
jq -c -r '.[] | .url + " " + .thumbnailUrl' input.json | while read i; do
    echo $i -P ./images8
    echo $i -P ./thumbnails8
     
     

