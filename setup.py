from setuptools import setup, find_packages

from pylabrobot.__version__ import __version__

long_description = open('README.md', encoding='utf-8').read()

extras_docs = [
    'sphinx_book_theme',
    'myst_nb',
    'sphinx_copybutton',
]

extras_fw = [
    'pyusb'
]

extras_http = [
    'requests',
]

extras_websockets = [
    'websockets'
]

extras_simulation = extras_websockets

extras_venus = [
    'pyhamilton'
]

extras_testing = [
    'pytest',
    'pytest-timeout',
    'requests',
    'pylint'
] + extras_simulation

extras_server = [
    'flask',
    'wtforms',
    'wtforms_json'
]

extras_all = extras_docs + extras_simulation + extras_http + extras_websockets + extras_testing + \
              extras_venus + extras_server + extras_fw

setup(
    name='PyLabRobot',
    version=__version__,
    packages=find_packages(exclude="tools"),
    description='A hardware agnostic platform for liquid handling',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    url='https://github.com/pylabrobot/pylabrobot.git',
    extras_require={
        'testing': extras_testing,
        'docs': extras_docs,
        'simulation': extras_simulation,
        'http': extras_http,
        'websockets': extras_websockets,
        'venus': extras_venus,
        'server': extras_server,
        'all': extras_all
    }
)
