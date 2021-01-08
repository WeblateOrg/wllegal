#
# Copyright © 2012 - 2021 Michal Čihař <michal@cihar.com>
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

from django.test import TestCase
from django.urls import reverse


class LegalTestCase(TestCase):
    def test_terms(self):
        response = self.client.get(reverse("legal:terms"))
        self.assertContains(response, "04705904")

    def test_privacy(self):
        response = self.client.get(reverse("legal:privacy"))
        self.assertContains(response, "04705904")

    def test_index(self):
        response = self.client.get(reverse("legal:index"))
        self.assertContains(response, "The services are provided")

    def test_security(self):
        response = self.client.get("/security.txt")
        self.assertContains(response, "https://hackerone.com/weblate")
