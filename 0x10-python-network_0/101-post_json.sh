#!/bin/bash
# sends JSON POST req and displays body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
