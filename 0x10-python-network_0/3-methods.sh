#!/bin/bash
#bash script to make a delete request from a url
curl -sX OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f1 --complement
