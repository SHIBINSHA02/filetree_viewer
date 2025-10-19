<!-- README.md -->
# filetree_viewer

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Python package and CLI tool that allows you to **visualize the complete file and folder structure** of any directory. Designed for developers, system administrators, and anyone who wants a clear overview of a project's or folder's structure.

---

## ✨ Features

- 🌳 Recursively traverse directories and display all files and folders
- 🐍 Works as a Python library or command-line tool
- 👁️ Optionally include hidden files and folders
- 📊 Multiple output formats:
  - Visually formatted tree
  - JSON for programmatic use
- 🪶 Lightweight and dependency-free (optional `rich` support for colorized output)
- 🌍 Cross-platform (Windows, Linux, macOS)

---

## 📦 Installation

### Install from source

```bash
git clone https://github.com/yourusername/filetree_viewer.git
cd filetree_viewer
pip install -e .
```

### Install from PyPI (coming soon)

```bash
pip install filetree-viewer
```

---

## 🚀 Quick Start

### Command Line Interface

After installation, use the CLI to visualize any directory:

```bash
# View current directory
filetree-viewer .

# View a specific directory
filetree-viewer /path/to/directory

# Include hidden files
filetree-viewer . --show-hidden

# Output as JSON
filetree-viewer . --json
```

### Python API

```python
from filetree_viewer import get_directory_structure, print_tree

# Get and print the directory structure
tree = get_directory_structure(".")
print_tree(tree)

# Output as JSON
json_tree = get_directory_structure(".", as_json=True)
print(json_tree)
```

---

## 📖 Usage

### CLI Options

| Option | Description |
|--------|-------------|
| `path` | Root directory to scan (default: current directory) |
| `--json` | Output structure as JSON instead of tree format |
| `--show-hidden` | Include hidden files and folders (starting with `.`) |

### Examples

```bash
# Basic usage
filetree-viewer .

# Show hidden files
filetree-viewer . --show-hidden

# Windows path with spaces
filetree-viewer "C:\Program Files\MyApp"

# Output as JSON for parsing
filetree-viewer /home/user/projects --json > structure.json
```

---

## 📋 Example Output

### Tree Format

```
📁 .
   📁 filetree_viewer
      📄 __init__.py
      📄 __main__.py
      📄 cli.py
      📄 core.py
      📄 utils.py
   📄 LICENSE
   📄 README.md
   📄 requirements.txt
   📄 setup.py
```

### JSON Format

```json
{
  "name": ".",
  "type": "directory",
  "children": [
    {
      "name": "filetree_viewer",
      "type": "directory",
      "children": [
        { "name": "__init__.py", "type": "file" },
        { "name": "__main__.py", "type": "file" },
        { "name": "cli.py", "type": "file" },
        { "name": "core.py", "type": "file" },
        { "name": "utils.py", "type": "file" }
      ]
    },
    { "name": "LICENSE", "type": "file" },
    { "name": "README.md", "type": "file" },
    { "name": "requirements.txt", "type": "file" },
    { "name": "setup.py", "type": "file" }
  ]
}
```

---

## 🛠️ Development

### Setup Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/filetree_viewer.git
   cd filetree_viewer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install in editable mode:
   ```bash
   pip install -e .
   ```

4. Run tests (if available):
   ```bash
   pytest tests/
   ```

### Project Structure

```
filetree_viewer/
├── filetree_viewer/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py          # CLI interface
│   ├── core.py         # Core logic
│   └── utils.py        # Helper functions
├── tests/
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

---

## 🎯 Future Enhancements

- [ ] Colorized tree view using `rich` library
- [ ] Export tree as Markdown or HTML
- [ ] Filter by file type (e.g., `*.py`, `*.js`)
- [ ] Limit traversal depth
- [ ] Respect `.gitignore` patterns
- [ ] Custom ignore patterns
- [ ] File size information
- [ ] Last modified timestamps
- [ ] Interactive mode

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**S Shibinsha**

- Email: shibin24888@gmail.com
- GitHub: [@SHIBINSHA02](https://github.com/SHIBINSHA02)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

## 📝 Changelog

### v1.0.0 (Initial Release)
- Basic directory tree visualization
- CLI interface
- Python API
- JSON output support
- Hidden files toggle