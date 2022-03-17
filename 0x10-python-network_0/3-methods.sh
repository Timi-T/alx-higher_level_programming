#!/bin/bash
#bash script to make a delete request from a url
curl -siX OPTIONS "$1" | awk '/Allow/ {print $2}'
