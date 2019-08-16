import os
from setuptools import setup,find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "mysql2mongodb",
    version = "0.0.1",
    author = "Aaron Parfitt",
    author_email = "aaronparfitt123@gmail.com",
    description = ("MySQL to MongoDB Exporter"),
    license = "MIT",
    keywords = "mongodb",
    url = "http://packages.python.org/mysql2mongo",
    packages=find_packages(),
    long_description=read('README.md'),
    scripts=['scripts/mysql2mongoDB'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
    ],
)