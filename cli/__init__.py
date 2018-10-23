import click

from .cm import cm_group
from .cps import cps_command


@click.group()
def data_delivery():
    pass

data_delivery.add_command(cm_group)
data_delivery.add_command(cps_command)