import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Flask-ContentBlocks',
    version='1.0',
    url='http://github.com/brainfire/flask-contentblocks',
    license='BSD',
    author='Zakaria Zajac',
    author_email='zak@brainfi.re',
    description='A lite CMS extension for flask focusing\
				on delivering content to created blocks on the page',
    long_description=read('README.md'),
    packages=['flask_contentblocks'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'Flask-SQLAlchemy>=0.16'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)