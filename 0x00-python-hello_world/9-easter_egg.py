#!/usr/bin/python3
with open('poem.txt', 'r') as f:
    for x in f:
        print(x.strip())
