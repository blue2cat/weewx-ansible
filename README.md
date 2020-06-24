# WeeWX for Ansible



Ansible playbook for setting up a server for running [weeWX](http://www.weewx.com/) software for a weather station.

All commits are tested with Tavis CI:

[![Build Status](https://travis-ci.org/blue2cat/weewx-ansible.svg?branch=master)](https://travis-ci.org/blue2cat/weewx-ansible)


### Usage
To install weeWx:
```
ansible-playbook -i hosts site.yml --user=<someuser>
```

