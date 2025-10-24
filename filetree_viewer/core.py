# filetree_viewer/core.py
import os
import json
# import pprint

def get_directory_structure(root_dir: str, as_json: bool = False, show_hidden: bool = False):
    """
    Recursively builds a nested dict representing the folder structure.
    """
    def build_tree(directory):
        tree = {"name": os.path.basename(directory), "type": "directory", "children": []}
        try:
            for item in os.listdir(directory):
                # print(item,"----------------->" ,directory)
                if not show_hidden and item.startswith('.'):
                    continue
                path = os.path.join(directory, item)
                if os.path.isdir(path):
                    tree["children"].append(build_tree(path))
                else:
                    tree["children"].append({"name": item, "type": "file"})
        except PermissionError:
            tree["children"].append({"name": "Permission Denied", "type": "error"})
   
        return tree

    structure = build_tree(root_dir)

    if as_json:
        return json.dumps(structure, indent=2)
    return structure


def print_tree(structure, prefix=""):
   
    if isinstance(structure, str):
        import json
        structure = json.loads(structure)

    # Print current directory/file
    connector = "└── " if prefix.endswith("└── ") else "├── "
    if structure["type"] == "directory":
        print(f"{prefix}📁 {structure['name']}")
        children = structure.get("children", [])
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            # Set new prefix for nested structure
            child_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(child, child_prefix)
    else:
        print(f"{prefix}📄 {structure['name']}")




# structure=get_directory_structure(r"C:\coding stuff\Programming_Stuff\Python_Hobby\filetree_viewer")
# pprint.pprint(structure)