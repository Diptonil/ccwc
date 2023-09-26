from utils.parser import Parser


def main() -> None:
    parser = Parser()    
    file = parser.get_file_name()
    needs_bytes = parser.needs_bytes()
    needs_lines = parser.needs_lines()
    needs_words = parser.needs_words()
    needs_characters = parser.needs_characters()



if __name__ == '__main__':
    main()
