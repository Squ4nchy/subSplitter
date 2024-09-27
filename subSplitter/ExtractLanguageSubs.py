from pprint import pprint


class ExtractLanguageSubs:
    events_format = ["Layer", "Start", "End", "Style", "Name", "MarginL", "MarginR", "MarginV", "Effect", "Text"]

    def __init__(self, language_identifier: str):
        self.language_identifier = language_identifier

    def parse_desired_language_lines(self, input_file):
        input_file_lines = input_file.splitlines()

        language_lines = list()
        # Separate out lines that match a defined value for the desired language.
        [language_lines.append(line) for line in input_file_lines if f",{self.language_identifier}," in line]

        return language_lines

    def extract_subtitle_fields(self, language_lines):
        split_language_line_list = list()
        # Split each list item into individual comma seperated values.
        [
            split_language_line_list.append(line.split(','))
            for line in language_lines
            if len(line.split(',')) == len(self.events_format)
        ]

        line_dict = dict()

        # Join comma split values into a neste dict with the "events_format" as
        # the key and the line number as the root key.
        for i, values in enumerate(split_language_line_list):
            line_dict[i + 1] = dict(zip(self.events_format, values))

        return line_dict
