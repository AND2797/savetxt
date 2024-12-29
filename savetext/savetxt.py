import click
from pathlib import Path
import csv


@click.group()
def cli():
    pass


@click.command()
@click.argument('file')
@click.argument('key')
@click.argument('value')
@click.argument('tags', default='')
def put(file, key, value, tags=''):
    home = Path.joinpath(Path.home(), 'savetxt')
    Path(home).mkdir(exist_ok=True)
    filepath = Path.joinpath(home, f'{file}.csv')
    with open(filepath, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow([key, value, tags])


cli.add_command(put)


if __name__ == '__main__':
    cli()