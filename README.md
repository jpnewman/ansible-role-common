# jpnewman.common

This is a general Ansible role, currently only developed for **Ubuntu**, that: -

- Updates apt cache

- Installs the following atp packages: -

    - software-properties-common
    - python-software-properties
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

- Update alternative editor to vim

- Configures 'skel' bash aliases

- Updates limits

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|
|---|---|
|apt_packages|Contains a list for apt packages to install|
|limits|Contains a list of 'limit' classes|

|'limit' class variables|Description|Default|
|---:|---|:---:|
|domain|Contains limits domain.|*|
|type|Contains limits type.|hard|
|item|Contains limits item.|nofile|
|value|Contains limits value.|unlimited|

**NOTE:** See [http://linux.die.net/man/5/limits.conf]() for more ```limits.conf``` information

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
