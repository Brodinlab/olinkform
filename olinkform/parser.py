import numpy as np
import pandas as pd


def parser_v1(df):
    df = df.iloc[:-18, :-8]  # remove unnecessary rows
    df.columns = df.columns.str[4:]  # to match protein naming in new Olink format
    # Sample as keys fix
    df = df.set_index("linear")
    # linear NPX to NPX (log2)
    sample_dict = dict()
    for i in range(len(df.index) - 5):
        sample_name = df.index[i]
        sample_name = sample_name[-6:]
        dict_for_this_sample = dict()
        for j in range(len(df.columns)-2):
            name_of_prot = df.columns[j]
            dict_for_this_sample[name_of_prot] = {'value': np.log2(df.iloc[i, j]), 'LOD': df.iloc[-1, j],
                                                  'MDF': df.iloc[-5,j], 'batch': int(df.iloc[i,-2]), 'projectID': df.iloc[i,-1]}
        sample_dict[sample_name] = dict_for_this_sample
    return sample_dict


def parser_v2(df):
    # dropping unwanted/unnecessary rows
    df = df.drop([0, 1, 3, 4, 5, 96])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])
    # dropping unwanted columns
    df = df.drop(['QC Warning', 'Plate ID'], axis=1)
    # Sample as keys fix
    df = df.set_index("Assay")
    sample_dict = dict()
    for i in range(len(df.index) - 2):
        dict_for_this_sample = dict()
        for j in range(len(df.columns)-2):
            name_of_prot = df.columns[j]
            dict_for_this_sample[name_of_prot] = {'value': df.iloc[i, j], 'LOD': df.iloc[-2, j],
                                                  'MDF': df.iloc[-1, j], 'batch': df.iloc[i,-2], 'projectID': df.iloc[i,-1]}
        sample_name = df.index[i].replace(' - ', '_').replace('-', '_')
        sample_dict[sample_name] = dict_for_this_sample
    return sample_dict


def results_to_dataframe(sample_dict):
    items = list()
    for sample_id in sample_dict.keys():
        sample = sample_dict[sample_id]
        for marker_id in sample.keys():
            value = {**sample[marker_id], 'sample_id': sample_id, 'marker': marker_id}
            items.append(value)
    return pd.DataFrame(items)[['batch', 'projectID', 'sample_id', 'marker', 'value', 'LOD', 'MDF']]


def get_parser(version):
    func_map = {
        'v1': parser_v1,
        'v2': parser_v2
    }
    return func_map[version]
