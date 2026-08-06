from pathlib import Path
from publishers.mock import MockPublisher
from publisher_engine import PublisherEngine

from loaders.stucture import load_structure

def main():
    structure_file = Path("data/structure.yaml")

    root = load_structure(structure_file)
    publisher = MockPublisher()

    engine = PublisherEngine(publisher)

    engine.publish(root)
    engine.publish(root)


if __name__ == "__main__":
    main()