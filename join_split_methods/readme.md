# Join & Split

## As String methods
- string.split()
- string.join()

## As OS module methods
- os.path.split()
- os.path.join()

## str.split():
- Where to use?
    - Used to split a string as required and convert it into an iterable.

- Syntax
    - string.split('split_operator', maxsplit)

- Demo.py
    - Split a string using different separators.
    - Get the first name only from a list of full names.

## str.Join():
- Where to use?
    - Used to join a list/tuple as required and convert 
    it into a string.

- Syntax
    - 'join_operator'.join(iterable)

- demo.py
    - Join texts from a list of texts.

## os.path.split():
- Where to use?
    - Used to correctly split the path of a file at '/' or '\', automatically and gives back the 
    filename. It makes the split of the file names os independent.

- Syntax
    - os.path.split(path)

- Demo.py
    - split the path of a file and get back the file name.

## os.path.join():
- Where to use?
    - Joins one or more path names into one complete path. So, Instead of hard-coding the path of a file or directory manually, use this method to join path components intelligently.

- Syntax
    - os.path.join(path1, path2, path3, ...)

- Demo.py
    - join the paths of a file to the current directory.


## Project demo
- A file containing 500 phone numbers is given. Read all the phone numbers from that file, split the country codes from the phone numbers and put them inside a bracket, spilt the country code and phone numbers with hyphen(-) and save these phone numbers in a separate file.

for example:
convert phone_num = 918888888888  into phone_num =  (91)-8888888888