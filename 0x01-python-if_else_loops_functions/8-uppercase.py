#!/usr/bin/env python3

def uppercase(str):
    now_upp = ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in str)
    print("{}".format(now_upp))
