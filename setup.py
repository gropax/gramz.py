try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Grammar transformations',
    'author': 'Maxime Laudrin',
    #'url': 'URL to get it at.',
    #'download_url': 'Where to download it.',
    'author_email': 'maximedelaudrin@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['gramz'],
    'scripts': [],
    'name': 'gramz'
}

setup(**config)
