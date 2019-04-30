## okta-cmd

### Introduction
This is my usual Okta-cli, help me easy to operate okta, because okta ui is too slow..

### Use
```bash
$ pip install okta-cmd
# init okta
$ okta-cmd init --url=https://test.okta.com --token=testtoken
# add group 
$ okta-cmd add-group --name=group-test1
# add user file to group
$ okta-cmd add-user-list-to-group --file=./user_list.txt --group=aaaaaaa
# copy group users to other group
$ okta-cmd copy-group-to-other --group=aaaaaaa --othergroup=bbb
# group list
$ okta-cmd group-list
# user list
$ okta-cmd user-list
```
### Features
*  [x] add group
*  [x] add user file to group
*  [x] copy group to other group
*  [x] group list
*  [x] user list

### TODO
*  [ ] download user list file
*  [ ] download group list file
*  [ ] Delete matching users
*  [ ] Delete matching groups

### Notes
* If you have new features or questions, you can write issues