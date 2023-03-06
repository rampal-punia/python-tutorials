# Single line, small and anonymous functions.


# Sort the list according to the last character of the name.
names = ['Dane', 'Albert', 'Jack', 'Oberon', 'Richard']
print(sorted(names, key=lambda x: x[-1]))
