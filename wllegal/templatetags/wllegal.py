# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from django import template
from django.utils.translation import get_language
from weblate_language_data.docs import DOCUMENTATION_LANGUAGES

register = template.Library()


@register.simple_tag
def weblate_documentation(page: str, anchor: str = "") -> str:
    """Return link to Weblate documentation."""
    doc_version = "latest"
    # Language variant
    code = DOCUMENTATION_LANGUAGES.get(get_language(), "en")
    # Optionally append anchor
    if anchor:
        anchor = "#{}".format(anchor.replace("_", "-"))
    # Generate URL
    return f"https://docs.weblate.org/{code}/{doc_version}/{page}.html{anchor}"
