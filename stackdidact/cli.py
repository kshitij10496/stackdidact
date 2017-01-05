import click

from generator import generate_question
from settings import DATA


@click.command()
@click.option('--tag', default='python', help='Search tag')
def main_cli(tag):
    DATA['tagged'] = tag
    question = generate_question(DATA)
    click.echo(question.color_format())

if __name__ == "__main__":
    main_cli()
