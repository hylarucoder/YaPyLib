# -*- encoding: UTF-8 -*-
from setuptools import Command, setup, find_packages

import io
import os
import sys
from codecs import open
from shutil import rmtree

VERSION = '0.0.1'

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except FileNotFoundError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


requires = [
    'SQLAlchemy',
    'tablib',
    'pandas',
    'psycopg2',
    'requests',
    'parsel',
    'beautifulsoup4',
    'jinja2',
    'click'
]


def read(f):
    return open(f, encoding='utf-8').read()


setup(
    name='yapylib',
    version=VERSION,
    description="常用工具类,拷贝在身边,一用好多年",
    long_description='Micheal Gardner的Py工具类,拷贝在身边,一用好多年',
    keywords='python utils terminal',
    author='twocucao',
    author_email='twocucao@gmail.com',
    url='https://github.com/twocucao/YaPyLib',
    license='MIT',
    py_modules=['yapylib'],
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'yapylib = yapylib.cli:cli'
        ]
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    cmdclass={
        'publish': PublishCommand,
    }
)

# install_requires=[
# 'requests',
# 'pycookiecheat'
# ] + (['pyobjc-core', 'pyobjc'] if 'darwin' in sys.platform else []),
