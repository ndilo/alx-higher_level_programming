#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.

    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    line = ""

    for char in text:
        # Append the character to the current line
        line += char

        # Check if the character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            # Print the line with 2 new lines
            print(line.strip())
            print()
            # Reset the line to an empty string
            line = ""

    # Print any remaining text in the last line
    if line:
        print(line.strip())
