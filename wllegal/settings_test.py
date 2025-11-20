# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os.path

from weblate.settings_test import *  # noqa: F403

INSTALLED_APPS = ["wllegal", *list(INSTALLED_APPS)]  # noqa: F405

LOCALE_PATHS = [os.path.join(os.path.dirname(__file__), "locale")]
LOCALE_FILTER_FILES = False
