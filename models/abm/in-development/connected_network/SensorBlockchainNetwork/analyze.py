import os
import sys
import pickle
import numpy as np
import pandas as pd
import seaborn as sn
import statsmodels.api as sms
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf


def calculate_summary_stats_from_agent_vars_dfs(df, warmup=30):
    # Operates on dataframe in place, adding columns of summary statistics
    # for the agent-level variables recorded in the agent_vars_by_tick column

    for dv in df['agent_vars_by_tick'][0].columns.tolist():
        for i, row in df.iterrows():
            summary = row['agent_vars_by_tick'][dv].unstack().describe().mean(axis=1)
            summary_post_warmup = row['agent_vars_by_tick'][dv].unstack()[warmup:].describe().mean(axis=1)

            for idx in summary.index:
                df.loc[i, dv + '_' + idx] = summary[idx]
                df.loc[i, dv + '_post_warmup_' + idx] = summary_post_warmup[idx]


def get_model_vars_df_from_pickle(filepath):
    try:

        f = open(filepath, 'rb')
        dfs = pickle.load(f)
        f.close()

        model_df = dfs['batch_model_df']
        calculate_summary_stats_from_agent_vars_dfs(model_df)

        return model_df
        # model_dataframes[file.replace('.pkl', '')] = model_df

    except:
        print("error with " + filepath + ":", sys.exc_info()[0])


def pearson_corr(df, iv, dv, verbose=True):
    pearson = df[[iv, dv]].corr()

    X_values = sms.add_constant(df[iv])
    regression_model = sms.OLS(df[dv], X_values).fit()
    if verbose:
        print(regression_model.summary())


    return {'regr_model': regression_model, 'X_values': X_values, 'pearson': pearson}

def line_of_best_fit(coeff, y_int, x):
    return coeff * x + y_int

def calculate_adf_results(series):

    adf = adfuller(series)

    results = {'adf_statistic': adf[0],
               'p_value': adf[1],
               '1%_critical_value': adf[4]['1%'],
               '5%_critical_value': adf[4]['5%'],
               '10%_critical_value': adf[4]['10%']}

    return results
