from brotli import compress
from argparse import ArgumentParser

try:
    parser = ArgumentParser()
    parser.add_argument("--file", help="Here you put file to compress")
    try:
        parser.add_argument("--outfile", help="Filename after compression")
    except:
        pass
    arguments = parser.parse_args()
except Exception as error:
    print(error)
    exit(1)
with open(arguments.file, "rb") as data:
    bytes_from_file = data.read()
compressed_bytes = compress(bytes_from_file)
path_to_write = arguments.outfile if bool(arguments.outfile) else arguments.file
with open(path_to_write + ".br", "wb") as data:
    data.write(compressed_bytes)
