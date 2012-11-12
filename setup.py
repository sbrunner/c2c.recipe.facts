# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

install_requires = [
    'setuptools',
    'zc.buildout',
]

# nose plugins with options set in setup.cfg cannot be in
# tests_require, they need be in setup_requires
setup_requires = [
    'nosexcover',
    'nose-progressive',
    'ipdbplugin',
    'unittest2',
]

setup(
    name='c2c.recipe.facts',
    version='0.1',
    description='Collect all puppet facter facts',
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Sysadmin',
    ],
    author='Stéphane Brunner',
    author_email='stephane.brunner@camptocamp.com',
    url='http://github.com/sbrunner/c2c.recipe.facts',
    license='BSD',
    keywords='puppet facts facter',
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    entry_points={
        "zc.buildout": [
            "default = c2c.recipe.facts:Facts",
        ]
    }
)
