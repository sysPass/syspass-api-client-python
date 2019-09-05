import unittest

from setuptools import setup, find_packages


def client_test_suite():
    return unittest.TestLoader().discover('tests', pattern='test_*.py')


with open('README.rst', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='sysPass-API-Client-Python',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/sysPass/syspass-api-client-python.git',
    license='MIT',
    author='Rubén D.',
    author_email='nuxsmin@syspass.org',
    description='sysPass API client for Python',
    long_description=LONG_DESCRIPTION,
    install_requires=[
        'requests'
    ],
    test_suite='setup.client_test_suite',
    tests_require=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
