
from models.page import Page

class PublisherEngine:

    def __init__(self, publisher):
        self.publisher = publisher

    def publish(self, root):
        self.publisher.connect()
        self._publish_page(root, None)

    def _publish_page(self, page: Page, parent=None) -> None:

        provider_page = self.publisher.find_page(page, parent)

        if provider_page is None:
            provider_page = self.publisher.create_page(page, parent)

        for child in page.children:
            self._publish_page(child, provider_page)