#Van Nguyen
#4/5/2018
#This program will open a file in the directory and report back the lines, words, and characters.


import os

def main():

    print("This program will open a file in the directory and report back the lines, words, and characters.")
    file = open('jabber.txt', 'r')
    lines = 0
    words = 0
    chars = 0
    for line in file:
        wordCount = line.split()
        lines += 1
        words += len(wordCount)
        for x in line:
            chars += 1
    print("This file contains %d lines, %d words, and %d characters!" % (lines, words, chars))

    file.close()
main()