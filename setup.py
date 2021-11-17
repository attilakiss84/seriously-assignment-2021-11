from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='Seriously vending machine',
    version='0.0.1',
    description='Seriously home assignment task',
    long_description=readme,
    author='Attila Kiss',
    author_email='attila.kiss.84@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests'))
)
