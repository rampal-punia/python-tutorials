'''✨ Python Code Example ✨'''

import random


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_color_hex():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'
