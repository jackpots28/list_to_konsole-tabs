import unittest
from pathlib import Path
from file_handler_dir import file_handler


class TestArgPassing(unittest.TestCase):
    def test_src_file_type(self):
        self.assertEqual(file_handler.check_if_file(Path("/this/is/a/test")), True)


if __name__ == "__main__":
    unittest.main()
