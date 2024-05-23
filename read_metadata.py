from collections import namedtuple
import struct

"""
Even though I don't need it for this project, I thought it would be cool to read the metadata from a .8xv file.
I don't think it works.
Info about Ti-84/Ti-83 metadata:
http://merthsoft.com/linkguide/ti83+/fformat.html
"""
FIELDS = [
    (None, "="),
    ("sig", "8s"),
    ("furtherSig", "3s"),
    ("comment", "42s"),
    (None, "6x"),
    ("name", "9s")
]

FILE_HEADER = "".join(format_type for _, format_type in FIELDS)

FileMetadata = namedtuple(
    "FileMetadata",
    [field_name for field_name, _ in FIELDS if field_name is not None],
)

def readMetadata(data, offset=0):
    metadata = []
    metadata = struct.unpack_from(FILE_HEADER, data, offset=offset)
    return FileMetadata._make(metadata)