import requests, json, os
from .common import *

class Okta(object):
  
  def __init__(self):
    pass
  
  def init(self, url, token):
    self.baseUrl = url
    self.apiToken = token
    self.url = url+'/api/v1'
    self.init_session()

  def test(self):
    print(self.url)

  def init_session(self):
    self.session = requests.Session()
    self.session.headers.update({
      'Content-Type':  'application/json',
      'Authorization': 'SSWS ' + self.apiToken,
    })

  def user_list(self, download=False, filePath="./", fileName="okta_user.json"):
    users = {}
    result = request_session(self.session, self.url+"/users", 'get')
    for user in result.json():
      users[user['profile']['email']] = {'id': user['id']}
    if download:
      fullPath = os.path.join(filePath, fileName)
      with open(fullPath, 'w+') as f:
        json.dump(users, f)
      print("Download success. path: {0}".format(fullPath))
    return users

  def group_list(self):
    groups = {}
    result = request_session(self.session, self.url+"/groups", 'get')
    for group in result.json():
      groups[group['profile']['name']] = {'id': group['id']}
    return groups
  
  def add_group(self, name):
    data = json.dumps({'profile': {'name': name}})
    request_session(self.session, self.url+"/groups", 'post', data=data)
    return True

  def udpate_group(self, groupId, profile):
    data = json.dumps(profile)
    request_session(self.session, self.url+"/groups/"+groupId, 'put', data=data)
    return True

  def del_group(self, groupId):
    request_session(self.session, self.url+"/groups/"+groupId, 'delete')
    return True
  
  def add_user_to_group(self, userId, groupId):
    request_session(self.session, self.url+"/groups/"+groupId+"/users/"+userId, 'put')
    return True
  
  def add_user_list_to_group(self, fileName, groupName):
    groupList = self.group_list()
    if not groupList.get(groupName):
      raise "not find group name"
    groupId = groupList[groupName]['id']
    userList = self.user_list()
    emailNotFind = []
    errors = []
    success = 0
    with open(fileName, 'r') as f:
      for i in f.read().split("\n"):
        email = i.strip()
        if not userList.get(email):
          emailNotFind.append(email)
        else:
          try:
            self.add_user_to_group(userList[email]['id'], groupId)
            success += 1
          except Exception as e:
            raise Exception("error: {0}, result: {1}".format(email, e))
    print("success: {0}, emailNotFind: {1}, errors: {2}".format(success, emailNotFind, errors))

  def copy_group_to_other(self, groupName, otherGroupName):
    groupList = self.group_list()
    if not groupList.get(groupName):
      raise "{0} not find".format(groupName)
    if not groupList.get(otherGroupName):
      raise "{0} not find".format(otherGroupName)
    r = self.session.get(self.url+"/groups/"+groupList[groupName]['id']+"/users")
    success = 0
    errors = []
    for user in r.json():
      try:
        self.add_user_to_group(user['id'], groupList[otherGroupName]['id'])
        success += 1
      except Exception as e:
        errors.append(user['profile']['email'])
    print("success: {0}, errors: {1}".format(success, errors))