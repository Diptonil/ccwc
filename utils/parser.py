from argparse import ArgumentParser
import logging


class Parser:
    """Custom CLI parser."""

    def __init__(self) -> None:
        self.parser = ArgumentParser(prog="ccwc", description="Tool to show word, line, character, and byte count.", add_help=False)
        self.add_parser_arguments()
        self.args = vars(self.parser.parse_args())
        print(self.args)

    def __str__(self) -> str:
        return "The main argument parser."
    
    def add_parser_arguments(self) -> None:
        """Adds all required arguments to the parser."""
        positional_arguments_group = self.parser.add_argument_group("POSITIONAL ARGUMENTS")
        positional_arguments_group.add_argument("file", type=str, help="The file path that needs to be analysed.")
        options_group = self.parser.add_mutually_exclusive_group()
        options_group.add_argument("-h", "--help", action="help", help="To show this help message.")
        options_group.add_argument("-c", "--bytes", action="store_true", help="To show number of bytes in a file.")
        options_group.add_argument("-l", "--lines", action="store_true", help="To show number of lines in a file.")
        options_group.add_argument("-w", "--words", action='store_true', help="To show number of words in a file.")
        options_group.add_argument("-m", "--characters", action='store_true', help="To show number of characters in a file.")

    def get_file_name(self) -> str:
        """Returns the source file name."""
        return self.args["file"]

    def needs_bytes(self) -> bool:
        """Returns if -c flag is passed."""
        return self.args["bytes"]

    def needs_lines(self) -> bool:
        """Returns if -l flag is passed."""
        return self.args["lines"]
    
    def needs_words(self) -> bool:
        """Returns if -w flag is passed."""
        return self.args["words"]
    
    def needs_characters(self) -> bool:
        """Returns if -m flag is passed."""
        return self.args["characters"]
    