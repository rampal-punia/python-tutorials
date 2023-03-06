# Pathlib module

[Pathlib](https://docs.python.org/3/library/pathlib.html) module was introduced in Python 3.4 with [PEP 428](https://peps.python.org/pep-0428/). It is a part of the Python standard library that provides an object-oriented interface for working with file paths. It allows us to create, manipulate, and operate on file paths in a platform-agnostic way.

Before introduction to this module in Python, the obvious module to work with files was OS module, which by the way is still very handy for many useful tasks. But for working with files OS module manipulates the files path as pure strings. Whereas the Pathlib module takes an object-oriented approach.

## Import Path Class

```python
from pathlib import Path

# Path is a PurePath subclass that can make system calls.
```

The pathlib module provides a set of classes that represent file paths as objects, rather than just strings. These classes provide a number of methods for working with file paths, such as `exists()`, `is_file()`, and `mkdir()`.

For example, we can use the Path class from the pathlib module to create a file path object, and then use the exists() method to check whether the file or directory specified by the path exists:

```python
from pathlib import Path

path = Path('/path/to/file')
if path.exists():
    print('The file or directory exists')
else:
    print('The file or directory does not exist')

```

We can also use the Path class to manipulate file paths, such as by changing the name or extension of a file, or by joining multiple file paths together. It can be particularly useful when we need to perform file system operations that involve complex file paths, or when we need to work with file paths in a platform-specific way.

## Methods Available On Path Object

To get all the methods available on the Path object we will use the built-in function `dir()`.

```python
print([method for method in dir(Path) if not method.startswith('_')])

# Output
['absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'glob', 'group', 'home', 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_mount', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'link_to', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'with_name', 'with_suffix', 'write_bytes', 'write_text']
```

## Directory Paths

```python
# Get current working directory
cwd = Path.cwd()
print(cwd)  # /home/ram/working-with-files

# Get home directory
print(Path.home())  # /home/ram

# Make a directory
path = Path.cwd() / "demofiles"
path.mkdir()

# Join path
cwd = Path.cwd()
req_dir = cwd / "files"
print(req_dir)  # /home/ram/working-with-files/files
```

## Files Path

```python
# Check if a file exists
file = Path('readme.md')
print(file.exists())        # True

# Join path
cwd = Path.cwd()
req_dir = cwd.joinpath("files")
print(req_dir)  # /home/ram/working-with-files/files

# List all files & dirs in a directory
child_obj = req_dir.iterdir()
for child in child_obj:
    print(child)
# Output
/home/ram/working-with-files/files/titanic_data.csv
/home/ram/working-with-files/files/excels
/home/ram/working-with-files/files/file3.csv
/home/ram/working-with-files/files/file1.txt
/home/ram/working-with-files/files/file2.txt

# Get a file with specific extension from a directory
print(sorted(req_dir.glob('*.txt')))
# Output:
[PosixPath('/home/ram/working-with-files/files/file1.txt'), PosixPath('/home/ram/working-with-files/files/file2.txt')]
```

## Files MetaData

```python
# Access a file
file = Path.cwd() / "readme.md"

# get absolute path of the file
absolute_path = file.resolve()
print(absolute_path)
# Output: /home/ram/working-with-files/readme.md

# Get parent folder
print(absolute_path.parent)
# Output: /home/ram/working-with-files

# Get name of the file
print(file.name)
# Output: readme.md

# Get suffix
print(file.suffix)
# Output: .md

# Get stem
print(file.stem)
# Output: readme

# Get root
print(file.root)
# Output: /

# Get parts of the path
print(file.parts)
# Output: ('/', 'home', 'ram', 'working-with-files', 'readme.md')

# Create new file in current working directory
Path.touch((Path(".") / "new_file.md"))
# Or
Path.touch((Path.cwd() / "new_file.md"))

# Check Stat of this file
print(file.stat())
# Output
os.stat_result(st_mode=33188, st_ino=540055, st_dev=2080, st_nlink=1, st_uid=1000, st_gid=1000, st_size=1503, st_atime=1673239779, st_mtime=1673239779, st_ctime=1673239779)

# Access stat with key like
print(file.stat().st_size)      # 1503
print(file.stat().st_mtime)     # 1673239779.7524743
```

## Reading and Writing To Files

```python
# Read and Write to a file
file = Path('demo.txt')

# Create the file and write data
file.write_text("Hello demo file")

# read data from the file
print(file.read_text())
```

## Deleting A File and Directory

```python
# Remove a file
file = Path(".") / "new_file.md"
file.unlink()

# Remove a dir, Dir must be empty. (Still Be careful with this. Removes permanently.)
dir = Path(".") / "demodir"
dir.rmdir()
# If not empty the following error occurs
#  OSError: [Errno 39] Directory not empty:
```

## Difference between Pathlib and OS modules of Python

Pathlib and os are both Python modules that provide functions for working with file and directory paths. Pathlib is a more modern and object-oriented way of working with file paths, while os is a more traditional, functional way of working with file paths.

Here are some differences between the two modules:

|Pathlib|OS|
|-------------------|-------------------------|
|It provides a more intuitive and Pythonic interface for working with file paths, using classes and methods to represent and manipulate file paths. |It provides a more procedural interface, with functions that perform various operations on file paths.|
|It represents paths as objects with useful methods and attributes|It represents paths as strings.|
|pathlib is generally easier to use and more readable, especially when working with long chains of path manipulations. It also has a more consistent API and better support for Unicode paths.|os is generally more powerful and flexible, and is often used in cases where pathlib does not provide the necessary functionality. It also has a wider range of functions for working with the operating system and the filesystem.
|||
