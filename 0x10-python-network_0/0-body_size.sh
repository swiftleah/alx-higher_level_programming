#!/bin/bash
# takes in a URL, sends request to that URL and displays size of body
curl -s "$1" | wc -c
