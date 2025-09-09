.. image:: https://s.weblate.org/cdn/Logo-Darktext-borders.png
   :alt: Weblate
   :target: https://weblate.org/
   :height: 80px

**Weblate is libre software web-based continuous localization system,
used by over 2500 libre projects and companies in more than 165 countries.**


This is legal module used on the `Hosted Weblate service
<https://weblate.org/hosting/>`_.

You can use them as an example how to customize `Weblate
<https://weblate.org/>`_, but there are probably not generally usable.  If you
think something should be part of Weblate, please open an issue.

.. image:: https://img.shields.io/badge/website-weblate.org-blue.svg
    :alt: Website
    :target: https://weblate.org/

.. image:: https://hosted.weblate.org/widgets/weblate/-/svg-badge.svg
    :alt: Translation status
    :target: https://hosted.weblate.org/engage/weblate/?utm_source=widget

.. image:: https://bestpractices.coreinfrastructure.org/projects/552/badge
    :alt: CII Best Practices
    :target: https://bestpractices.coreinfrastructure.org/projects/552

.. image:: https://img.shields.io/pypi/v/wllegal.svg
    :target: https://pypi.org/project/wllegal/
    :alt: PyPI package

.. image:: https://readthedocs.org/projects/weblate/badge/
    :alt: Documentation
    :target: https://docs.weblate.org/

Installation
------------

Install using pip:

.. code-block:: sh

    pip3 install wllegal

Sources are available at <https://github.com/WeblateOrg/wllegal>.

Usage
-----

Include the module in the `INSTALLED_APPS`, it has to be placed prior to other
Weblate modules to override it's templates:

.. code-block:: python

   INSTALLED_APPS.insert(0, "wllegal")
