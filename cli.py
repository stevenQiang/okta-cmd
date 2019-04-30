import click
from okta import Okta
from common import *

@click.group()
@click.pass_context
def cli(ctx):
  if ctx.invoked_subcommand != 'init':
    okta = Okta()
    config_data = get_config()
    okta.init(config_data['url'], config_data['token'])
    ctx.obj = okta
    
@cli.command()
@click.option('--url', required=True)
@click.option('--token', required=True)
@click.pass_obj
def init(ctx, url, token):
  set_config({'url': url, 'token': token})
  print('done.')

@cli.command()
@click.pass_obj
def user_list(okta):
  print(okta.user_list())

@cli.command()
@click.pass_obj
def group_list(okta):
  print(okta.group_list())

@cli.command()
@click.option('--name', required=True)
@click.pass_obj
def add_group(okta, name):
  print(okta.add_group(name))

@cli.command()
@click.option('--file')
@click.option('--group')
@click.pass_obj
def add_user_list_to_group(okta, file, group):
  okta.add_user_list_to_group(file, group)

@cli.command()
@click.option('--group')
@click.option('--othergroup')
@click.pass_obj
def copy_group_to_other(okta, group, othergroup):
  okta.copy_group_to_other(group, othergroup)

cli()
