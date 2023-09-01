#!/usr/bin/python3
"""
function text_indentation
Args: text
prints 2 newlines after . ? or semi colon
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [".", "?", ":"]
    lines = []
    line = ""

    for char in text:
        if char == '\n':
            lines.append(line)
            lines.append("")
            line = ""
        else:
            line += char
            if char in punctuation:
                lines.append(line)
                lines.append("")
                line = ""

    if line:
        lines.append(line)

    for line in lines:
        print(line)
