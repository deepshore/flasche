import click


@click.group()
def main():
    pass


@main.command()
@click.argument('name')
def add(name):
    click.echo("add {n}".format(n=name))


@main.command()
@click.argument('name')
def init(name):
    click.echo("init {n}".format(n=name))
