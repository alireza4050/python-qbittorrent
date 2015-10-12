#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
          name = 'qbittorrent',
          version = '0.1.0',
          description = '''Python wrapper for the QBittorrent web api v3.1.x''',
          author = "Mookfist",
          author_email = "mookfist@gmail.com",
          license = 'Apache2',
          url = 'https://github.com/mookfist/python-qbittorent',
          scripts = [],
          packages = ['qbittorrent'],
          package_dir = {'qbittorrent': 'qbittorrent'},
          package_data = {'': ['README.md','LICENSE','doc']},
          include_package_data = True,
          classifiers = [
            'Development Status :: 3 - Alpha', 
            'Environment :: Console', 
            'Intended Audience :: Developers', 
            'License :: OSI Approved :: MIT', 
            'Programming Language :: Python', 
            'Programming Language :: Python :: 2', 
            'Programming Language :: Python :: 2.7'
          ],
          install_requires = [ "requests" ],
          zip_safe=True
    )