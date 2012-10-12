# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='tiket',
    version='0.1',
    author='Gilang Chandrasa',
    author_email='gilang@chandrasa.com',
    packages=['tiket'],
    url='https://github.com/gchandrasa/tiket',
    license='MIT',
    description='Tiket.com API Wrapper',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data = { '': ['README.rst'] },
    install_requires=['requests',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)