#!/bin/bash
#bash script to make a delete request from a url
curl -sI "$1" | awk '/Allow/ {print $2}'
