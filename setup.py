
#!/usr/bin/python
#coding=utf-8
sys.path.append('./src')
from distutils.core import setup
from pyinit import __version__
setup(name='pyinit',
      version=__version__,
      description='A python empty project',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      packages=['pyinit'],
      package_dir={'pyinit': 'src/pyinit'},
      package_data={'pyinit': ['stuff']},
      license='BSD',
      platforms=['any'],
      url='https://github.com/solos/pyinit')
