"""{{ cookiecutter.project_short_description }}

This package demonstrates modern Python packaging practices with integrated
tooling for code quality, testing, and documentation.
"""

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

from .core import Calculator, greet

__all__ = ["Calculator", "greet", "__version__"]
