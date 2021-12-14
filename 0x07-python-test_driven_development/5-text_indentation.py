#!/usr/bin/python3
"""
Module for text indentation function
"""


def text_indentation(text):
    """
    Function to indent text
    """
    start = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    if len(text) == 0:
        print()
    else:
        for s in range(len(text)):
            if (text[s] == ' ' or text[s] == '   ') and start == 0:
                s += 1
            elif text[s] != '.' and text[s] != '?' and text[s] != ':':
                print(text[s], end='')
                start = 1
            else:
                print(text[s])
                print()
                start = 0   
