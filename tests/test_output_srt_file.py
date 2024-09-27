from os import path, remove, rmdir
import unittest
from pprint import pprint

from subSplitter.ExtractLanguageSubs import ExtractLanguageSubs
from subSplitter.InputFile import InputFile
from subSplitter.OutputSrtFile import OutputSrtFile


class TestOuputSrtFile(unittest.TestCase):
    def setUp(self):
        extract_language = ExtractLanguageSubs("Default-ja")

        fp = path.abspath("")
        file_path = path.join(
            fp,
            "resources",
            "March Comes in Like a Lion - 01 - Rei Kiriyama - The Town Along the River.ja-en.ass"
        )

        input_file = InputFile(
            file_path
        )

        language_lines = extract_language.parse_desired_language_lines(input_file.read_file_contents())
        self.line_dict = extract_language.extract_subtitle_fields(language_lines)

    def test_create_srt_file_contents(self):
        output_file = OutputSrtFile("fake\pathington", self.line_dict)
        self.assertTrue(output_file.file_contents)

    def test_save_new_srt_file(self):
        output_file_path = r"C:\Users\Sauron\Documents\coding\python\subSplitter\tests\resources"
        output_file = OutputSrtFile(output_file_path, self.line_dict)
        output_file.save_new_srt_file("Default-ja", 1)

        file_exists = path.exists(path.join(output_file_path, "Default-ja", "1.srt"))
        self.assertTrue(file_exists)

    def tearDown(self):
        output_file_path = r"C:\Users\Sauron\Documents\coding\python\subSplitter\tests\resources"
        file_path = path.join(output_file_path, "Default-ja")
        file_exists = path.exists(file_path)
        if file_exists:
            remove(path.join(file_path, "1.srt"))
            rmdir(file_path)


if __name__ == '__main__':
    unittest.main()
