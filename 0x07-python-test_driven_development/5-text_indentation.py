#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    k = 0
    while k < len(text) and text[k] == ' ':
        k += 1

    while k < len(text):
        print(text[k], end="")
        if text[k] == "\n" or text[k] in ".?:":
            if text[k] in ".?:":
                print("\n")
            k += 1
            while k < len(text) and text[k] == ' ':
                k += 1
            continue
        k += 1
