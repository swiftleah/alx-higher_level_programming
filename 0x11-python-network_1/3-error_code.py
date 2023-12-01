#!/usr/bin/python3
""" takes URL, sends req and displays body of response in utf-8 - otherwise error """
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            decoded_response = response.read().decode('utf-8')
            print(decoded_response)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
