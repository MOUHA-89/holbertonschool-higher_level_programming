#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        result += char
        skip_space = False

        if char in punctuation:
            result += "\n\n"
            skip_space = True

    print(result.format())
