# WeeWX Server
Ansible playbook for setting up a server for running [weeWX](http://www.weewx.com/) software for a weather station.

I have this running on a Raspberry Pi with Raspbian Jessie - so this is the only place the playbook has been tested.

This particular configuration of weeWX will publish web files to an AWS S3 bucket running as a static website, instead of using its own web server.  It uses the [weewx-S3upload extension](https://github.com/wmadill/weewx-S3upload) together with the [s3cmd - S3 command-line tool](http://s3tools.org/s3cmd).

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

