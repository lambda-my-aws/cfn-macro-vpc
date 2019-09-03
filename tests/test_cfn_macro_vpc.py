#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cfn_macro_vpc` package."""

import pytest
from cfn_macro_vpc import cfn_macro_vpc

import yaml

values = None
with open('test_input.yml', 'r') as fd:
    values = yaml.loads(fd.read())

print(values)
