import os
from datetime import datetime

class MarkdownStorage:

    def save(self, note):
        
        #grab the date for use as document title
        date = datetime.now().strftime("%Y-%m-%d")
        
        # daily note so file name is simply date
        filename = date +".md"

        os.makedirs("notes", exist_ok=True)
        filepath = os.path.join("notes", filename)
        
        with open(filepath, "a") as f:
            f.write("# [{}]\n\n".format(date))
            f.write("## {}\n".format(note.category))
            f.write("- {}\n\n".format(note.text))

    def read(self, note):
        print(note)
