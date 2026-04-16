"""
A simple program that reads a file, counts lines,
words, and letters, prints the results, and appends
statistics back to the file.
"""


def file_info(filename):
    """Counts lines, words, and letters in a file
    and appends the results to it."""

    file = open(filename, "r", encoding="utf-8")
    text = file.read()
    file.close()

    lines = text.split("\n")
    line_count = len(lines)

    words = text.split()
    word_count = len(words)

    letter_count = 0
    for symbol in text:
        if symbol not in (" ", "\n"):
            letter_count += 1

    print("Number of lines:", line_count)
    print("Number of words:", word_count)
    print("Number of letters:", letter_count)

    file = open(filename, "a", encoding="utf-8")
    file.write("\n\n--- File statistics ---\n")
    file.write("Lines: " + str(line_count) + "\n")
    file.write("Words: " + str(word_count) + "\n")
    file.write("Letters: " + str(letter_count) + "\n")
    file.close()


file_info("test.txt")
