import os
import sys
import unittest

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def client_test_suite():
    return unittest.TestLoader().discover('tests', pattern='test_*.py')


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['syspass_api_client']

requires = ['requests']

test_requirements = []

about = {}

with open(os.path.join(here, 'syspass_api_client', '__version__.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__url__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'syspass_api_client': 'syspass_api_client'},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    test_suite='setup.client_test_suite',
    tests_require=test_requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.5',
    project_urls={
        'Source': 'https://github.com/sysPass/syspass-api-client-python',
    },
)
