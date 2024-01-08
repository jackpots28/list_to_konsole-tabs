#!/usr/bin/python3

# from arg_parser.arg_parser import _parser
from file_handler import file_handler
from pathlib import Path

src_path = Path("/stuff")
src_file = src_path/"test.txt"
des_file = f""

print(list(src_path.glob("**/*")))
default_output_name = Path("~/tabs")

if __name__ == "__main__":
    file_handler.get_subdirs(src_path)
    print(file_handler.check_if_file(src_file))
    
    file_handler.print_contents(src_file)