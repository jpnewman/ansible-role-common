# jpnewman.common

[![Ansible Role](https://img.shields.io/ansible/role/9586.svg?maxAge=2592000)](https://galaxy.ansible.com/jpnewman/common/)
[![Build Status](https://travis-ci.org/jpnewman/ansible-role-common.svg?branch=master)](https://travis-ci.org/jpnewman/ansible-role-common)

This is a general Ansible role that: -

- Updates apt cache

- Installs the following atp packages. Can be overwritten via list variable ```apt_packages```: -

    - software-properties-common
    - python-software-properties / python3-software-properties (Stretch)
    - ntp
    - unzip
    - htop
    - vim
    - sysstat
    - nmon
    - nload
    - whois
    - sshpass
    - expect
    - traceroute
    - curl

- Updates alternative editor to vim

- Configures 'skel' bash aliases

- Updates limits

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|
|---|---|
|apt_packages|Overrides the list of the default apt packages to install|
|limits|Contains a list of 'limit' classes|

|'limit' class variables|Description|Default|
|---:|---|:---:|
|domain|Contains limits domain.|*|
|type|Contains limits type.|hard|
|item|Contains limits item.|nofile|
|value|Contains limits value.|unlimited|

**NOTES: -**
- Default apt packages are included via ```vars``` YAML files ```ansible_os_family``` and then ```ansible_lsb.codename```.  
  *e.g.* If ```apt_packages``` is not defined and the platform codename is ```Stretch```, variables from platform file ```vars/ubuntu.yml``` will be loaded and then overwritten with variables in ```vars/stretch.yml```, if it exists.
- See <http://linux.die.net/man/5/limits.conf> for more ```limits.conf``` information.

*e.g.*

```
apt_packages:
  - software-properties-common
  - python-software-properties
  - ntp
  - unzip
  - htop
  - vim

...

limits:
  - domain: '*'
    type: 'soft'
    item: 'nofile'
    value: 'unlimited'
  - domain: '*'
    type: 'hard'
    item: 'nofile'
    value: 'unlimited'
```

## Dependencies

none

## Example Playbook

    - hosts: servers
      roles:
         - { role: jpnewman.common, tags: ["init"] }

## Testing

For more information on testing the template review readme ```./tests/templates/README.md```

## License

MIT / BSD

## Author Information

John Paul Newman
