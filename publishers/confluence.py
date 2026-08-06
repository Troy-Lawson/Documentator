from publishers.base import BasePublisher


class ConfluencePublisher(BasePublisher):

    def connect(self):
        raise NotImplementedError

    def find_page(self, page, parent=None):
        raise NotImplementedError

    def create_page(self, page, parent=None):
        raise NotImplementedError

    def update_page(self, page, existing):
        raise NotImplementedError