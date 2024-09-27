import argparse
import os
import glob

from ExtractLanguageSubs import ExtractLanguageSubs
from InputFile import InputFile
from OutputSrtFile import OutputSrtFile


def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-I', '--inputPath', nargs='+', help="A list of input file paths", required=True)
    parser.add_argument('-O', '--outputPath', nargs=1, help='Output location for all srt files', required=True)
    parser.add_argument('-l', '--languageId', nargs=1, help='String used that will identify required lines', required=True)

    args = parser.parse_args()
    output_path = os.path.abspath(args.outputPath[0])
    language_id = args.languageId[0]
    print(output_path, language_id)

    file_paths = list()
    for path in args.inputPath:
        file_paths += glob.glob(path)

    for i, path in enumerate(file_paths):
        path = os.path.abspath(path)

        input_file = InputFile(path)

        extract_language = ExtractLanguageSubs(language_id)
        language_lines = extract_language.parse_desired_language_lines(input_file.read_file_contents())
        line_dict = extract_language.extract_subtitle_fields(language_lines)

        output_file = OutputSrtFile(os.path.abspath(output_path), line_dict)
        output_file.save_new_srt_file(language_id, i + 1)
