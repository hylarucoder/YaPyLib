# -*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(name='yapylib',
      version=VERSION,
      description="常用工具类,拷贝在身边,一用好多年",
      long_description='Micheal Gardner的Py工具类,拷贝在身边,一用好多年',
      classifiers=["Topic :: Utilities"],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python utils terminal',
      author='twocucao',
      author_email='twocucao@gmail.com',
      url='https://github.com/twocucao/YaPyLib',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'requests',
          'parsel',
          'beautifulsoup4',
          'jinja2',
          'click'
      ],
      entry_points={
          'console_scripts': [
              'yapylib = yapylib.cli:cli'
          ]
      },
      )

# install_requires=[
# 'requests',
# 'pycookiecheat'
# ] + (['pyobjc-core', 'pyobjc'] if 'darwin' in sys.platform else []),
