help:
# Description: A list of make targets with examples in Makefile
	@grep -F ":" Makefile | awk '!/awk/' | awk '!/Description/' | sed -e 's/://'

build:
	jupyter-book build /workspaces/PythonBook/Py4Analytics/

publish: build
	ghp-import -n -p -f /workspaces/PythonBook/Py4Analytics/_build/html