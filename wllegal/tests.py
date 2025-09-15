# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django.test import TestCase
from django.urls import reverse


class LegalTestCase(TestCase):
    def test_terms(self) -> None:
        response = self.client.get(reverse("legal:terms"))
        self.assertContains(response, "21668027")

    def test_privacy(self) -> None:
        response = self.client.get(reverse("legal:privacy"))
        self.assertContains(response, "21668027")

    def test_index(self) -> None:
        response = self.client.get(reverse("legal:index"))
        self.assertContains(response, "We process personal data")

    def test_security(self) -> None:
        response = self.client.get("/security.txt")
        self.assertRedirects(response, "/.well-known/security.txt")
        response = self.client.get("/.well-known/security.txt")
        self.assertContains(
            response, "https://github.com/WeblateOrg/weblate/security/advisories"
        )
