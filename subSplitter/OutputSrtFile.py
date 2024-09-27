from os import path, mkdir
from datetime import datetime


class OutputSrtFile:
    def __init__(self, output_file_path: str, sub_field_line_dict: dict):
        self.output_file_path = output_file_path
        self.sub_field_line_dict = sub_field_line_dict
        self.file_contents = self.create_srt_file_contents()

    def create_srt_file_contents(self):
        file_contents = str()
        for k, v in self.sub_field_line_dict.items():
            ass_format = "%H:%M:%S.%f"
            srt_format = "%H:%M:%S,%f"
            ass_start_time = datetime.strptime(v["Start"], ass_format)
            ass_end_time = datetime.strptime(v["End"], ass_format)
            srt_start_time = datetime.strftime(ass_start_time, srt_format)[:-3]
            srt_end_time = datetime.strftime(ass_end_time, srt_format)[:-3]


            split_text = v["Text"].split("\\N")
            file_contents += f"{k}\n"
            file_contents += f"{srt_start_time} --> {srt_end_time}\n"
            file_contents += f"{v["Text"]}\n\n" if (len(split_text) == 1) else f"{split_text[0]}\n{split_text[1]}\n\n"

        return file_contents

    def save_new_srt_file(self, output_folder_name, file_number):
        output_folder_path = path.join(self.output_file_path, output_folder_name)
        if not path.exists(output_folder_path):
            mkdir(output_folder_path)

        with open(path.join(output_folder_path, f"{file_number}.srt"), 'w', encoding='utf8') as f:
            f.write(self.file_contents)
