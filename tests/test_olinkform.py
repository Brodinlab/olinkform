#!/usr/bin/env python

"""Tests for `olinkform` package."""

from olinkform import parse, parse_to_dataframe


def test_parse():
    r1 = parse('tests/data/new_v1.xlsx', 'v1')
    assert len(r1) == 112

    r2 = parse('tests/data/new_v2.xlsx', 'v2')
    assert len(r2) == 90


def test_parse_to_csv():
    r1 = parse_to_dataframe('tests/data/new_v1.xlsx', 'v1')
    assert r1.shape == (10304, 7)

    r2 = parse_to_dataframe('tests/data/new_v2.xlsx', 'v2')
    assert r2.shape == (24840, 7)
