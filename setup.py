#!/usr/bin/env python
import pypandoc
from setuptools import setup

readme = pypandoc.convert('README.md', 'rst')

with open('LICENSE') as f:
    license = f.read()

setup(
    name='falcon-openapi',
    python_requires='>3.5.0',
    version='0.1.4',
    description='Falcon router to map openapi spec to resources',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Sam Kleiner',
    author_email='sam@skleiner.com',
    license=license,
    url='https://github.com/StoicPerlman/falcon-openapi/',
    download_url = 'https://github.com/StoicPerlman/falcon-openapi/archive/0.1.4.tar.gz',
    keywords = ['falcon', 'openapi', 'api'],
    packages=['falcon_openapi'],
    install_requires=[
        'falcon',
        'pyyaml'
    ],
    extras_require={
        'dev': [
            'unittest'
        ]
    }
)
