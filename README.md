# python-sphinx

Examples to have a quick reminder on how to use sphinx in a python project

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

```
sphinx-apidoc -f -o . ../project/
```