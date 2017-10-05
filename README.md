### Sample vagrant Env for a nodejs app using mysql and memcached

This environment will be setup using ansible , and integration testing is done using testinfra python module.

[testinfra](http://testinfra.readthedocs.io/)
[ansible](https://www.ansible.com/)

## Setup
This command will install the required dependencies for integration testing
* make deps

## Running tests
*  make
*  make test
