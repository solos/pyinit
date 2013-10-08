

PROJECT = raw_input('Please enter the name of project: ') or 'pyinit'
DESCRIPTION = raw_input('Please enter the description of the project: ') \
    or "A python empty project"
AUTHOR = 'solos'
EMAIL = 'solos@solos.so'
LICENSES = 'MIT'
LICENSES_DETAIL = ''
URL = 'https://github.com/%s/%s' % (AUTHOR, PROJECT)
PLATFORMS = ['any']
MANIFEST = '''include ChangeLog.txt LICENES.txt README.md requirements.txt
recursive-include test *.py *.sh
recursive-include docs *.md
'''
REQUIREMENTS = '\n'.join([])
README = '''
# %s

## about

''' % PROJECT

SETUP = '''
#!/usr/bin/python
#coding=utf-8

import sys
sys.path.append('./src')

from distutils.core import setup
from %s import __version__

setup(name='%s',
      version=__version__,
      description='%s',
      long_description=open('README.md').read(),
      author='%s',
      author_email='%s',
      packages=['%s'],
      package_dir={'%s': 'src/%s'},
      package_data={'%s': ['stuff']},
      license='%s',
      platforms=%s,
      url='%s')
''' % (PROJECT,
       PROJECT,
       DESCRIPTION,
       AUTHOR,
       EMAIL,
       PROJECT,
       PROJECT,
       PROJECT,
       PROJECT,
       LICENSES,
       PLATFORMS,
       URL)

test_project = """
# -*- coding:utf-8 -*-

import sys
sys.path.append('../src/')

import %s
import unittest


class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version(self):
        self.assertIsNotNone(%s.__version__, '0.0.1')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_version'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
"""
ChangeLog = """# %s changelog

## %s

* First public version.
"""

run_all_test = """python -m unittest discover -s ./ -p 'test_*.py' -v\n"""
