#!/usr/bin/python3
# takes URL and email, sends POST req and displays body of reponse
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        decoded_response = response.read().decode('utf-8')
    print(decoded_response)
