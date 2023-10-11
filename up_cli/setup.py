# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['up_cli']

package_data = \
{'': ['*']}

install_requires = \
['pluggy>=1.3.0,<2.0.0']

entry_points = \
{'console_scripts': ['up = up_cli.main:main']}

setup_kwargs = {
    'name': 'up',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Julio Faerman',
    'author_email': 'jufaerma@redhat.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)

