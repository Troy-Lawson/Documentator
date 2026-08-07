import os
from datetime import datetime


class MarkdownStorage:
    def save(self, note):

        # grab the date for use as document title
        date = datetime.now().astimezone().strftime("%Y-%m-%d")

        # daily note so file name is simply date
        filename = date + ".md"

        os.makedirs("notes", exist_ok=True)
        filepath = os.path.join("notes", filename)

        with open(filepath, "a") as f:
            f.write(f"# [{date}]\n\n")
            f.write(f"## {note.category}\n")
            f.write(f"- {note.text}\n\n")

    def read(self, note):
        print(note)
