import pandas as pd
import numpy as np


CSV_FILE = "../data/ESS1-8e01/ESS1-8e01.csv"
OUT_FILE = "../data/out/full_data_clean.pickle"

""" Import """
usecols = [
    'cntry', 'essround', 'pspwght', 'pweight',
    'gndr', 'agea', 'polintr', 'trstprl', 'trstlgl', 'trstplc', 'trstplt',
    'trstprt', 'trstep', 'trstun', 'vote', 'lrscale', 'tvtot', 'tvpol',
    'netuse', 'stflife', 'stfeco', 'stfgov', 'stfdem', 'brncntr',
    'ctzcntr', 'facntr', 'mocntr', 'happy', 'edulvla', 'eduyrs',
    'hinctnta', 'uemp5yr', 'health', 'partner', 'sclmeet', 'crmvct',
    'mnactic', 'wkhtot', 'domicil', 'rlgblg', 'rlgdgr', 'chldhm',
    'chldhhe'
]

data = pd.read_csv(
    CSV_FILE,
    usecols=usecols
)


""" Data Cleaning"""
round_map = {
    1: pd.to_datetime(2002, format="%Y"),
    2: pd.to_datetime(2004, format="%Y"),
    3: pd.to_datetime(2006, format="%Y"),
    4: pd.to_datetime(2008, format="%Y"),
    5: pd.to_datetime(2010, format="%Y"),
    6: pd.to_datetime(2012, format="%Y"),
    7: pd.to_datetime(2014, format="%Y"),
    8: pd.to_datetime(2016, format="%Y")
}

gender_map = {
    1: 'm',
    2: 'f',
    9: np.nan
}

y_n_map = {
    1: 'y',
    2: 'n',
    6: np.nan,
    7: np.nan,
    8: np.nan,
    9: np.nan
}

domicil_map = {
    1: 'big_city',
    2: 'suburbs',
    3: 'town',
    4: 'country_village',
    5: 'farm_countryside',
    7: np.nan,
    8: np.nan,
    9: np.nan
}

main_activity_map = {
    1: "paid_work",
    2: "education",
    3: "unemployed_looking",
    4: "unemployed_not_looking",
    5: "sick_disabled",
    6: "retired",
    7: "community_military_service",
    8: "housework_children_others",
    9: "other",
    66: np.nan,
    77: np.nan,
    88: np.nan,
    99: np.nan
}

cntry_map = {
    'AT': 'Austria',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'CH': 'Switzerland',
    'CY': 'Cyprus',
    'CZ': 'Czechia',
    'DE': 'Germany',
    'DK': 'Denmark',
    'EE': 'Estonia',
    'ES': 'Spain',
    'FI': 'Finland',
    'FR': 'France',
    'GB': 'United Kingdom',
    'GR': 'Greece',
    'HR': 'Croatia',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IS': 'Iceland',
    'IT': 'Italy',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RU': 'Russia',
    'SE': 'Sweden',
    'SI': 'Slovenia',
    'SK': 'Slovakia',
    'TR': 'Turkey',
    'UA': 'Ukraine'
}
# basics
data['country'] = [cntry_map[x] for x in data['cntry']]
data['year'] = [round_map[x] for x in data['essround']]

# politics
data['polintr'].replace([7, 8, 9], np.nan, inplace=True)
data['trstprl'].replace([77, 88, 99], np.nan, inplace=True)
data['trstlgl'].replace([77, 88, 99], np.nan, inplace=True)
data['trstplc'].replace([77, 88, 99], np.nan, inplace=True)
data['trstplt'].replace([77, 88, 99], np.nan, inplace=True)
data['trstprt'].replace([77, 88, 99], np.nan, inplace=True)
data['trstep'].replace([77, 88, 99], np.nan, inplace=True)
data['trstun'].replace([77, 88, 99], np.nan, inplace=True)
data['vote'].replace([7, 8, 9], np.nan, inplace=True)
data['lrscale'].replace([77, 88, 99], np.nan, inplace=True)

# media
data['tvtot'].replace([77, 88, 99], np.nan, inplace=True)
data['tvpol'].replace([66, 77, 88, 99], np.nan, inplace=True)
data['netuse'].replace([77, 88, 99], np.nan, inplace=True)

# satisfaction
data['stflife'].replace([77, 88, 99], np.nan, inplace=True)
data['stfeco'].replace([77, 88, 99], np.nan, inplace=True)
data['stfgov'].replace([77, 88, 99], np.nan, inplace=True)
data['stfdem'].replace([77, 88, 99], np.nan, inplace=True)

# citizen/born
data['brncntr_map'] = [y_n_map[x] for x in data['brncntr']]
data['facntr_map'] = [y_n_map[x] for x in data['facntr']]
data['mocntr_map'] = [y_n_map[x] for x in data['mocntr']]
data['ctzcntr_map'] = [y_n_map[x] for x in data['ctzcntr']]

# person
data['happy'].replace([77, 88, 99], np.nan, inplace=True)
data['gndr_map'] = [gender_map[x] for x in data['gndr']]
data['agea'].replace(999, np.nan, inplace=True)
data['edulvla'].replace([0, 55, 77, 88, 99], np.nan, inplace=True)
data['eduyrs'].replace([77, 88, 99], np.nan, inplace=True)

# income
data['hinctnta'].replace([77, 88, 99], np.nan, inplace=True)
data['uemp5yr_map'] = [y_n_map[x] for x in data['uemp5yr']]

# socio-economic
data['health'].replace([7, 8, 9], np.nan, inplace=True)
data['partner_map'] = [y_n_map[x] for x in data['partner']]
data['sclmeet'].replace([77, 88, 99], np.nan, inplace=True)
data['crmvct_map'] = [y_n_map[x] for x in data['crmvct']] # crime
data['mnactic_map'] = [main_activity_map[x] for x in data['mnactic']]
data['wkhtot'].replace([666, 777, 888, 999], np.nan, inplace=True)
data['domicil_map'] = [domicil_map[x] for x in data['domicil']]

# religion - rlgblg binary, rlgdgr religiosity 1-10
data['rlgblg_map'] = [y_n_map[x] for x in data['rlgblg'].fillna(value=9)]
data['rlgdgr'].replace([77, 88, 99], np.nan, inplace=True)

# children (present, ever)
data['chldhm_map'] = [y_n_map[x] for x in data['chldhm']]
data['chldhhe_map'] = [y_n_map[x] for x in data['chldhhe']]
# consider adding: inprdsc, not available for full duration though

""" Export """
data.drop(
    columns=['chldhhe', 'chldhm', 'rlgblg', 'domicil', 'mnactic',
             'crmvct', 'partner', 'uemp5yr', 'ctzcntr', 'mocntr',
             'facntr', 'brncntr', 'gndr', 'essround', 'pweight', 'cntry'],
    inplace=True
)

data.to_pickle(OUT_FILE)
