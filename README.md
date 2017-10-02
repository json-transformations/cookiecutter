json-transformations-cookiecutter
==============================

Recommended [cookiecutter](https://github.com/audreyr/cookiecutter) template for [json-transformations](https://github.com/json-transformations) projects.

Usage
-----

    pip install cookiecutter
    git clone https://github.com/json-transformations/json-transformations-cookiecutter.git
    cookiecutter json-transformations-cookiecutter/

You should then change the classifiers in `{{ package_name }}/setup.py` - it is assumed that the project will run on the latest versions of Python 3 only, but also consider testing for Python 2.7. Remove any classifiers that do not apply. The full list of PyPI classifiers can be found [here](https://pypi.python.org/pypi?:action=list_classifiers).

* Fill out the README.
* The LICENSE will default to the json-transformations LICENSE.
* Verify the `.travis.yml` file is accurate.

Explanation
-----------

The decisions `json-transformations-cookiecutter` makes should all be explained here.

### README

* **README should use reStructuredText format**
  This is the format used by most Python tools, is expected by [setuptools](https://setuptools.readthedocs.io), and can be used by [Sphinx](http://sphinx-doc.org/).

### Testing

* **Use [Tox](https://tox.readthedocs.io) to manage test environments**
  Tox provides isolation, runs tests across multiple Python versions, and ensures the package can be installed.
* **Uses [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test library and runner than the standard library's unittest.
