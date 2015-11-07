# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

install_requires = [
    'minion-backend'
]

setup(name='minion-nessus-plugin',
      version='0.1',
      description='Nessus Plugin for Minion',
      url='https://github.com/18F/minion-nessus-plugin/',
      author='David Best',
      author_email='david.best@gsa.gov',
      packages=['minion', 'minion.plugins'],
      namespace_packages=['minion', 'minion.plugins'],
      zip_safe = True,
      include_package_data=True,
      install_requires = install_requires)
