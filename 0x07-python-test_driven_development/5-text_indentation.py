#!/usr/bin/python3
"""
function text_indentation
Args: text
prints 2 newlines after . ? or semi colon
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = ""
    prev_char_was_separator = False

    for char in text:
        if char in ".?:":
            formatted_text += char + '\n\n'
            prev_char_was_separator = True
        else:
            formatted_text += char
            prev_char_was_separator = False

    lines = formatted_text.split('\n')
    lines = [line.strip() for line in lines]
    formatted_text = '\n'.join(lines)
    print(formatted_text)
