book_path = /workspaces/py4analytics
help:
# Description: A list of make targets with examples in Makefile
	@grep -F ":" Makefile | awk '!/awk/' | awk '!/Description/' | sed -e 's/://'

build:
	jupyter-book build ${book_path}

publish: build
	ghp-import -n -p -f ${book_path}/_build/html

clean:
	rm -rf ${book_path}/_build

rebuild: clean build

convert_to_sphinx:
# Convert the jupyter book to a Sphinx website
	jupyter-book config sphinx ${book_path}
	sphinx-build ${book_path} ${book_path}/_build/html -b html