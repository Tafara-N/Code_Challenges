#!/usr/bin/env python3

"""
Function that, given a string of text (possibly with punctuation and line-breaks),
returns an array of the top-3 most occurring words, in descending order of the
number of occurrences
"""

def top_3_words(text: str)-> list:
    """
    Parameters
        text:- A string of text

    Return
        A list of the top 3 most occurring words in the text
    """

    word_dict = {}
    words = text.split()

    for word in words:
        # Remove any non-alphabetic characters from the word
        word = ''.join(filter(str.isalpha, word)).lower()
        # If the word is not empty
        if word:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    sorted_words = sorted(word_dict, key=word_dict.get, reverse=True)
    return sorted_words[:3]


text = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

print(top_3_words(text))