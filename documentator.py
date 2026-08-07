from datetime import datetime

import click

# Custom classes
from models.note import Note
from storage.markdown import MarkdownStorage


@click.group()
def cli():
    pass


@cli.command()
@click.option("-o", "--observation")
def note(observation):

    note = Note(
        timestamp=datetime.now().astimezone(),
        author="Troy",  # TODO: replace this with a config variable somehow
        category="Observation",
        text=observation,
    )

    markdown = MarkdownStorage()  # handles markdown releated actions

    markdown.save(note)

    # print("\n test read \n")

    # storage.read(note)


if __name__ == "__main__":
    cli()
