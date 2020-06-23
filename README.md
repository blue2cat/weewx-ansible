# WeeWX for Ansible

[![Build Status](https://travis-ci.org/blue2cat/weewx-ansible.svg?branch=master)](https://travis-ci.org/blue2cat/weewx-ansible)

Ansible playbook for setting up a server for running [weeWX](http://www.weewx.com/) software for a weather station.

This has been tested on Ubuntu:latest -- 2004

### Publish files to S3
To use the S3 upload tool, uncomment the S3 upload line in [site.yml](./site.yml). This particular configuration of weeWX will publish web files to an AWS S3 bucket running as a static website, instead of using its own web server.  It uses the [weewx-S3upload extension](https://github.com/wmadill/weewx-S3upload) together with the [s3cmd - S3 command-line tool](http://s3tools.org/s3cmd).

Because it publishes to S3 you will need an AWS account and some credentials.  These are stored in [secrets.yml](./secrets.yml) and encrypted using [ansible vault](http://docs.ansible.com/ansible/playbooks_vault.html).  You will need to provide a password to decrypt or overwrite with your own version - it has the following format:
```
---
access_key: YOUR_ACCESS_KEY
secret_key: YOUR_SECRET_KEY
```

### Usage
To be prompted for vault password each time:
```
ansible-playbook -i hosts site.yml --ask-vault-pass
```
To pick up vault password from local file:
```
ansible-playbook -i hosts site.yml --vault-password-file ~/vault_pass.txt
```

