#!/usr/bin/python3

import argparse
import pathlib
import sys
import pkg_resources
from file_handler_dir.file_handler import file_handler_class
from raw_cmdln_entry.cmdln_entry import raw_cmdln_entry_Class


def main():

    # Dynamically get version from setup
    __version__ = pkg_resources.require("list-to-tabs")[0].version


    parser = argparse.ArgumentParser(
        description="Splits single newline seperated host "
        "file into Konsole tab batches",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    base_group = parser.add_argument_group("Base options", "Regularly accepted arguments")

    exclusive_group = parser.add_mutually_exclusive_group(required=False)
    # Not implemented fully
    exclusive_group.add_argument(
        "-x", "--xmode",
        help="-x / --xmode cannot be used with any other options"
             "\nIn xmode, list-to-tabs will prompt for newline entries "
             "to be typed directory onto cmdln (Until blank newline is "
             "processed which will terminate the loop and print on exit)"
    )

    base_group.add_argument(
        "-v", "--version",
        help="get current package version",
        action='version',
        version='%(prog)s ' + __version__
    )
    exclusive_group.add_argument(
        "-s", "--source",
        help="fully qualified path to host list - /path/to/list",
        type=pathlib.Path
    )
    base_group.add_argument(
        "-d", "--dest",
        help="fully qualified path to output dir - /path/to/output_dir (Default is CWD)",
        type=pathlib.Path,
        default=pathlib.Path().absolute(),
        required=False
    )
    base_group.add_argument(
        "-b", "--batch",
        default=(sys.maxsize / 2),
        help="set number of hosts per batch - default is entire file",
        type=int
    )
    base_group.add_argument(
        "-n", "--name",
        default="output_batch",
        help="set name of batches - default name is output_batch",
        type=str
    )
    base_group.add_argument(
        "-c", "--command",
        default="ssh",
        help="Set the command to enter into tabs file - default is ssh <host>",
        type=str
    )




    passed_args = vars(parser.parse_args())
    test_parse = parser.parse_known_args()
    print(passed_args.items())
    print(test_parse)

    sys.exit()

    src_file_path = passed_args["source"]
    dest_dir_path = passed_args["dest"]
    output_name = passed_args["name"]

    # Currently unimplemented
    # batch_size = passed_args["batch"]

    if not (src_file_path.is_file()) or not (dest_dir_path.is_dir()):
        print("Source or Destination not reachable")
        sys.exit()

    file_obj = file_handler_class()
    file_dict = file_obj.file_to_dict(src_file_path)

    # TODO: this prints will need to be removed
    print(file_dict.values())

    file_dict = {
        host: file_obj.text_transform(file_dict[host], "ssh") for host in file_dict
    }

    for item in file_dict.values():
        file_obj.insert_into_file(dest_dir_path, output_name, item)

    for item in file_dict.items():
        print(item)
    # TODO: need to check this prior to appending to file so that it can be incremented
    # print(file_handler_dir.check_if_file(des_file))


if __name__ == "__main__":
    main()
