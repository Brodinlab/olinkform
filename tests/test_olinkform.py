#!/usr/bin/env python

"""Tests for `olinkform` package."""

from olinkform import parse


def test_parse():
    r1 = parse('tests/data/v1.xlsx', 'v1')
    assert len(r1) == 112

    r2 = parse('tests/data/v2.xlsx', 'v2')
    assert len(r2) == 90
