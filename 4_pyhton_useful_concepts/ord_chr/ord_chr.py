'''Python Tutorials: ord() and chr() introduction.
'''

lower_chars = "a quick brown fox jumps over the lazy dog"
upper_chars = lower_chars.upper()

chars_unicode = {i: chr(i) for i in range(1114111)}

with open("chars_unicode.txt", 'w') as f:
    f.write(str(chars_unicode))
