import ast
import re
import setuptools
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(i.req) for i in install_reqs]

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('{{cookiecutter.package_name}}/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version=version,
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=readme,

    packages=setuptools.find_packages(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    install_requires=reqs,

    extras_require={
        'colors': ['colorama'],
        'json_higlighting': ['pygments']
    },

    entry_points={
        'console_scripts': ['{{ cookiecutter.package_name }}='
                            '{{ cookiecutter.package_name }}.cli:main']
    },
)

