#!/bin/sh 
clean() {
    rm -rf venv
}
install_deps() {
    pip install virtualenv
	virtualenv venv 
	. venv/bin/activate
	pip install -r requirements.txt
}
main() {
  clean
  install_deps
}
main
