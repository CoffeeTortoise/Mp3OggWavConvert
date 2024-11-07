from pydub import AudioSegment
from typing import Any
import os
from enumerations import Formats, FORMATS, FOLDERS


class AudioConverter:
    def __init__(self) -> None:
        self.inp: int = Formats.MP3
        self.out: int = Formats.OGG
    
    def convert(self) -> None:
        if self.inp == self.out:
            return
        inp_folder: str = FOLDERS[self.inp]
        out_folder: str = FOLDERS[self.out]
        for file in os.listdir(inp_folder):
            if not file.endswith(FORMATS[self.inp]):
                continue
            out: str = file.replace(FORMATS[self.inp], FORMATS[self.out])
            out_file: str = f'{out_folder}/{out}'
            inp_file: str = f'{inp_folder}/{file}'
            source_file: Any = AudioSegment.from_file(inp_file, format=FORMATS[self.inp])
            source_file.export(out_file, format=FORMATS[self.out])
