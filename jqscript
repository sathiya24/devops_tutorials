#!/bin/bash

wget --output-document=jqpro1 'https://jsonplaceholder.typicode.com/photos'
mkdir images2
mkdir thumbnail
jq -c -r '.[] | .url' jqpro1 | while read i; do
    echo $i -P ./images2
done
jq -c -r '.[] | .url' jqpro1 | while read i; do
    echo $i -P ./thumbnail
done
