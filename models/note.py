from datetime import datetime

class Note:
    def __init__(self, timestamp, author, category, text):
        self.timestamp = timestamp
        self.author = author
        self.category = category
        self.text = text

    def __str__(self):
        return (
            f"Note(timestamp={self.timestamp}, "
            f"author='{self.author}', "
            f"category='{self.category}', "
            f"text='{self.text}')"
        )
