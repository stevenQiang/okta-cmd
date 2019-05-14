## okta-cmd

### Introduction
This is my usual Okta-cli, help me easy to operate okta, because okta ui is too slow..

### Basic Features
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

### Advanced Features
#### Download user list file
user-list command add three options. 
* --download: want download user list 
* --filename: file name, the default is okta_users.json 
* --filepath: file path, the default is ./ 

```bash
$ okta-cmd user-list --download
Download success. path: ./okta_users.json
$ okta-cmd user-list --download --filename=test.json
Download success. path: ./test.json
$ okta-cmd user-list --download --filename=test.json --filepath=./oktacmd
Download success. path: ./oktacmd/test.json
```
#### Download group list file
group-list command add three options. 
* --download: want download groups list 
* --filename: file name, the default is okta_groups.json 
* --filepath: file path, the default is ./ 

```bash
$ okta-cmd group-list --download
Download success. path: ./okta_groups.json
$ okta-cmd group-list --download --filename=test.json
Download success. path: ./test.json
$ okta-cmd group-list --download --filename=test.json --filepath=./oktacmd
Download success. path: ./oktacmd/test.json
```


### Features
*  [x] add group
*  [x] add user file to group
*  [x] copy group to other group
*  [x] group list
*  [x] user list
*  [x] download user list file
*  [x] download group list file

### TODO
*  [ ] Delete matching users
*  [ ] Delete matching groups

### Notes
* If you have new features or questions, you can write issues