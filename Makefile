.PHONY: deps
all: 
	vagrant up

deps:
	./installdeps.sh

test:
	./runtests.sh
