from abc import ABC, abstractmethod

from models.page import Page

class DocumentationProvider(ABC):

    @abstractmethod
    def find_page(self, title: str, parent) -> object | None:
        ...

    @abstractmethod
    def create_page(self, page: Page, parent) -> object:
        ...