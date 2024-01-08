import argparse

parser_descp = f"Splits single newline seperated host file into Konsole tab batches"

class _parser(argparse.ArgumentParser(description=parser_descp, formatter_class=argparse.ArgumentDefaultsHelpFormatter)):
    def __init__(self):
        self.add_argument("SRC", help="Fully quilified path to host list - /path/to/list")
        self.add_argument("DEST", help="Fully quilified path to output dir - /path/to/output_dir")
        self.add_argument("-b", "--batch_size", help="Set number of hosts per batch - default is 6")
        self.add_argument("-n", "--file_name", help="Set name of batches - default is batch#")


