import os

import click
from pathlib import Path
import csv
import subprocess


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


@click.command()
@click.argument('file')
def cat(file):
    home = Path.joinpath(Path.home(), 'savetxt')
    filepath = Path.joinpath(home, f'{file}.csv')
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[0])


@click.command()
@click.argument('file')
def browse(file):
    home = Path.joinpath(Path.home(), 'savetxt')
    filepath = Path.joinpath(home, f'{file}.csv')
    command = f'cat {filepath} | fzf'
    result = subprocess.run(command, shell=True, capture_output=True)
    line = result.stdout.strip().decode('utf-8')
    print(get_site(line))


def get_site(row):
    return row.split('|')[1]


cli.add_command(put)
cli.add_command(cat)
cli.add_command(browse)


if __name__ == '__main__':
    cli()