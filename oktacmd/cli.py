import click
from .okta import Okta
from .common import *

@click.group()
@click.pass_context
def main_cli(ctx):
  if ctx.invoked_subcommand not in ['init', 'auth']:
    okta = Okta()
    config_data = get_config()
    okta.init(config_data['url'], config_data['token'])
    ctx.obj = okta
    
@main_cli.command()
@click.option('--url', required=True)
@click.option('--token', required=True)
@click.pass_obj
def init(ctx, url, token):
  set_config({'url': url, 'token': token})
  print('done.')

@main_cli.command()
@click.pass_obj
def auth(ctx):
  print('Steven Love Tina')

@main_cli.command()
@click.option('--download', is_flag=True)
@click.option('--filepath', default='./')
@click.option('--filename', default='okta_user.json')
@click.pass_obj
def user_list(okta, download, filepath, filename):
  res = okta.user_list(download, filepath, filename)
  if not download:
    print(res)

@main_cli.command()
@click.pass_obj
def group_list(okta):
  print(okta.group_list())

@main_cli.command()
@click.option('--name', required=True)
@click.pass_obj
def add_group(okta, name):
  print(okta.add_group(name))

@main_cli.command()
@click.option('--file', required=True)
@click.option('--group', required=True)
@click.pass_obj
def add_user_list_to_group(okta, file, group):
  okta.add_user_list_to_group(file, group)

@main_cli.command()
@click.option('--group', required=True)
@click.option('--othergroup', required=True)
@click.pass_obj
def copy_group_to_other(okta, group, othergroup):
  okta.copy_group_to_other(group, othergroup)
