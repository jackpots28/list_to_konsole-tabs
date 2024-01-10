#!/usr/bin/python3

# from arg_parser.arg_parser import _parser
from file_handler import file_handler
from pathlib import Path

src_path = Path("/home/simsjo-a")
src_file = src_path/"server.list"

des_path = Path("/home/simsjo-a/tabs")
des_file = des_path/"batch"

default_batch_size = 6

# print(list(src_path.glob("**/*")))

if __name__ == "__main__":
    file_dict = file_handler.file_to_dict(src_file)
    
    print(file_dict.values())
    print(len(file_dict))

    default_batch_size = len(file_dict)

    file_dict = {x: file_handler.text_formatter(file_dict[x]) for x in file_dict}

    for item in file_dict.values():
        file_handler.insert_into_file(des_file, item)

    print(file_dict)