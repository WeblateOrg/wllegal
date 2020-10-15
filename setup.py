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
from distutils.command.build import build
from distutils.core import Command
from distutils.dep_util import newer
from glob import glob
from itertools import chain

from setuptools import setup
from translate.tools.pocompile import convertmo

LOCALE_MASKS = [
    "wllegal/locale/*/LC_MESSAGES/*.po",
]

with open("requirements.txt") as requirements:
    REQUIRES = requirements.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    LONG_DESCRIPTION = readme.read()


class BuildMo(Command):
    description = "update MO files to match PO"
    user_options = []

    def initialize_options(self):
        self.build_base = None

    def finalize_options(self):
        self.set_undefined_options("build", ("build_base", "build_base"))

    def run(self):
        for name in chain.from_iterable(glob(mask) for mask in LOCALE_MASKS):
            output = os.path.splitext(name)[0] + ".mo"
            if not newer(name, output):
                continue
            print(f"compiling {name} -> {output}")
            with open(name, "rb") as pofile, open(output, "wb") as mofile:
                convertmo(pofile, mofile, None)


class WeblateBuild(build):
    """Override the default build with new subcommands."""

    # The build_mo has to be before build_data
    sub_commands = [("build_mo", lambda self: True)] + build.sub_commands


setup(
    name="wllegal",
    version="0.8",
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
    setup_requires=["translate-toolkit"],
    long_description=LONG_DESCRIPTION,
    cmdclass={"build_mo": BuildMo, "build": WeblateBuild},
)
