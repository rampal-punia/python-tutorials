methods = ['capitalize', 'casefold', 'center',
           'count', 'encode', 'endswith',
           'expandtabs', 'find', 'format',
           'format_map', 'index', 'isalnum',
           'isalpha', 'isascii', 'isdecimal',
           'isdigit', 'isidentifier', 'islower',
           'isnumeric', 'isprintable', 'isspace',
           'istitle', 'isupper',
           'join', 'ljust', 'lower',
           'lstrip', 'maketrans',
           'partition', 'replace', 'rfind',
           'rindex', 'rjust', 'rpartition', 'rsplit',
           'rstrip', 'split', 'splitlines', 'startswith',
           'strip', 'swapcase', 'title', 'translate', 'upper',
           'zfill']

str_1 = "Learning Python Is A Fun"
for item in methods:
    print(f"print(f'{item} is :{{str_1}}.{item}()')")
