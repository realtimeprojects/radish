#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
  name = "radish",
  version = "0.00.02",
  description = "Behaviour-Driven-Development tool for python",
  author = "Timo Furrer",
  author_email = "tuxtimo@gmail.com",
  url = "http://github.com/timofurrer/radish",
  packages = [ "radish", "radish/Writers" ],
  entry_points = { "console_scripts": [ "radish = radish.main:main", ] },
  package_data = { "radish": [ "*.md" ] }
)
