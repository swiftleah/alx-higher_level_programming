#!/bin/bash
# takes in a URL, sends request to that URL and displays size of body
# size in bytes and must use curl
curl -s "$1" | wc -c
