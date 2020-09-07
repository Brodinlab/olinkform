from collections import OrderedDict

import pandas as pd
from pandas.testing import assert_frame_equal

from olinkform.parser import parser_v1, parser_v2, results_to_dataframe


def test_parser_v1():
    # check length, keys, markers and dict value
    f = 'tests/data/new_v1.xlsx'
    df = pd.read_excel(f)
    r = parser_v1(df)
    assert len(r) == 112
    expected_keys = ['090202', '080414', '080521', '080303', '080813', '091130', '081229', '090205', '081117', '090423',
                     '091214', '090122', '090209', '081201', '090601', '081103', '091202', '090123', '090302', '090602',
                     '090326', '090414', '090914', '090310', '090421', '090507', '100525', '090505', '090605', '090622',
                     '090901', '100304', '100406', '110112', '100308', '100511', '101013', '110208', '100410', '100510',
                     '110307', '110316', '100412', '100503', '100609', '100930', '111017', '100922', '101122', '110317',
                     '110919', '101025', '110516', '101128', '101213', '110113', '111110', '110111', '110222', '110406',
                     '110505', '110622', '110407', '110617', '120509', '110502', '110707', '111007', '121009', '111208',
                     '120109', '120405', '130128', '120213', '120312', '120507', '120611', '120104', '130122', '120223',
                     '120322', '120503', '120110', '130325', '120510', '120604', '120618', '120924', '131021', '120813',
                     '120914', '121119', '120524', '131008', '121001', '121218', '130220', '120910', '130304', '130506',
                     '130429', '130131', '140403', '130516', '130710', '130411', '131007', '131122', '131203', '140305',
                     '130905', 'KP']
    assert set(r.keys()) == set(expected_keys)

    expected_markers = ['IL-8', 'VEGF-A', 'BDNF', 'MCP-3', 'hGDNF', 'CDCP1', 'CD244', 'IL-7', 'OPG', 'LAP TGF-beta-1',
                        'uPA', 'IL-6', 'IL-17C', 'MCP-1', 'IL-17A', 'CXCL11', 'AXIN1', 'TRAIL', 'IL-20RA', 'CXCL9',
                        'CST5', 'IL-2RB', 'IL-1 alpha', 'OSM', 'IL-2', 'CXCL1', 'TSLP', 'CCL4', 'CD6', 'SCF', 'IL-18',
                        'SLAMF1', 'TGFA', 'MCP-4', 'CCL11', 'TNFSF14', 'FGF-23', 'IL-10RA', 'FGF-5', 'MMP-1', 'LIF-R',
                        'FGF-21', 'CCL19', 'IL-15RA', 'IL-10RB', 'IL-22 RA1', 'IL-18R1', 'PD-L1', 'Beta-NGF', 'CXCL5',
                        'TRANCE', 'HGF', 'IL-12B', 'IL-24', 'IL-13', 'ARTN', 'MMP-10', 'IL-10', 'TNF', 'CCL23', 'CD5',
                        'MIP-1 alpha', 'Flt3L', 'CXCL6', 'CXCL10', '4E-BP1', 'IL-20', 'SIRT2', 'CCL28', 'DNER',
                        'EN-RAGE', 'CD40', 'IL-33', 'IFN-gamma', 'FGF-19', 'IL-4', 'LIF', 'NRTN', 'MCP-2', 'CASP-8',
                        'CCL25', 'CX3CL1', 'TNFRSF9', 'NT-3', 'TWEAK', 'CCL20', 'ST1A1', 'STAMPB', 'IL-5', 'ADA',
                        'TNFB', 'CSF-1']

    assert set(r['130905'].keys()) == set(expected_markers)
    assert r['130905']['NT-3'] == {'value': 0.8318772411916731, 'LOD': 1.78, 'MDF': 0.14049586776859502,
                                   'batch': 2015020, 'projectID': 'baby'}


def test_parser_v2():
    # check length, keys, markers and dict value
    f = 'tests/data/new_v2.xlsx'
    df = pd.read_excel(f)
    r = parser_v2(df)
    assert len(r) == 90
    expected_keys = ['ME/CFS_001_B', 'ME/CFS_003_T1', 'ME/CFS_026_T1', 'ME/CFS_005_T2', 'ME/CFS_004_T2',
                     'ME/CFS_029_T1', 'ME/CFS_015_T2', 'ME/CFS_012_T1', 'ME/CFS_028_T2', 'ME/CFS_031_T2',
                     'ME/CFS_003_T2', 'HC (Lucie): 1st wk', 'ME/CFS_022_T1', 'ME/CFS_011_T2', 'ME/CFS_008_T2',
                     'ME/CFS_014_B', 'ME/CFS_013_T2', 'ME/CFS_031_T1_1 wk', 'ME/CFS_019_T1', 'ME/CFS_025_T1',
                     'ME/CFS_013_T1', 'ME/CFS_005_B', 'ME/CFS_030_T2', 'ME/CFS_007_B', 'ME/CFS_026_B',
                     'ME/CFS_021_T1', 'ME/CFS_015_T1', 'ME/CFS_023_B', 'ME/CFS_017_T2', 'ME/CFS_002_B',
                     'ME/CFS_029_T2', 'ME/CFS_017_T1', 'ME/CFS_031_T1', 'ME/CFS_030_B', 'ME/CFS_009_T2',
                     'ME/CFS_022_B', 'ME/CFS_024_T2', 'HC (Axel): After 12 wks', 'ME/CFS_027_T1', 'ME/CFS_004_T1',
                     'ME/CFS_007_T2', 'ME/CFS_006_B', 'ME/CFS_002_T1', 'ME/CFS_010_T1', 'ME/CFS_015_B',
                     'ME/CFS_032_T1', 'ME/CFS_023_T1', 'ME/CFS_021_T2', 'ME/CFS_026_T2', 'ME/CFS_029_B',
                     'ME/CFS_019_B', 'ME/CFS_009_T1', 'HC (Jun): 1st wk', 'ME/CFS_024_B', 'ME/CFS_025_T2',
                     'ME/CFS_032_B', 'ME/CFS_011_B', 'ME/CFS_001_T1', 'ME/CFS_005_T1', 'ME/CFS_027_B',
                     'ME/CFS_008_B', 'ME/CFS_028_B', 'ME/CFS_010_T2', 'ME/CFS_004_B', 'ME/CFS_028_T1',
                     'ME/CFS_017_B', 'ME/CFS_013_B', 'ME/CFS_032_T2', 'HC (Axel): 1st wk ', 'ME/CFS_014_T1',
                     'ME/CFS_009_B', 'ME/CFS_001_T2', 'ME/CFS_031_B', 'ME/CFS_012_T2', 'ME/CFS_003_B', 'ME/CFS_016_B',
                     'ME/CFS_002_T2', 'ME/CFS_024_T1', 'ME/CFS_010_B', 'ME/CFS_021_B', 'ME/CFS_022_T2',
                     'ME/CFS_023_T2', 'ME/CFS_025_B', 'ME/CFS_027_T2', 'ME/CFS_014_T2', 'ME/CFS_012_B',
                     'ME/CFS_019_T2', 'HC (Christian): 1st wk', 'ME/CFS_007_T1', 'ME/CFS_030_T1']
    assert set(r.keys()) == set(expected_keys)

    expected_markers = ['IL8', 'VEGFA', 'CD8A', 'MCP-3', 'GDNF', 'CDCP1', 'CD244', 'IL7', 'OPG', 'LAP TGF-beta-1',
                        'uPA', 'IL6', 'IL-17C', 'MCP-1', 'IL-17A', 'CXCL11', 'AXIN1', 'TRAIL', 'IL-20RA', 'CXCL9',
                        'CST5', 'IL-2RB', 'IL-1 alpha', 'OSM', 'IL2', 'CXCL1', 'TSLP', 'CCL4', 'CD6', 'SCF', 'IL18',
                        'SLAMF1', 'TGF-alpha', 'MCP-4', 'CCL11', 'TNFSF14', 'FGF-23', 'IL-10RA', 'FGF-5',
                        'MMP-1', 'LIF-R', 'FGF-21', 'CCL19', 'IL-15RA', 'IL-10RB', 'IL-22 RA1', 'IL-18R1',
                        'PD-L1', 'Beta-NGF', 'CXCL5', 'TRANCE', 'HGF', 'IL-12B', 'IL-24', 'IL13', 'ARTN', 'MMP-10',
                        'IL10', 'TNF', 'CCL23', 'CD5', 'CCL3', 'Flt3L', 'CXCL6', 'CXCL10', '4E-BP1', 'IL-20', 'SIRT2',
                        'CCL28', 'DNER', 'EN-RAGE', 'CD40', 'IL33', 'IFN-gamma', 'FGF-19', 'IL4', 'LIF', 'NRTN',
                        'MCP-2', 'CASP-8', 'CCL25', 'CX3CL1', 'TNFRSF9', 'NT-3', 'TWEAK', 'CCL20', 'ST1A1',
                        'STAMBP', 'IL5', 'ADA', 'TNFB', 'CSF-1', 'CLMP', 'LRIG1', 'NPTXR', 'AHCY', 'THOP1', 'CTSO',
                        'FCRL1', 'CD164', 'DDC', 'ACP6', 'TFF2', 'S100P', 'ANGPT2', 'CD2AP', 'ANGPTL7', 'CLEC5A',
                        'TINAGL1', 'GLRX', 'ENO2', 'NADK', 'GHRL', 'SERPINB8', 'SERPINB6', 'CDHR5', 'CCDC80', 'DIABLO',
                        'CA13', 'SEMA3F', 'KLK10', 'PILRB', 'ANGPTL1', 'APLP1', 'ADGRG2', 'TYMP', 'GRAP2', 'LILRA5',
                        'ALDH1A1', 'CD79B', 'ANXA4', 'ANXA11', 'SIGLEC7', 'ITGB7', 'QDPR', 'SNAP23', 'APEX1', 'ENTPD5',
                        'CLSTN2', 'COMT', 'CLUL1', 'HDGF', 'CHRDL2', 'CTSH', 'NOMO1', 'NQO2', 'SOST', 'FAM3C', 'TXNDC5',
                        'PPP1R2', 'DPP7', 'LRP11', 'ADGRE2', 'ENPP7', 'SSC4D', 'MCFD2', 'REG4', 'SUMF2', 'CANT1',
                        'CD1C', 'GAL', 'CDH2', 'TYRO3', 'CRKL', 'IGFBPL1', 'RTN4R', 'VCAN', 'FBP1', 'TSHB', 'BAG6',
                        'NECTIN2', 'ARG1', 'USP8', 'FKBP4', 'SDC4', 'PAG1', 'KYAT1', 'DAB2', 'NPDC1', 'METRNL',
                        'MEP1B', 'ROR1', 'NT-proBNP', 'RNASE3', 'IFNL1', 'EIF4B', 'CRADD', 'TDGF1', 'ECE1', 'CETN2',
                        'CDH15', 'SMOC1', 'FOLR2', 'KLB', 'CDH17', 'GPNMB', 'BST2', 'PTPN1', 'SRP14', 'ATP6V1F',
                        'RBKS', 'FKBP7', 'ANXA10', 'GSTP1', 'KIR2DL3', 'RPS6KB1', 'EREG', 'CD302', 'IMPA1', 'CRIP2',
                        'SCGB1A1', 'CTF1', 'FHIT', 'CLSTN1', 'HSP90B1', 'LEPR', 'CD33', 'ADAM15', 'NDRG1', 'CEACAM3',
                        'GBP2', 'FGFR2', 'NXPH1', 'NAA10', 'IL15', 'DSG3', 'SFRP1', 'IFI30', 'FCAR', 'PRTFDC1',
                        'PLA2G10', 'IKZF2', 'UBE2F', 'DPEP2', 'TBCB', 'NPM1', 'ASGR1', 'EPHA10', 'COL4A3BP', 'PSG1',
                        'PSME1', 'KIRREL2', 'PAEP', 'CCL27', 'MAD1L1', 'AKT1S1', 'PTS', 'IL32', 'FUT8', 'TPPP3',
                        'PFDN2', 'CARHSP1', 'VSTM1', 'DEFB4A', 'ABHD14B', 'AARSD1', 'PHOSPHO1', 'DUSP3', 'TNFRSF13C',
                        'NEFL', 'HMOX2', 'RNF31', 'DPEP1', 'SNCG', 'IL3RA', 'AOC1', 'KIF1BP', 'PPP3R1', 'ILKAP',
                        'ISLR2', 'ING1', 'PMVK', 'WWP2', 'FKBP5', 'GGT5', 'CD63']
    assert set(r['ME/CFS_001_B'].keys()) == set(expected_markers)
    assert r['ME/CFS_001_B']['CD63'] == {'value': 5.93737, 'LOD': -1.05438, 'MDF': 0.04444, 'batch': 190516, 'projectID': 'ME/CFS'}


def test_results_to_dataframe():
    r = OrderedDict()

    r['ME/CFS_001_B'] = {
        'CD63': {'value': 5.93737, 'LOD': -1.05438, 'MDF': 0.04444, 'batch': 190516, 'projectID': 'ME/CFS'}
    }
    r['ME/CFS_003_T1'] = OrderedDict()
    r['ME/CFS_003_T1']['PFDN2'] = {'value': 1.55192, 'LOD': 1.08316, 'MDF': 0.11111, 'batch': 190516, 'projectID': 'ME/CFS'}
    r['ME/CFS_003_T1']['ABHD14B'] = {'value': 0.55768, 'LOD': -0.12011, 'MDF': 0.2, 'batch': 190516, 'projectID': 'ME/CFS'}

    df = results_to_dataframe(r)
    expected = pd.DataFrame([[190516, 'ME/CFS', 'ME/CFS_001_B', 'CD63', 5.93737, -1.05438, 0.04444],
                             [190516, 'ME/CFS', 'ME/CFS_003_T1', 'PFDN2', 1.55192, 1.08316, 0.11111],
                             [190516, 'ME/CFS', 'ME/CFS_003_T1', 'ABHD14B', 0.55768, -0.12011, 0.2]
                             ],
                            columns=['batch', 'projectID', 'sample_id', 'marker', 'value', 'LOD', 'MDF'])
    assert_frame_equal(df, expected)
