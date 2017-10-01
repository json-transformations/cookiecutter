import setuptools

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    install_requires=['jsoncut',
                      'click',
    ],

    extras_require={
        'colors': ['colorama'],
        'json_higlighting': ['pygments']
    },

    entry_points={
        'console_scripts': ['{{ cookiecutter.package_name }}='
                            '{{ cookiecutter.package_name }}.cli:main']
    },
)

