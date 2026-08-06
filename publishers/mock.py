from publishers.base import BasePublisher

class MockPublisher(BasePublisher):

    def __init__(self):
        self.next_id = 1

    def connect(self):
        print("Connected to MockPublisher")

    def find_page(self, title, parent=None):
        return None

    def create_page(self, page, parent=None):
        page_id = self.next_id
        self.next_id += 1

        print(f"CREATE {page.title} ({page_id})")

        return page_id

    def update_page(self, page, existing):
        print(f"UPDATE {page.title}")