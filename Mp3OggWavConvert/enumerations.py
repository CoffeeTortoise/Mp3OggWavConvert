from enum import IntEnum
from config import MP3_FOLDER, OGG_FOLDER, WAV_FOLDER


class Formats(IntEnum):
    """Formats of audio: mp3 = 0, ogg = 1, wav = 2"""
    MP3 = 0
    OGG = 1
    WAV = 2
    

# Linked constants
FOLDERS: tuple[str, ...] = MP3_FOLDER, OGG_FOLDER, WAV_FOLDER
FORMATS: tuple[str, ...] = 'mp3', 'ogg', 'wav'