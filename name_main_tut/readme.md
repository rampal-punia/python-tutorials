# What is __name__ == "__main__"

# Practical use case one
    --> If the requirement is to run a particular code from an specific file only, not if that file is imported. 
    
    --> It also avoids accidently running a script, which is meant to be run from the main file only.

    --> This file can be used as the main program or imported by other module.

# Practical use case two
    --> If you need to write code in collaboration where the type of variables is known but practically no variable is yet provided.

    suppose you are requested to build some code for the situations mentioned below.
    
    1. Add 'n' elements of a list.

    2. Create two separate list from the dictionary of the keys with superheroes and actors. And create two separate text file from them.
