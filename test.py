import argparse

parser = argparse.ArgumentParser(description="List directory contents")
parser.add_argument("-l", "--long", action="store_true", help="long listing format")
parser.add_argument("-F", "--format", action="store_true", help="display file type")
args = parser.parse_args()

if args.long:
    print("works")
