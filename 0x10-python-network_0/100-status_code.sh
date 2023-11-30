#!/bin/bash
# sends req to URL passed as 1st arg and displays status code only
curl -slw "%{http_code}" -o /dev/null "$1"
