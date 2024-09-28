import os
from datetime import *

stats = os.stat("abc.txt")
print("The size of file in bytes is:",stats.st_size)
print("File last modified time", datetime.fromtimestamp(stats.st_mtime))
print("File last accessed time",datetime.fromtimestamp(stats.st_atime))


