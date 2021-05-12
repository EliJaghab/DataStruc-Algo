def reverse_words(message):
    # Reverse all the Characters in the Entire Message
    reverse_characters(message, 0, len(message) - 1)

    # Make Each Individual Word Read Forwards

    # Hold the Index of the Start of the Current Word
    currStart = 0

    for i in range(len(message) + 1):
        if (i == len(message) or (message[i] == ' ')):
            reverse_characters(message, currStart, i - 1)
            currStart = i + 1


def reverse_characters(message, start, end):

    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1
