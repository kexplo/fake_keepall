# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='fake-keepall',
    version='0.1.2',
    description='Apply the fake `word-break: keep-all;` CSS property to static HTML file',
    python_requires='==3.*',
    project_urls={"repository": "https://github.com/kexplo/fake_keepall"},
    author='Chanwoong Kim',
    author_email='me@chanwoong.kim',
    license='MIT',
    classifiers=[
        'Environment :: Console', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3', 'Topic :: Text Processing'
    ],
    entry_points={
        "console_scripts": ["fake-keepall = fake_keepall.__init__:cli"]
    },
    packages=['fake_keepall'],
    package_dir={"": "."},
    package_data={},
    install_requires=['beautifulsoup4==4.*,>=4.9.1', 'click==7.*,>=7.1.2'],
    extras_require={
        "dev": [
            "flake8==3.*,>=3.8.2", "flake8-import-order==0.*,>=0.18.1",
            "pyflakes==2.*,>=2.2.0", "pytest==5.*,>=5.4.3"
        ]
    },
)
