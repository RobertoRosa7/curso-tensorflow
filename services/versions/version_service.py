# -*- coding: utf-8 -*-
import os

from keys.generate_key import GenerateKey as key

MAX_VERSION = 9
ZERO = 0
ONE = 1
dir = os.path.join(os.getcwd(), 'storage')


class VersionService:
    def get_version(self, file: list):
        find_last = file[-1]
        get_versions = find_last.split('.')

        major, minor, patch = get_versions[1:-1]
        return [int(major), int(minor), int(patch)]

    def inc_version(self, files: list, filename: str, ext: str) -> str:
        major, minor, patch = self.get_version(files)

        if int(patch) == MAX_VERSION:
            patch = ZERO
            if minor == MAX_VERSION:
                minor = ZERO
                major = major + ONE
            else:
                minor = minor + ONE
        else:
            patch = patch + ONE

        return '{}.{}.{}.{}.{}'.format(filename, major, minor, patch, ext)

    def get_last_version(self, filename: str, ext: str = key.EXT_TXT, path: str = dir) -> str:
        return self.find(filename, ext, path)[-1]

    def get_next_version(self, filename: str = key.FILENAME_DEFAULT, ext: str = key.EXT_TXT, path: str = dir) -> str:
        return self.find_one(filename, ext, path)

    def find(self, filename: str, ext: str, path: str):
        return list(
            filter(lambda file: file.startswith(filename) and file.endswith(ext), os.listdir(path)))

    def find_one(self, filename: str, ext: str, path: str) -> str:
        files = self.find(filename, ext, path)

        if not files:
            files = ['{}.{}.{}'.format(filename, key.VERSION_DEFAULT, ext)]

        return self.inc_version(files, filename, ext)
