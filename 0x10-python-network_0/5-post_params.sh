#!/bin/bash
# takes in URL and sends POST req. displays body of response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
