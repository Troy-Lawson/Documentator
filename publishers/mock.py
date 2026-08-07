from publishers.base import BasePublisher


class MockPublisher(BasePublisher):
    def __init__(self):
        self.next_id = 1
        self.tree = {}

    def connect(self):
        print("Connected to MockPublisher")

    def find_page(self, page, parent=None):
        result = self.tree.get(self._make_key(page, parent))

        if result is not None:
            print(f"FOUND {page.title} ({result['id']})")

        return result

    def create_page(self, page, parent=None):
        page_id = self.next_id
        self.next_id += 1

        print(f"CREATE {page.title} ({page_id})")

        record = {"id": page_id, "page": page}

        self.tree[self._make_key(page, parent)] = record

        return record

    def update_page(self, page, existing):
        print(f"UPDATE {page.title}")

    def _make_key(self, page, parent):
        parent_id = parent["id"] if parent else None

        return (parent_id, page.title)
