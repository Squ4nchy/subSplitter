from os import path
import unittest

from subSplitter.ExtractLanguageSubs import ExtractLanguageSubs
from subSplitter.InputFile import InputFile


class TestExtractLanguage(unittest.TestCase):
    def setUp(self):
        self.extract_language = ExtractLanguageSubs("Default-ja")

        fp = path.abspath("")
        file_path = path.join(
            fp,
            "resources",
            "March Comes in Like a Lion - 01 - Rei Kiriyama - The Town Along the River.ja-en.ass"
        )

        self.input_file = InputFile(
            file_path
        )

    def test_parse_desired_language_lines(self):
        language_lines = self.extract_language.parse_desired_language_lines(self.input_file.file_contents)
        self.assertIsInstance(language_lines, list)
        self.assertIsInstance(language_lines[0], str)

    def test_extract_sub_title_fields(self):
        language_lines = self.extract_language.parse_desired_language_lines(self.input_file.file_contents)
        subtitle_fields_line_dict = self.extract_language.extract_subtitle_fields(language_lines)
        self.assertIsInstance(subtitle_fields_line_dict, dict)
        self.assertIsInstance(subtitle_fields_line_dict[1], dict)


if __name__ == '__main__':
    unittest.main()
