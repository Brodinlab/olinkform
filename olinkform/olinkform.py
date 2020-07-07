"""Main module."""
import pandas as pd
from .parser import get_parser, results_to_dataframe


def parse(path, version):
    df = pd.read_excel(path)
    parser = get_parser(version)
    return parser(df)


def parse_to_dataframe(path, version):
    df = pd.read_excel(path)
    parser = get_parser(version)
    r = parser(df)
    return results_to_dataframe(r)

