import argparse
import json
parser = argparse.ArgumentParser()

parser.add_argument('-v', '--version', help="version number")
args = parser.parse_args()
print(args)
version_json = {
                "version": str(args.version)
                }

with open("version.json", "w") as outfile:
    json.dump(version_json, outfile)