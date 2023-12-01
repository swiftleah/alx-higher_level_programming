#!/usr/bin/python3
# takes github credentials and uses github API to display id
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, passwd))

    if response.status_code == 200:
        user_info = response.json()
        print("{}".format(user_info['id']))
    else:
        print(None)
