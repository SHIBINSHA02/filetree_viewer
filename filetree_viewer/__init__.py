# filetree_viewer/__init__.py
"""
filetree_viewer
===============

A Python package for visualizing complete directory structures 
from the current working directory or a given path.

Modules:
- core: Main logic for directory traversal and structure building
- cli:  Command-line interface
- utils: Optional helper functions
"""

from .core import get_directory_structure, print_tree

__all__ = ["get_directory_structure", "print_tree"]

__version__ = "1.0.0"
__author__ = "Your Name"
