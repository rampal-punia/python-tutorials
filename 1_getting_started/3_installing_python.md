# Steps to Install Python

Note:- If you are on Linux, chances are you already have a version of Python pre-installed. You can always download the newer version.

## Download Python Version for your OS

- Visit Python's [official website](https://www.python.org/).

- If you are on Windows; Under Downloads tab click 'Download Python <version_name> button. Or click 'All Releases'.

- Select you OS/platform and download the latest stable release.

## Installation

### Linux

```bash
$ sudo apt-get update
$ sudo apt-get install python3 # Or use
$ sudo apt-get upgrade python3

# For creating virtual environments
$ sudo apt-get install python3-dev python3-pip

pip3 install virtualenv
```

### macOS

- Install Brew

```bash
brew install python3
```

### Windows

- Run the installer and follow the instructions.

Note:- On window, `checkbox` to add the Python to your PATH should be checked, if the installer offers this option.

For creating python virtual environments, see this gist: [Setup-Python3-virtual-environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7)
