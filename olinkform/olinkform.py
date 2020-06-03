"""Main module."""
import pandas as pd
from .parser import get_parser


def parse(path, version):
    df = pd.read_excel(path)
    parser = get_parser(version)
    return parser(df)
