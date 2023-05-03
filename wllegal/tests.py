# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
        self.assertContains(response, "We process personal data")

    def test_security(self):
        response = self.client.get("/security.txt")
        self.assertContains(response, "https://hackerone.com/weblate")
