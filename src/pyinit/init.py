#!/usr/bin/python
#coding=utf-8

import os
import config
from datetime import date


if __name__ == '__main__':
    project = config.PROJECT
    if project.isalnum():
        dir = '%s/%s' % ('.', project)
        try:
            os.mkdir(dir)
        except Exception, e:
            print e
        os.chdir(dir)
        open('setup.py', 'w').write(config.SETUP)
        open('requirements.txt', 'w').write(config.REQUIREMENTS)
        open('LICENSES.txt', 'w').write(config.LICENSES_DETAIL)
        pubdate = str(date.today())
        open('ChangeLog.txt', 'w').write(config.ChangeLog % (
            project, pubdate))
        open('MANIFEST.in', 'w').write(config.MANIFEST)
        if not os.path.isdir('test'):
            os.mkdir('test')
        open('test/test_%s.py' % project, 'w').write(
            config.test_project % (project, project), )
        open('test/run_all_test.sh', 'w').write(config.run_all_test)
        if not os.path.isdir('docs'):
            os.mkdir('docs')
        if not os.path.isdir('src'):
            os.mkdir('src')
        if not os.path.isdir('src/%s' % project):
            os.mkdir('src/%s' % project)
        open('src/%s/__init__.py' % project, 'w').write('')
        open('src/%s/stuff' % project, 'w').write('')
    else:
        print '''Project name must be letters '''\
              '''or numbers and could not start with numbers'''
