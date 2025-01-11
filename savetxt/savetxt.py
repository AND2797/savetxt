import click
from pathlib import Path
import csv
import pandas as pd
import subprocess


@click.group()
def cli():
    pass


@click.command()
@click.argument('file')
@click.argument('key')
@click.argument('tags', default='')
@click.argument('value')
def put(file: str, key: str, value: str, tags=''):
    """

    :param file: filename
    :param key: key for link
    :param value: value for link
    :param tags: tags for link. eg: python:multiprocess:socket
    :return:
    """
    home = Path.joinpath(Path.home(), 'savetxt')
    header = ["key", "tags", "value"]
    Path(home).mkdir(exist_ok=True)
    filepath = Path.joinpath(home, f'{file}.csv')
    row_to_add = pd.DataFrame(columns=header, data=[[file, key, value]])
    if filepath.exists():
        row_to_add.to_csv(filepath, header=False, mode='a', index=False, sep='|')
    else:
        row_to_add.to_csv(filepath, index=None)


@click.command()
@click.argument('file')
def cat(file: str):
    home = Path.joinpath(Path.home(), 'savetxt')
    filepath = Path.joinpath(home, f'{file}.csv')
    if filepath.exists():
        data = pd.read_csv(filepath)
        print(data)


def get_site(row):
    return row.split('|')[1]


cli.add_command(put)
cli.add_command(cat)

if __name__ == '__main__':
    cli()