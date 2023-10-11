# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['up_splat']

package_data = \
{'': ['*']}

install_requires = \
['pluggy>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'up-splat',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Julio Faerman',
    'author_email': 'jufaerma@redhat.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.12,<4.0',
}


setup(**setup_kwargs)

