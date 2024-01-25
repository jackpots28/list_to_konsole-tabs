import unittest
import tempfile
from pathlib import Path
from file_handler_dir import file_handler

temp_file = tempfile.NamedTemporaryFile()
test_string = "cmd"
test_output_name = Path(temp_file.name).name
test_output_dir = "/tmp"

class TestArgPassing(unittest.TestCase):
    def test_file_to_dict(self):
        self.assertEqual(
            file_handler.file_handler_class.file_to_dict(Path(temp_file.name)),
            second=dict()
        )

    def test_insert_into_file(self):
        file_handler.file_handler_class.insert_into_file(
            Path(test_output_dir),
            test_output_name, test_string
        )


if __name__ == "__main__":
    unittest.main()