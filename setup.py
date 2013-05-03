#!/usr/bin/env python2

from distutils.core import setup

setup(
	name='mifare-view-dump',
	version='0.0.1',
	license='GPL',
	description='Mifare Classic Dump Viewer',
	author='Dominik Heidler',
	author_email='dheidler@gmail.com',
	url='http://github.com/asdil12/mifare-view-dump',
	scripts=['mifare-view-dump'],
	requires=['texttable'],
)
