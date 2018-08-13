#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:04:04 2018

@author: olli
"""

"""Retrieve and print words from a URL"""

from urllib.request import urlopen

def fetch_words():
    """Fetch a list of words from URL."""
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):
    """Print items one per line."""
    for word in story_words:
        print(word)
        
def main():
    """Print each word from a text document from a URL."""
    words = fetch_words()
    print_words(words)
            
if __name__ == '__main__':
    main()    
