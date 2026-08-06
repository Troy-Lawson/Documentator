from abc import ABC, abstractmethod

from models.page import Page

class DocumentationProvider(ABC):

    @abstractmethod
    def connect(self) -> None:
        """Initialize and required connections"""

    @abstractmethod
    def find_page(self, title: str, parent=None):
        """REturn the provider-specific page object or None."""

    @abstractmethod
    def create_page(self, page: Page, parent=None):
        """Create a page and return the provider-specific object"""

    @abstractmethod
    def update_page(self, page: Page, existing) -> None:
        """Update an existing page"""