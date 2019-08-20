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

# from .Agents import * # << not necessary ... ? 

class SimpleOLSRegression():

    def __init__(self, dataframe, iv, iv_name, dv, dv_name, verbose=True):

        self.dataframe = dataframe
        self.iv = iv
        self.iv_name = iv_name
        self.dv = dv
        self.dv_name = dv_name

        self.verbose = verbose

        self.pearson = dataframe[[iv, dv]].corr()
        if self.verbose:
            print("Pearson correlation coefficient:", self.pearson.loc[iv, dv])

        self.X_values = sms.add_constant(dataframe[iv])
        self.regression_model = sms.OLS(dataframe[dv], self.X_values).fit()

        if self.verbose:
            print(self.regression_model.summary())

        self.gradient = self.regression_model.params[1]
        self.intercept = self.regression_model.params[0]
        self.rsquared = self.regression_model.rsquared
        self.pval = self.regression_model.f_pvalue

        self.x_lobf = [self.dataframe[self.iv].min(), self.dataframe[self.iv].max()]
        self.y_lobf = [self.x_lobf[0] * self.gradient + self.intercept, self.x_lobf[1] * self.gradient + self.intercept]

        self.dataframe[self.dv + '_predicted'] = self.dataframe.apply(lambda row: row[self.iv] * self.gradient + self.intercept, axis=1)
        self.dataframe[self.dv + '_error'] = self.dataframe[self.dv] - self.dataframe[self.dv + '_predicted']

    def print_regression_model_summary(self):
        print(self.regression_model.summary())

    def summary_stats(self):
        self.dataframe.describe()

    def scatter(self, savefig=False):

        plt.figure(figsize=(10,7))
        plt.scatter(self.dataframe[self.iv], self.dataframe[self.dv], label='Model iteration')

        if savefig:
            plt.savefig(savefig)


    def scatter_OLS(self, savefig=False):

        if self.pval < 0.05:
            ptext = "p < 0.05"
        else:
            ptext = "p = " + str(round(self.pval, 5))

        # Visualizing observations and OLS regression
        plt.figure(figsize=(10,7))
        plt.scatter(self.dataframe[self.iv], self.dataframe[self.dv], label='Model iteration')

        plt.plot(self.x_lobf, self.y_lobf, 'r--', label="Line of best fit (OLS linear regression)" )
        plt.legend(bbox_to_anchor=(1.05, 0.95))

        # Adapted from https://matplotlib.org/3.1.1/gallery/recipes/placing_text_boxes.html
        textstr = "\n".join((
            "y = " + str(round(self.gradient, 5)) + 'x + ' + str(round(self.intercept, 5)),
            ptext,
            r"$R^2$ = " + str(round(self.rsquared, 5))
        ))

        plt.text( self.dataframe[self.iv].max() + ((self.dataframe[self.iv].max() - self.dataframe[self.iv].min()) * 0.2),
                 self.dataframe[self.dv].max() - ((self.dataframe[self.dv].max() - self.dataframe[self.dv].min()) * 0.25), textstr)

        # add Rsquared, MSE, p-value
        _ = plt.xlabel(self.iv_name)
        _ = plt.ylabel(self.dv_name)
        _ = plt.title("Scatterplot and OLS regression line of best fit:\n" +
                      self.iv_name + " versus \n" + self.dv_name.lower())

        if savefig:
            plt.savefig(savefig)

    def plot_residuals_fits(self, savefig=False):
        plt.figure(figsize=(10,3))

        plt.scatter(self.dataframe[self.dv + '_predicted'], self.dataframe[self.dv + '_error'])
        _ = plt.xlabel('Predicted ' + self.dv_name)
        _ = plt.ylabel('Residual error')
        _ = plt.title("Residuals vs fits: The effects of " + self.iv_name.lower() + " on\n " + self.dv_name.lower())

        if savefig:
            plt.savefig(savefig)

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
