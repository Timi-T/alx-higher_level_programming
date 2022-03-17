#!/bin/bash
#bash script to make a delete request from a url
curl -X OPTIONS "$1" | awk '/Allow/ {print $2}'
