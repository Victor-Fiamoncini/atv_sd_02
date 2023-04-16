''' This module defines the FileHandler class '''

from os.path import join

import json

from paths import Paths

class FileHandler:
    ''' FileHandler class '''

    def save_json_as_txt(self, filename: str, content: dict) -> str:
        ''' Store the JSON input as .txt file '''

        txt_filepath = join(Paths.OUTPUT_DIRPATH, filename)

        with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
            json.dump(content, txt_file, indent=2)

            return txt_filepath
