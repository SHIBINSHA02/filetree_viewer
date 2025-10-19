# filetree_viewer/cli.py
import argparse
from .core import get_directory_structure, print_tree

def main():
    parser = argparse.ArgumentParser(description="Display full file structure of a directory.")
    parser.add_argument("path", nargs="?", default=".", help="Root directory path (default: current directory)")
    parser.add_argument("--json", action="store_true", help="Output structure as JSON")
    parser.add_argument("--show-hidden", action="store_true", help="Include hidden files/folders")

    args = parser.parse_args()

    structure = get_directory_structure(args.path, as_json=args.json, show_hidden=args.show_hidden)

    if args.json:
        print(structure)
    else:
        print_tree(structure)

if __name__ == "__main__":
    main()
