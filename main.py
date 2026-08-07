from pathlib import Path

from loaders.structure import load_structure
from publisher_engine import PublisherEngine
from publishers.mock import MockPublisher


def main():
    structure_file = Path("data/structure.yaml")

    root = load_structure(structure_file)
    publisher = MockPublisher()

    engine = PublisherEngine(publisher)

    engine.publish(root)
    engine.publish(root)


if __name__ == "__main__":
    main()
