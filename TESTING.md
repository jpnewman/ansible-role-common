
# Testing

## Install Dependencies

~~~
pip install -r requirements.txt
~~~

### VirtualBox

> Mac OS X

~~~
brew cask install virtualbox
brew cask install virtualbox-extension-pack
~~~

### Vagrant

> Mac OS X

~~~
brew cask install vagrant
~~~

### Vagrant-Manager

> Mac OS X

~~~
brew cask install vagrant-manager
~~~

## Running Tests

### All Platforms

~~~
molecule test --platform=all
~~~

### Specific Platform

~~~
molecule test --platform=trusty64
molecule test --platform=xenial64
molecule test --platform=jessie64
molecule test --platform=stretch64
~~~

### Login

~~~
molecule login --host ansible-role-common-trusty64
molecule login --host ansible-role-common-xenial64
molecule login --host ansible-role-common-jessie64
molecule login --host ansible-role-common-stretch64
~~~

## Destroy, All Platforms

~~~
molecule destroy --platform=all
~~~
