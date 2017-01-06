import click

from .settings import QUERY_PARAMS
from .generator import generate_question, open_in_browser


@click.command()
@click.option('--tag', default='python', help='Search tag')
@click.option('--browser', default=None, help='Browser to view questions')
def main_cli(tag, browser):
    """
        Stackdidact - Learn new stuff from stack overflow everyday
    """
    QUERY_PARAMS['tagged'] = tag
    question = generate_question(QUERY_PARAMS)
    click.echo(question.color_format())
    if browser:
	    open_in_browser(question.link)


if __name__ == "__main__":
    main_cli()
