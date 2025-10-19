# filetree_viewer/core.py
import os
import json

def get_directory_structure(root_dir: str, as_json: bool = False, show_hidden: bool = False):
    def build_tree(directory):
        tree = {"name": os.path.basename(directory), "type": "directory", "children": []}
        try:
            for item in os.listdir(directory):
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


def print_tree(structure, indent=""):
 
    if isinstance(structure, str):
        import json
        structure = json.loads(structure)

    print(f"{indent}📁 {structure['name']}")
    for child in structure.get("children", []):
        if child["type"] == "directory":
            print_tree(child, indent + "   ")
        else:
            print(f"{indent}   📄 {child['name']}")
