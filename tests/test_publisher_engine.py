from models.page import Page
from publisher_engine import PublisherEngine
from publishers.mock import MockPublisher


def test_publish_is_idempotent() -> None:
    root = Page("Handbook", children=[Page("Onboarding"), Page("Operations")])
    publisher = MockPublisher()
    engine = PublisherEngine(publisher)

    engine.publish(root)
    first_tree = publisher.tree.copy()
    engine.publish(root)

    assert publisher.tree == first_tree
    assert publisher.next_id == 4
