#!/bin/sh

run_tests() {
	. venv/bin/activate
	vagrant ssh-config > .vagrant/ssh-config
	testinfra --hosts=default --ssh-config=.vagrant/ssh-config tests.py
}

main() {
    run_tests
}

main
