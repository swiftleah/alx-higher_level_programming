#!/usr/bin/python3
""" takes URL, sends req to URL & displays value of X-Request-Id var """
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        requestId = response.getheader('X-Request-Id')
        print("{}".format(requestId))
