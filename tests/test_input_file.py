from os import path
import unittest

from subSplitter.InputFile import InputFile


class TestInputFile(unittest.TestCase):
    def setUp(self):
        fp = path.abspath("")
        file_path = path.join(
            fp,
            "resources",
            "March Comes in Like a Lion - 01 - Rei Kiriyama - The Town Along the River.ja-en.ass"
        )

        self.input_file = InputFile(
            file_path
        )

    def test_input_file_class(self):
        self.assertIsInstance(self.input_file, InputFile)

    def test_read_file_contents(self):
        self.assertTrue(self.input_file.file_contents)

if __name__ == '__main__':
    unittest.main()