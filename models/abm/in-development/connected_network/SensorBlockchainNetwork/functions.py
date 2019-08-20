import sys
import pickle
import numpy as np
import pandas as pd

# Agent Reporters #
#                 #
#                 #
# =============== #




# Model Reporters #
#                 #
#                 #
# =============== #

def get_datacollector(model):
    return model.datacollector

def get_agent_expiry_ticks(model):
    # In analysis will need to check expiry ticks column and
    # cast to int to get summary stats.

    s = pd.DataFrame(columns=['unique_id', 'expiry_tick'])

    for a in model.schedule.agents:
        s = s.append({'unique_id': int(a.unique_id), 'expiry_tick': a.dead}, ignore_index=True)

    survival_rate = s['expiry_tick'].isna().sum() / len(s)

    s = s[['expiry_tick']].dropna().astype(int).describe()
    s.loc['survival_rate'] = survival_rate

    return s

def get_agent_vars_by_tick(model):
    return model.datacollector.get_agent_vars_dataframe()

def get_model_vars_by_tick(model):
    return model.datacollector.get_model_vars_dataframe()

def get_mining_summary(model):
    try:
        df = model.blockchain.mempool
        frac_unmined = df['block_mined'].isna().sum() / len(df)

        df = df.dropna()
        df['mining_time'] = df['block_mined'] - df['block_submitted']

        s = df['mining_time'].astype(int).describe()
        s['frac_unmined'] = frac_unmined

        return s

    except:
        return "Failed on tick " + str(model.schedule.steps) + " --- " + sys.exc_info[0]


# Batch Reporters #
#                 #
#                 #
# =============== #

class InfoCurrency:
    """ A cheeky workaround to store dataframes as a value in another dataframe ..."""
    def __init__(self, df):
        self.df = df

def extract_informational_currency_from_batch_df(batch_df):

    df_tmp = pd.DataFrame(columns=['num_sensors',  'record_freq', 'record_bytes', 'stochasticity', 'info_currency_df'])
    for i, row in batch_df.iterrows():
        df_tmp.loc[i, 'num_sensors'] = row['num_sensors']
        df_tmp.loc[i, 'record_freq'] = row['record_freq']
        df_tmp.loc[i, 'record_bytes'] = row['record_bytes']
        df_tmp.loc[i, 'stochasticity'] = row['stochasticity']

        df_tmp.loc[i, 'info_currency_df'] = InfoCurrency(row['data_collector'].get_agent_vars_dataframe()['informational_currency'].unstack())

    return df_tmp

def extract_mining_summary_from_batch_df(batch_df):
    """
    A function extracting mining descriptive statistics
    from the dataframe returned from the
    batchrunner.get_model_vars_dataframe() method invocation
    """
    df = pd.DataFrame(columns=['num_sensors',  'record_freq', 'record_bytes', 'stochasticity', 'mean_mining_time', 'std', 'min', 'max'])

    for i, row in batch_df.iterrows():

        df.loc[i, 'num_sensors'] = row['num_sensors']
        df.loc[i, 'record_freq'] = row['record_freq']
        df.loc[i, 'record_bytes'] = row['record_bytes']
        df.loc[i, 'stochasticity'] = row['stochasticity']

        try:
            df.loc[i, 'mean_mining_time'] = row['mining_summary']['mean']
            df.loc[i, 'std'] = row['mining_summary']['std']
            df.loc[i, 'min'] = row['mining_summary']['min']
            df.loc[i, 'max'] = row['mining_summary']['max']
        except:
            df.loc[i, 'mean_mining_time'] = row['mining_summary']

    return df

def extract_gwei_spent_from_batch_df(batch_df):
    df_tmp = pd.DataFrame(columns=['num_sensors',  'record_freq', 'record_bytes', 'stochasticity'])

    for i, row in batch_df.iterrows():
        df_tmp.loc[i, 'num_sensors'] = row['num_sensors']
        df_tmp.loc[i, 'record_freq'] = row['record_freq']
        df_tmp.loc[i, 'record_bytes'] = row['record_bytes']
        df_tmp.loc[i, 'stochasticity'] = row['stochasticity']

        df_gwei = row['data_collector'].get_agent_vars_dataframe()['gwei_spent'].unstack()

        for col in df_gwei.columns:
            df_gwei[str(col) + '_shift'] = df_gwei[col].shift(1)
            df_gwei[str(col) + '_gwei_spend'] = df_gwei[col] - df_gwei[str(col) + '_shift']

        df_gwei = df_gwei[[col for col in df_gwei.columns if 'spend' in str(col)]]

        df_tmp.loc[i, 'df_gwei_spent'] = InfoCurrency(df_gwei)

    return df_tmp

def extract_network_life_cycle_from_batch_df(batch_df):
    return batch_df[[ 'num_sensors','record_bytes', 'record_freq', 'stochasticity', 'agent_expiry_ticks']]


# To generate pickles of results to import into the analysis notebook

def pickle_batch_run_results(batch_run, outfile):

    model_dfs = batch_run.get_model_vars_dataframe()
    mining_cols = model_dfs['mining_summary'][0].index.tolist()

    for i, row in model_dfs[['mining_summary']].iterrows():
        for c in mining_cols:
            try:
                model_dfs.loc[i, 'mining_' + c] = row['mining_summary'][c]
            except:
                model_dfs.loc[i, 'mining_' + c] = np.nan


    d = {
        'batch_model_df': model_dfs,
        'batch_agent_df': batch_run.get_agent_vars_dataframe()
    }

    with open(outfile, 'wb') as f:
        pickle.dump(d, f)
