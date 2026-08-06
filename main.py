from pathlib import Path

from loaders.stucture import load_structure

def main():
    structure_file = Path("data/structure.yaml")

    root = load_structure(structure_file)

    print(root)


if __name__ == "__main__":
    main()