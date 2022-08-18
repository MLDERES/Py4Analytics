## Structure

* _build - represents the HTML files that will be deployed (currently using the ghp_pages branch)
* book - represents the actual contents of the Jupyter book
* book/lessons - this is where the content chapters go.
* book/extras - a placeholder for lessons and exercises that haven't been integrated yet
* book/src - python files that are supporting the notebooks
* book/exercises - exercise or coding opportunities associated with each chapter
* book/data - data used in the notebooks
* book/img - any image files used in the chapters or notebooks

## Building the book
To "build" the book, that is turn the contents into static HTML, use the `make build` command, assuming you are running in the container.  This will compile the content into the _build folder. You can then view/test the content by opening the `_build\html` folder in a browser or double-clicking the `_build\html\intro.hmtl` file.

## Deploying the book
Deploying the book means ensuring that the book is available at the given endpoint.  This is done with the `make publish` command.