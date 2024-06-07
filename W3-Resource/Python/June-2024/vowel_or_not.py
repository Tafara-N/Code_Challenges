#!/usr/bin/env python3

"""
Program to test whether a passed letter is a vowel or not
"""

def vowel_or_not(letter):
    """
    Function to test whether a passed letter is a vowel or not
    """
    vowels = 'aeiou'
    if letter.lower() in vowels:
        return True
    else:
        return False

if __name__ == '__main__':
    letter = input('Enter a letter: ')
    if vowel_or_not(letter):
        print(f'{letter} is a vowel')
    else:
        print(f'{letter} is not a vowel')
