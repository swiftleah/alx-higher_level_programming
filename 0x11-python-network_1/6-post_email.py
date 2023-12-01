#!/usr/bin/python3
# takes URL and email, sends POST req and displays body of reponse
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})
    print(response.text)
