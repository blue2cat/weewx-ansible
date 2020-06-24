# Ansible for Weewx

### About 
weewx-ansible is a Ansible playbook for automatically installing [weeWx](http://weewx.com) on Linux. [Take a look the Travis CI page to see all tested versions](https://travis-ci.org/github/blue2cat/weewx-ansible). 



Travis CI:

[![Build Status](https://travis-ci.org/blue2cat/weewx-ansible.svg?branch=master)](https://travis-ci.org/blue2cat/weewx-ansible)


### Usage
To install weeWx:
```
ansible-playbook -i hosts site.yml --user=<someuser>
```

