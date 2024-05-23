from pathlib import Path
import os
import sys

def openFolder(folderDir: str):
        """
            Gets all of the byte data of all the files in a folder specified by `folderDir`.\n
            `folderDir` must be a raw string.
        """
        a = []
        for root, dirs, files in os.walk(folderDir, topdown=False):
            for name in files:
                a.append(Path(os.path.join(root, name)).read_bytes())
        return a


def read(inputData: bytes, address: int, count: int = 1):
        """
        Reads `count` bytes starting from `address`.
        """
        if 0 <= address + count <= len(inputData):
            v = inputData[address : address + count]
            return int.from_bytes(v, sys.byteorder)
        else:
            raise IndexError(f'{address=}+{count=} is out of range')