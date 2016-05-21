# python-sphinx

Examples to have a quick reminder on how to use sphinx in a python project.

Generated doc available on [github pages](http://jbouzekri.github.io/python-sphinx/)

## Installation

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
cd doc
make html
cd _build/html
python -m SimpleHTTPServer
```

Then go to [http://localhost:8000](http://localhost:8000)

## Init sphinx doc in existing project

Install sphinx. In your virtualenv :

```
pip install sphinx
```

I assume that your project follow the standard python tree :

* package : folder with the source code of your project
* setup.py : script to trigger install
* requirements.txt : file to install dependencies thanks to pip
* ...

create a `doc` folder in the root folder and init sphinx :

```
mkdir doc
cd doc
sphinx-quickstart
```

Answers questions. This is what I use in my projects :

| Question                                                                   | Answer            |
| -------------------------------------------------------------------------- | ----------------- |
| Root path for the documentation [.]                                        | <ENTER>           |
| Separate source and build directories                                      | n                 |
| Name prefix for templates and static dir                                   | _                 |
| Project name                                                               | Your project name |
| Author name(s)                                                             | Author names      |
| Project version                                                            | 0.0.1             |
| Project release                                                            | <ENTER>           |
| Project language                                                           | en                |
| Source file suffix                                                         | .rst              |
| Name of your master document (without suffix)                              | index             |
| Do you want to use the epub builder                                        | n                 |
| autodoc: automatically insert docstrings from modules                      | y                 |
| doctest: automatically test code snippets in doctest blocks                | n                 |
| intersphinx: link between Sphinx documentation of different projects       | y                 |
| todo: write "todo" entries that can be shown or hidden on build            | y                 |
| coverage: checks for documentation coverage                                | n                 |
| imgmath: include math, rendered as PNG or SVG images                       | n                 |
| mathjax: include math, rendered in the browser by MathJax                  | n                 |
| ifconfig: conditional inclusion of content based on config values          | y                 |
| viewcode: include links to the source code of documented Python objects    | y                 |
| githubpages: create .nojekyll file to publish the document on GitHub pages | n                 |

Change these answers to match your project.

You can initiate the documentation to match your project automatically :

```
sphinx-apidoc -f -o . ../project/
```

This command assumes that the main package folder for your project is named `project`.

I like to have a clean `doctree`. So I remove all generated rst and create an empty index.rst where I put :

```
.. toctree::
   :maxdepth: 2

   module1
   package1
```

module1 references a `module1.rst` file to describe a module at the root of the main package
package1 references a `package1.rst` file to describe a package at the root of main package

Look in the doc folder of this repository to see what these file contain.

This project uses `sphinx_py3doc_enhanced_theme` theme to have a clean, light and responsive theme.

You can look into [doc/conf.py](doc/conf.py) to see the custom configuration for this project.