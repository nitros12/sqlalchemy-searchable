"""
sqlalchemy-searchable
---------------------

Provides fulltext search capabilities for declarative SQLAlchemy models.
"""

from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)

setup(
    name='sqlalchemy-searchable',
    version='0.1.2',
    url='https://github.com/kvesteri/sqlalchemy-searchable',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description=(
        'Provides fulltext search capabilities for declarative SQLAlchemy'
        ' models.'
    ),
    long_description=__doc__,
    packages=['sqlalchemy_searchable'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'SQLAlchemy==0.7.8',
    ],
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
