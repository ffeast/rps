from distutils.core import setup

with open('README.txt') as file:
    long_description = file.read()

setup(name='rps',
      version='1.1',
      description='A simple requests per second (rps) counter',
      long_description=long_description,
      author='ffeast',
      author_email='ffeast@gmail.com',
      url='https://github.com/ffeast/rps',
      scripts=['rps'])
