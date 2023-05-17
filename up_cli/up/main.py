import click

from up_lib.up_lib import hello_world_from_init
from up_lib.up_lib.up_lib import hello_world_from_lib


@click.command(name="up")
def main():
    click.echo(hello_world_from_init())
    click.echo(hello_world_from_lib())


if __name__ == '__main__':
    main()
