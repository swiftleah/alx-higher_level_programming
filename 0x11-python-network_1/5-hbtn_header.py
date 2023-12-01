#!/usr/bin/python3
""" takes URL, sends req and displays X-request-Id in response header """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print("{}".format(req.headers.get("X-Request-Id")))
