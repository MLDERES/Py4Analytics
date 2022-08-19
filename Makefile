help:
# Description: A list of make targets with examples in Makefile
	@grep -F ":" Makefile | awk '!/awk/' | awk '!/Description/' | sed -e 's/://'

build:
	jupyter-book build /workspaces/py4analytics

publish: build
	ghp-import -n -p -f /workspaces/py4analytics/_build/html

clean:
	rm -rf /workspaces/py4analytics/_build

rebuild: clean build