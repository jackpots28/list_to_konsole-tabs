from pathlib import Path


def get_subdirs(file_path: Path):
    list_of_dirs = [x for x in file_path.iterdir() if x.is_dir()]
    print(list_of_dirs)

def check_if_file(file_path: Path)->bool:
    return file_path.exists and not file_path.is_dir()

def print_contents(file_path: Path):
    with open(file_path) as file:
        for line_num, line_content in enumerate(file):
            print(line_num, line_content)