import click

from .generator import generate_question
from .settings import DATA, ALL_SITES

sites = '\n'.join(['{:<20}: {}'.format(*site_data) for site_data in ALL_SITES.items()])

@click.command()
@click.option('--tag', default='python', help='Search tag.')
@click.option('--site', default='stackoverflow', help='StackExchange site to search in from this list of options:\n' + sites)
def main_cli(tag, site):
    """
    Fresh Questions from Stack Exchange family for those who want to learn
    something new often
    """
    DATA['tagged'] = tag
    DATA['site'] = site
    question = generate_question(DATA)
    click.echo(question.color_format())

if __name__ == "__main__":
    main_cli()
