import sys
from typing import Literal

from src import checksums, build, meta

mode: Literal["checksums", "build", "meta"]
mode = sys.argv[2]  # argv[1] 是 github token

if mode == "checksums":
    checksums.run()
elif mode == "build":
    build.run()
elif mode == "meta":
    meta.run()
