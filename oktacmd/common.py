import json, os
import requests

CONFIG_FILE = "{0}/.okta_cmd".format(os.getenv("HOME"))
REQUIRED_LIST = ['url', 'token']

def get_config():
  with open(CONFIG_FILE) as f:
    data = json.load(f)
    check_config(data)
    return data

def set_config(data):
  with open(CONFIG_FILE, 'w+') as f:
    json.dump(data, f)

def check_config(data):
  for name in REQUIRED_LIST:
    if not data.get(name):
      raise Exception("Config File missing parameter: {0}, Please use the init command to initialize".format(name))

def request_session(session, url, method, **kwargs):
  result = getattr(session, method)(url, **kwargs)
  if result.status_code >= 400:
    raise requests.HTTPError(json.dumps(result.json()))
  return result
