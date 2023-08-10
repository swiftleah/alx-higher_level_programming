#!/usr/bin/python3

import hidden_4

hidden_names = [name for name in dir(hidden_4) if not name.startswith('__')]
for name in hidden_names:
    print("{}".format(name))
