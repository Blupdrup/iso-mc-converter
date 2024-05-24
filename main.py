"""
I decided to make this project when I saw The Science Elf's video 'I Wrote Minecraft for a Calculator',
which you can watch here:
https://www.youtube.com/watch?v=Bj9CiMO66xk&pp=ygUZbWluZWNyYWZ0IG9uIGEgY2FsY3VsYXRvcg%3D%3D.

As I was playing around with his program, I had the idea of converting the TI-84 worlds into actual Minecraft nbt data.

To convert your calculator worlds into Minecraft nbt structures, connect your calculator to your computer with a USB cable and open a TI-84 file transfer program of your choice.

After you opened your program of choice, find the 16 world data AppVars for the world you want to convert (A,B,C,D, or ,E).
Each world saved on the calculator is split into 16 horizontal slices to save memory.
For example, WORLDA will have 16 different AppVars:
WORLDA00,
WORLDA01,
WORLDA02,
...
WORLDA15

There will be an extra file that will not have any numbers after its name;
this file contains information that we don't need and you don't have to transfer this file.
Transfer the files to a new folder on your computer.
(The name of this folder doesn't matter)

After transferring the files to your computer, 
use this program
"""


from settings import *
from palette import *
from folder import *

from nbtlib import schema
from nbtlib.tag import *
import nbtlib
from gzip import *

Structure = schema('Structure', {
        'DataVersion': Int,
        'author': String,
        'size': List[Int],
        'palette': List[schema('State', {
            'Name': String,
            'Properties': Compound,
        })],
        'blocks': List[schema('Block', {
            'state': Int,
            'pos': List[Int],
            'nbt': Compound,
        })],
        'entities': List[schema('Entity', {
            'pos': List[Double],
            'blockPos': List[Int],
            'nbt': Compound,
        })],
    })
"""
    The nbtlib compound tag schema for a structure.\n
    This schema makes it much easier to generate nbt structures.
"""


class StructureFile(nbtlib.nbt.File, Structure):
    def __init__(self, structure_data=None):
        super().__init__(structure_data or {})
        self.gzipped = True
    @classmethod
    def load(cls, filename, gzipped=True):
        return super().load(filename, gzipped)



def prompt():
    """
        Prompts the user for load and save directories.\n
        Returns a tuple structured like this : (`Load Directory`, `Save Directory`).
    """
    load = input("Folder directory to load from: ")
    save = input("File directory to save to: ")
    load = load.lstrip("\"")
    load = load.rstrip("\"")
    save = save.lstrip("\"")
    save = save.rstrip("\"")
    return (load, save)




def readFileData(inputData: bytes, readOffset: int):
    """
        Reads only the variable data from the raw byte data `inputData` with a `readOffset`.\n
        The last two bytes in a .8xv file are a checksum and are not needed.
    """
    outputData = []
    for a in range(len(inputData)-readOffset-2):
        outputData.append(read(inputData, readOffset+a))
    return outputData


def readWorldData(dir: str):
    """
        Reads all of the world data in a folder specified by `dir`.\n
        `dir` must be a raw string.\n
        The folder should contain `WORLD00` to `WORLD15`,
        but it should NOT contain `WORLD`.
        That file contains data that is not needed for this project.
    """
    world = []
    dec = openFolder(dir)
    for a in range(len(dec)):
        data = dec[a]
        world.append(readFileData(data, READ_OFFSET))

    return world


def writeNBT(loadDir: str, saveDir: str):
    """
        Loads the calculator world from `loadDir` and saves the nbt data to `saveDir`.
        Both directories need to be raw strings.
    """
    DataVersion = 2865
    size = [48,16,48]
    paletteGenerator = PaletteGenerator()
    palette = paletteGenerator.get_palette()
    world = readWorldData(loadDir)
    blocks = []
    for a in world:
        for b in range(len(a)):
            block = {}
            block.update({"state":a[b]})
            block.update({"pos":[Int(b%48), Int(world.index(a)), Int(b//48)]})
            blocks.append(block)

    nbtStructure = Structure({
        'DataVersion': DataVersion,
        'size': size,
        'palette': palette,
        'blocks': blocks,
        'entities': [],
    })
    structure_file = StructureFile(nbtStructure)
    structure_file.save(saveDir)




if __name__ == "__main__":
    loadDir, saveDir = prompt()
    writeNBT(loadDir, saveDir)