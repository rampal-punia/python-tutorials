# Python inbuild functions we are going to discuss:
    - map()
    - sorted()
    - zip()
    - filter()
    - reduce()

# Map():
    - Where to use?
        -- Used to apply some operations on each element of an iterable.

    - Syntax
        -- map(function, iterable).  

    - Practical
        -- Convert a list of floats to int.
        -- Get names only from a list of emails.

    - Take the output as a list or it will return the map object. In that case we  need to use it in a for loop.

# Sorted():
    - Where to use?
        -- Used to sort a list, dictionary, tuple or sets.

    - Syntax
        -- sorted(iterable, key=None, reverse=False)

    - Practical
        -- General uses.
        -- Sorting using lambdas.

# Zip():
    - Where to use?
        -- Zip takes two or more iterables as arguments and returns a list of tuples. Each tuple consists the element of the same index from those iterators. zip() can accept any type of iterable, such as lists, tuples, dictionaries, sets, and so on.

        The length of the tuple will be equal to the length of the shortest iterable. 

    - Syntax
        -- zip(iterable1, iterable2, iterable3, ...)

    - Practical
        -- zipping int, letter, float lists.
        -- Passing lists of unequal lengths.

# Filter():
    - Where to use?
        -- Get a list filtered for the desired output, based on some conditions.

    - Syntax
        -- filter(function, iterable)

    - Practical
        -- get vowels from a list of alphabets.
        -- Get a list of odd numbers from a list of numbers.


# reduce()
    - Where to use?
        -- This function is useful when we need to apply some operations to an iterable and reduce it to a single collective value.

    - Syntax
        -- First import it (from functools import reduce)
        -- reduce(function, iterable)

    - Practical
        -- Get the product of all the elements of a list.