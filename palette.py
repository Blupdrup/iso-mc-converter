# TODO: Implement crafting tables, furnaces, and jukeboxes.
BLOCK_CONVERT_DICT = {
    0:"minecraft:air",
    1:"minecraft:water",
    2:"minecraft:stone",
    3:"minecraft:grass_block",
    4:"minecraft:dirt",
    5:"minecraft:cobblestone",
    6:"minecraft:oak_planks",
    7:"minecraft:brick_block",
    8:"minecraft:wooden_slab",
    9:"minecraft:oak_log",
    10:"minecraft:oak_leaves",
    11:"minecraft:sand",
    12:"minecraft:bookshelf",
    13:"minecraft:tnt",
    14:"minecraft:netherack",
    15:"minecraft:emerald_ore",
    16:"minecraft:diamond_ore",
    17:"minecraft:sponge",
    18:"minecraft:gravel",
    19:"minecraft:mossy_cobblestone",
    20:"minecraft:coal_ore",
    21:"minecraft:iron_ore",
    22:"minecraft:bedrock",
    23:"minecraft:iron_block",
    24:"minecraft:gold_block"
}
"""
    Converts integers into minecraft IDs.\n
    Currently crafting tables, furnaces, jukeboxes are replaced by netherack, emerald ore, and diamond ore respectively,
"""


class PaletteGenerator:
    """
        Generates a palette for the nbt structure.
    """

    palette = []

    def get_palette(self):
        """
            Gets a list of all the blocks in the palette.
        """
        for a in range(25):
            self.palette.append({"Name":BLOCK_CONVERT_DICT[a]})
        return self.palette