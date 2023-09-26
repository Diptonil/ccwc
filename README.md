# ccwc

An implementation of the UNIX `wc` command (first in a series of coding challenges by John Crickett). This entils no external dependencies. The only built-ins that are used:
- `logging`: To print out error messages.
- `argparse`: To handle the CLI interactivity.
- `os`: For operations on files.
- `sys`: For handling low-level system calls, stdin and exit.
- `atexit`: Exit handlers.


## Files

- `utils/application.py`: Core utility implementation of all options.
- `utils/parser.py`: Definition of the argparse CLI handler.
- `ccwc.py`: Main executable.


## Logic

The tool deals with the logic of:
1. Accepting file name and operating on it, as necessary according to the options.
2. In case file name is not available and file data is piped in via `stdin`, we use the `sys.stdin.read()` call to get the data and store it into a file called "temp.txt". That file is consequently deleted once all operations are done using `atexit`.
The only downside to this approach is if the input file itself is called "temp.txt", in which case the operation would succeed but would lead to the deletion of the main file too. The solution to this would be the generaion of a file name using `random` module (a combination of symbols, digits and alphabets). In that case, the chances of collision of names would be less.


# Usage

Use it exactly the same way as the `wc` command, with available options of:
- `-l`: Line count.
- `-w`: Word count.
- `-m`: Character count.
- `-c`: Byte count.

Example:
```sh
./ccwc.py test.txt
7145  58164 342190 test.txt
```

OR

```sh
cat test.txt | ./ccwc.py
7145  58164 342190
```
