import click

from up_lib.up_lib import hello_world_from_lib


@click.group(name="up")
def main():
    click.echo("main")


@main.command()
def copy():
    click.echo("copy")


@main.command()
def expect():
    click.echo("expect")


@main.command()
def copy():
    click.echo("copy")


@main.command()
def install():
    click.echo("install")


@main.command()
def template():
    click.echo("template")


@main.command()
def wait():
    click.echo("wait")


if __name__ == '__main__':
    main()
