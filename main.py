"""
Simple rotational cipher, given text and integer key
which specifies how many steps to shift each letter
"""


letters_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rotate(text, key):
    new_txt = ''
    for letter in text:
        if letter not in letters_l and not letter.isupper():
            new_txt += letter
        fix_letter = letter.lower()

        if fix_letter in letters_l:
            new_lttr = letters_l.index(fix_letter)
            new_lttr += key
            if new_lttr > 25:
                new_lttr -= 26
            if letter.isupper():
                new_txt += letters_l[new_lttr].upper()
            if letter.islower():
                new_txt += letters_l[new_lttr]
    return new_txt

