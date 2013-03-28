all: install

install:
	python setup.py install
readme:
	pandoc README.md --from markdown --to rst -o README.rst
publish: readme
	python setup.py sdist register upload
