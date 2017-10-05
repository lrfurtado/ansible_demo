#!/bin/sh

run_tests() {
	vagrant ssh-config > .vagrant/ssh-config
	testinfra --hosts=default --ssh-config=.vagrant/ssh-config tests.py
}

main() {
    run_tests
}

main
