# -*- coding: utf-8 -*-

from __future__ import print_function
import click
from ckanext.heroslideradmin.db import init as db_setup


@click.group()
def heroslideradmin():
    '''heroslideradmin commands
    '''
    pass


@heroslideradmin.command()
def initdb():
    '''
        heroslideradmin initdb
    '''
    db_setup()
    print('DB tables created')


def get_commands():
    return [heroslideradmin]
