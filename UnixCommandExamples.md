# Data Science - Unix Command Examples

## File system Command

### cat
cat is a standard Unix utility that reads files sequentially, writing them to standard output. The name is derived from its function to concatenate files.

### Syntax

cat [options] [file_names]

-b number non-blank output lines
-e implies -v but also display end-of-line characters as $ (GNU only: -E the same, but without implying -v)
-n number all output lines
-s squeeze multiple adjacent blank lines
-t implies -v, but also display tabs as ^I (GNU: -T the same, but without implying -v)
-u use unbuffered I/O for stdout. POSIX does not specify the behavior without this option.
-v (GNU: --show-nonprinting), displays nonprinting characters, except for tabs and the end of line character
