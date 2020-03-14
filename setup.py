#!/usr/bin/env python
#
# Copyright © 2012 - 2019 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os

from setuptools import setup
from setuptools.command.sdist import sdist

from babel.messages import frontend as babel

with open("requirements.txt") as requirements:
    REQUIRES = requirements.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    LONG_DESCRIPTION = readme.read()


class BabelSdist(sdist):
    def run(self):
        self.run_command("compile_catalog")
        super().run()


setup(
    name="wllegal",
    version="0.4",
    packages=["wllegal"],
    include_package_data=True,
    license="GPLv3+",
    description=("Hosted Weblate legal stuff"),
    url="https://weblate.org/",
    download_url="https://weblate.org/download/",
    bugtrack_url="https://github.com/WeblateOrg/wllegal/issues",
    author="Michal Čihař",
    author_email="michal@cihar.com",
    zip_safe=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=REQUIRES,
    setup_requires=["Babel"],
    long_description=LONG_DESCRIPTION,
    cmdclass={"compile_catalog": babel.compile_catalog, "sdist": BabelSdist},
)
