#!/usr/bin/env python3
# Audio Helper
# This script is used to help with audio files.
# For now, it'll convert ogg files to mp3 files,
# and fix metadata for mp3 files.

import os
import sys
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.oggvorbis import OggVorbis
from mutagen.mp3 import MP3
from pydub import AudioSegment


class AudioHelper:
    """Audio Helper.
    Handles mp3 and ogg files.
    """

    def __init__(self, path):
        self._path = path
