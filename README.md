# Data Science - Sublime Text Environment configurations

## Install Homebrew

Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's macOS operating system.

install the latest XCode and then run the following command to install:

``/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``

add the following line to your .bashrc or .zshrc:

``export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"``



## Generating Token for gitHub for sublimeText

``curl -u {github kakuffo} -d '{"scopes":["gist"], "note": "sublime-github"}' https://api.github.com/authorizations``


## Install and Use GNU Tools on macOS/OS X

### Install pip

pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the default source for packages and their dependencies

``sudo easy_install pip``

#### key-commands examples

##### pip - Search

``pip search * `` - Will search all available packages for pip

##### Pip - Install a package

``pip install pytest`` - Will install the PyTest framework which can be used for data testing

##### Pip - Uninstall a package

``pip uninstall pytest`` - Will uninstall the PyTest

##### Pip - Show information

``pip show information pyTest``

``Name: pytest
Version: 3.5.1
Summary: pytest: simple powerful testing with Python
Home-page: http://pytest.org
Author: Holger Krekel, Bruno Oliveira, Ronny Pfannschmidt, Floris Bruynooghe, Brianna Laugher, Florian Bruhin and others
Author-email: None
License: MIT license
Location: /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages
Requires: attrs, py, more-itertools, setuptools, pluggy, six
Required-by:``


### grep

grep searches input files for lines containing a match to a given pattern list. When it finds a match in a line, it copies the line to standard output (by default), or produces whatever other sort of output you have requested with options.  Though grep expects to do the matching on text, it has no limits on input line length other than available memory, and it can match arbitrary characters within a line. If the final byte of an input file is not a newline, grep silently supplies one. Since newline is also a separator for the list of patterns, there is no way to match newline characters in a text.


``brew install grep --with-default-names``

#### key-commands examples


### wdiff

wdiff is a front end to diff for comparing files on a word per word basis. It works by creating two temporary files, one word per line, and then executes diff on these files. It collects the diff output and uses it to produce a nicer display of word differences between the original files.

``brew install wdiff --with-gettext``

#### key-commands examples



###  ed

GNU ed is a line-oriented text editor. It is used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts. A restricted version of ed, red, can only edit files in the current directory and cannot execute shell commands. Ed is the "standard" text editor in the sense that it is the original editor for Unix, and thus widely available.

``brew install ed --with-default-names``


#### key-commands examples



### findutills

The GNU Find Utilities are the basic directory searching utilities of the GNU operating system. These programs are typically used in conjunction with other programs to provide modular and powerful directory search and file locating capabilities to other commands.

``brew install findutils --with-default-names``


#### key-commands examples



### gnu-indent

The indent program can be used to make code easier to read. It can also convert from one style of writing C to another. indent understands a substantial amount about the syntax of C, but it also attempts to cope with incomplete and misformed syntax.

``brew install gnu-indent --with-default-names``


#### key-commands examples


### gnu-sed

sed is a stream editor. A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline). While in some ways similar to an editor which permits scripted edits (such as ed), sed works by making only one pass over the input(s), and is consequently more efficient. But it is sed’s ability to filter text in a pipeline which particularly distinguishes it from other types of editors.

``brew install gnu-sed --with-default-names``


#### key-commands examples


### gnu-tar

GNU tar creates and manipulates archives which are actually collections of many other files; the program provides users with an organized and sys- tematic method for controlling a large amount of data. The name “tar” originally came from the phrase “Tape ARchive”, but archives need not (and these days, typically do not) reside on tapes.

``brew install gnu-tar --with-default-names``

#### key-commands examples



### gnu-which

``brew install gnu-which --with-default-names``


### gnu-tls

``brew install gnutls``


#### key-commands examples


### gzip

``brew install gzip``



#### key-commands examples


### gnu-screen

Screen is a full-screen window manager that multiplexes a physical terminal between several processes, typically interactive shells. Each virtual terminal provides the functions of the.


``brew install screen``


### watch

watch is a command-line tool, part of the Linux procps and procps-ng packages, that runs the specified command repeatedly and displays the results on standard output so you can watch it change over time.

``brew install watch``


### gnu-wget

 GNU Wget. A command-line utility for retrieving files using HTTP, HTTPS and FTP protocols.

``brew install wget``


### binutils

The GNU Binary Utilities, or binutils, are a set of programming tools for creating and managing binary programs, object files, libraries, profile data, and assembly source code.

``brew install binutils``

### gnu-diffutils

GNU Diffutils. GNU Diffutils is a package of several programs related to finding differences between files. Computer users often find occasion to ask how two files differ.

``brew install diffutils``

### gnu-gawk

The awk utility interprets a special-purpose programming language that makes it possible to handle simple data-reformatting jobs easily with just a few lines of code. This manual teaches you what awk does and how you can use awk effectively.

``brew install gawk``





