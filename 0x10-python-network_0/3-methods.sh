#!/bin/bash
#bash script to make a delete request from a url
curl -sIX OPTIONS "$1" | awk '/Allow/ {print $2}'
