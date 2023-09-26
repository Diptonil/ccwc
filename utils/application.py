import os
import sys
import logging


class Application:
    """The core functionality is handled here."""

    def __init__(self, file_name: str, requirements: dict) -> None:
        self.file_name = file_name
        self.requirements = requirements
        self.file_validity_check()
        self.file_data = self.get_file_data()

    def file_validity_check(self) -> None:
        """Checks if the file exists and is valid."""
        if self.file_name == "<stdin>":
            self.file_name = "temp.txt"
            with open(self.file_name, "w") as file:
                file.write(sys.stdin.read())
        if not os.path.exists(self.file_name):
            logging.error("Path specified does not exist.")
            sys.exit()
        elif os.path.isdir(self.file_name):
            logging.error("Path specified is that of a directory, not a file.")
            sys.exit()

    def get_file_data(self) -> str:
        """Returns the contents of the entire file as a string"""
        file_data = None
        with open(self.file_name, "r") as file:
            file_data = file.read()
        return file_data
    
    def get_bytes(self) -> int:
        """Returns the number of bytes in the file."""
        data = os.path.getsize(self.file_name)
        return data

    def get_lines(self) -> int:
        """Returns the number of lines in the file."""
        return len(self.file_data.split("\n")) - 1
    
    def get_words(self) -> int:
        """Returns the number of words in the file."""
        return len(self.file_data.split()) 
    
    def get_characters(self) -> int:
        """Returns the number of lines in the file."""
        return len(self.file_data.encode(sys.getfilesystemencoding()))
    
    def get_result(self) -> None:
        """To evaluate final result."""
        if self.file_name == "temp.txt":
            self.file_name = ""
        if self.requirements["needs_bytes"]:
            print(self.get_bytes(), self.file_name)
        elif self.requirements["needs_lines"]:
            print(self.get_lines(), self.file_name)
        elif self.requirements["needs_words"]:
            print(self.get_words(), self.file_name)
        elif self.requirements["needs_characters"]:
            print(self.get_characters(), self.file_name)
        else:
            print(self.get_lines(), self.get_words(), self.get_bytes(), self.file_name)
