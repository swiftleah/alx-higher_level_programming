#!/bin/bash
# takes URL as arg, sends GET request and displays body of response
curl -sH "X-School-User-Id: 98" "$1"
