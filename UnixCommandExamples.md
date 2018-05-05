# Data Science - Unix Command Examples

## File system Command

### cat
cat is a standard Unix utility that reads files sequentially, writing them to standard output. The name is derived from its function to concatenate files.

### Syntax

``cat [options] [file_names]``

-b number non-blank output lines
-e implies -v but also display end-of-line characters as $ (GNU only: -E the same, but without implying -v)
-n number all output lines
-s squeeze multiple adjacent blank lines
-t implies -v, but also display tabs as ^I (GNU: -T the same, but without implying -v)
-u use unbuffered I/O for stdout. POSIX does not specify the behavior without this option.
-v (GNU: --show-nonprinting), displays nonprinting characters, except for tabs and the end of line character

### chomd
chmod is the command and system call which may change the access permissions to file system objects (files and directories). It may also alter special mode flags. The request is filtered by the umask. The name is an abbreviation of change mode.

### Syntax

``chmod [options] mode[,mode] file1 [file2 ...]``


-R recursive, i.e. include objects in subdirectories
-f force, forge ahead with all objects even if errors occur
-v verbose, show objects processed

### chowner
The command chown, an abbreviation of change owner, is used on Unix-like systems to change the owner of file system files, directories.

### Syntax

``chown [-h] owner[:group] file...``

``chown -R [-H|-L|-P] owner[:group] file...``
