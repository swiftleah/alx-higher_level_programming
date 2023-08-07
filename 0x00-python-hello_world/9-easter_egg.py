#!/usr/bin/python3

file_path = 'poem.txt'
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())
