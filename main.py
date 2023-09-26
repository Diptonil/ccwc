import atexit
import os

from utils.parser import Parser
from utils.application import Application


def delete_temporary_file() -> None:
    """Removes the temporary file generated during piping of data, if it exists."""
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")


def main() -> None:
    atexit.register(delete_temporary_file)
    parser = Parser()    
    file = parser.get_file_name()
    requirements = {
        "needs_bytes": parser.needs_bytes(),
        "needs_lines": parser.needs_lines(),
        "needs_words": parser.needs_words(),
        "needs_characters": parser.needs_characters()
    }
    app = Application(file, requirements)
    app.get_result()


if __name__ == '__main__':
    main()
