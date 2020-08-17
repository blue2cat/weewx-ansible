# Ansible for Weewx
[![Build Status](https://travis-ci.org/blue2cat/weewx-ansible.svg?branch=master)](https://travis-ci.org/blue2cat/weewx-ansible)

### About 
`weewx-ansible` is a Ansible playbook for automatically installing [WeeWx](http://weewx.com) on Linux. [Take a look the Travis CI page to see all tested versions](https://travis-ci.org/github/blue2cat/weewx-ansible). 


### Usage

#### Create a Hosts File for Ansible Automation

```
> sudo nano hosts.txt
```

```
#hosts.txt
[weewx]
172.17.122.80 ansible_user=<user> ansible_ssh_private_key_file=~/.ssh/id_rsa ansible_become=yes
```

#### Run the Ansible Playbook

```
> ansible-playbook -i hosts site.yml --user=<someuser>
```

