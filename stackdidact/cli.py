import click

from generator import generate_question, colorize, open_in_browser
from settings import QUERY_PARAMS, USER_AGENT

@click.command()
@click.option('--tag', default='python', help='Search tag')
def main_cli(tag):
    """
        Stackdidact - Learn new stuff from stack overflow everyday
    """
    QUERY_PARAMS['tagged'] = tag
    question = generate_question(QUERY_PARAMS)
    click.echo(colorize(question))
    open_in_browser(USER_AGENT, question.link)

if __name__ == "__main__":
    main_cli()
