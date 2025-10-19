# filetree_viewer/setup.py
from setuptools import setup, find_packages

setup(
    name="filetree_viewer",
    version="1.0.0",
    author="Your Name",
    description="A Python package to view complete file structure from current schema",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "filetree-viewer = filetree_viewer.cli:main",
        ],
    },
    python_requires=">=3.7",
)
