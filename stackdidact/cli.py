import click

from .settings import QUERY_PARAMS
from .generator import generate_question, open_in_browser


@click.command()
@click.option('--tag', default='python', help='Search tag.')
@click.option('--browse', default=None, help='Browser to view questions.')
@click.option('--site', default='stackoverflow',
              help='StackExchange site to search in.')
def main_cli(tag, browse, site):
    """
    Fresh Questions from Stack Exchange family for those who want to learn
    something new often
    """
    QUERY_PARAMS['tagged'] = tag
    QUERY_PARAMS['site'] = site
    question = generate_question(QUERY_PARAMS)
    click.echo(question.color_format())
    if browse:
        open_in_browser(question.link)


if __name__ == "__main__":
    main_cli()
