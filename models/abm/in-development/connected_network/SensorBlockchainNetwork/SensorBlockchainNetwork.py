import sys
import math
import copy
import random
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from mesa import Agent
from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import Grid
from mesa.time import RandomActivation
from mesa.batchrunner import BatchRunner

# Class definitions

class Sensor(Agent):
    """
    An edge device.

    Attributes:
        battery_life: Total battery on board.
        mortal: a boolean value indicating whether the agent should
            cease activity once battery is depleted.
        record_cost, record_freq, record_bytes: Values
            to calculate sensor recording behavior
        compute_cost_per_byte: An abstracted link between
            bytes computed and energy consumed
        info_reduction: An abstracted scaling metric to
            calculate the amount of data to transmit based
            on the amount of data collected at the edge.
            Represents edge computing capability.
        sign_cost: An estimate of the energy consumed to sign a tx.
        transmit_cost_per_byte: A link between bytes transmitted
            and energy consumed
        transmit_freq: How often data is transmitted from the sensor
            to the blockchain. If n > 1, every n ticks. If n < 1,
            n is the probability of transmitting each tick
        gas_price: The gas_price a sensor is willing to pay to get
            its transactions mined by the EVM.
        blockchain: a pointer to the blockchain each sensor is
            connecting to, so it can invoke class methods
        stochasticity: The measure of randomness, applied when
            appropriate, to simulate variation
        model: The model that is creating the sensor.

    """
    def __init__(self, unique_id, battery_life, mortal,
                record_cost, record_freq, record_bytes,
                compute_cost_per_byte, info_reduction,
                sign_cost,
                transmit_cost_per_byte, transmit_freq,
                gas_price, blockchain, stochasticity,
                model):

        super().__init__(unique_id, model)

        if self.model.verbose:
            print('Creating Sensor agent ID', unique_id)

        self.battery_life = battery_life
        self.mortal = mortal
        self.dead = np.nan
        self.record_cost = record_cost
        self.record_freq = record_freq
        self.record_bytes = record_bytes
        self.compute_cost_per_byte = compute_cost_per_byte
        self.info_reduction = info_reduction
        self.sign_cost = sign_cost
        self.transmit_cost_per_byte = transmit_cost_per_byte
        self.transmit_freq = transmit_freq
        self.gas_price = gas_price
        self.blockchain = blockchain
        self.stochasticity = stochasticity

        self.gwei_spent = 0
        self.data_collected = 0
        self.last_sync = 0
        self.nonce = 0
        self.db = np.array([]) # << bytes recorded per tick

        self.blockchain.chain.loc[0, self.unique_id] = False


    def record(self):
        if (self.record_freq > 1 and self.model.schedule.steps % self.record_freq == 0) or self.record_freq > random.random():

                self.battery_life -= self.record_cost # << independent of number of bytes?
                new_record = self.record_bytes
                if self.stochasticity:
                    new_record = math.ceil(new_record  * (1 + random.uniform(self.stochasticity * -1, self.stochasticity)))

                self.db = np.append(self.db, new_record)

        else:
            self.db = np.append(self.db, 0)


    def next_nonce(self):
        self.nonce += 1
        return self.nonce


    def transmit(self):

        if self.model.verbose:
            print("Transmitting tx from", self.unique_id)

        # Prepare data for transmission:

        # Calculate number of bytes to transmit (result of edge computation)
        bytes_collected = np.sum(self.db[self.last_sync : ])
        num_bytes_to_transmit = self.compute(bytes_collected)

        if num_bytes_to_transmit > 0:

            tx = self.create_tx_dict(self.next_nonce(),
                           self.last_sync, self.model.schedule.steps,
                           self.gas_price, num_bytes_to_transmit)

            # Prepare and sign tx
            self.sign()

            # Transmit, subtracting energy cost and adding gwei cost
            self.battery_life -= self.transmit_cost_per_byte * num_bytes_to_transmit
            self.blockchain.add_to_mempool(tx)

            self.last_sync = self.model.schedule.steps

    def create_tx_dict(self, nonce, start, end, gas_price, num_bytes):
        """
        Assemble variables into a dictionary representing
        an (abstracted) Ethereum transaction.
        """

        tx = {}

        tx['nonce'] = nonce
        tx['from_address'] = self.unique_id
        tx['start_sync'] = start
        tx['end_sync'] = end
        tx['gas_price'] = gas_price
        # self.gas_limit = gas_limit # << unused parameter
        tx['num_bytes'] = num_bytes

        return tx

    def compute(self, num_bytes):

        # Only invoked from within the transmit() method

        if self.info_reduction is not 1:
            self.battery_life -= self.compute_cost_per_byte * num_bytes
            return math.ceil(self.info_reduction * num_bytes)
        else:
            return num_bytes
            # with no compute cost


    def sign(self):

        # Only invoked from within the transmit() method
        self.battery_life -= self.sign_cost


    def confirm_tx(self, tx):

        # Here we could include learning element ...

#         mine_lag =  self.model.schedule.steps - tx.block_submitted
        # if mine_lag took too long - or was too quick - according to some threshold:
        #      change transmit_freq, info_reduction or gas_price ...

        self.gwei_spent += tx.gas_spend


    def step(self):

        self.gwei_spent = 0

        if math.isnan(self.dead):
            if self.battery_life < 0 and self.mortal:
                if self.model.verbose:
                    print("Sensor", self.unique_id, "out of battery at tick", self.model.schedule.steps)
                self.dead = self.model.schedule.steps

            self.record()

            if self.transmit_freq >= 1:
                if self.model.schedule.steps % self.transmit_freq == 0:
                    self.transmit()
            elif self.transmit_freq > random.random():
                self.transmit()





class Blockchain(Agent):

    def __init__(self, unique_id, gas_price, block_gas_limit,
                gas_per_byte, gas_per_second, avg_block_time, model):

        super().__init__(unique_id, model)

        if self.model.verbose:
            print("Blockchain created: ID", unique_id)

        self.gas_price = gas_price
        self.block_gas_limit = block_gas_limit
        self.gas_per_byte = gas_per_byte
        self.gas_per_second = gas_per_second
        self.avg_block_time = avg_block_time
        self.chain = pd.DataFrame()

        self.tx_ct = 0
        self.mempool = pd.DataFrame(columns=["from_address", "nonce",
                                             "start_sync", "end_sync",
                                             "gas_price", "num_bytes",
                                             "gas_spend", "tx_id",
                                             "mined", "block_submitted"])

    def add_to_mempool(self, tx):
        tx['gas_spend'] = tx['gas_price'] * self.gas_per_byte * tx['num_bytes']

        tx['tx_id'] = self.tx_ct
        tx['mined'] = False
        tx['block_submitted'] = self.model.schedule.steps
        row = pd.DataFrame(tx, index = [self.tx_ct])

        self.tx_ct += 1
        self.mempool = self.mempool.append(row, ignore_index=True)

    def write_data(self, num_bytes):

        gwei_spent = self.gas_per_byte * num_bytes * self.gas_price
        return gwei_spent

    def mine_block(self):

        if self.model.verbose:
            print("Mining BLOCK NUMBER:", self.model.schedule.steps)
        self.chain.loc[self.model.schedule.steps] = [False for col in self.chain.columns]

        # Sort mempool to get highest-value transactions
        mp = self.mempool[self.mempool['mined'] == False].sort_values(by=['gas_spend', 'block_submitted']).reset_index()

        if len(mp) > 0:

            mp['cum_gas'] = mp['gas_spend'].cumsum()
            if mp['cum_gas'].max() > self.block_gas_limit:

                # If we cannot include all transactions in a block, fit as many as possible ...
                tx_mined = mp[0 : mp[mp['cum_gas'] > self.block_gas_limit].index[0]]

            else:
                tx_mined = mp[0 : ]

            if self.model.verbose:
                print("Mining", len(tx_mined), "out of", len(mp), "unvalidated transactions.\n")
                print("Gas value:", tx_mined['gas_spend'].sum(), '\n')

            for tx in tx_mined.iterrows():

                if self.model.verbose:
                    print("Mining tx id:", tx[1].tx_id)

                self.model.schedule._agents[tx[1].from_address].confirm_tx(tx[1])
                self.mempool.loc[self.mempool['tx_id'] == tx[1].tx_id, "mined"] = True
                self.mempool.loc[self.mempool['tx_id'] == tx[1].tx_id, "block_mined"] = self.model.schedule.steps

                self.chain.loc[tx[1].start_sync : tx[1].end_sync, tx[1].from_address] = True

        else:
            if self.model.verbose:
                print('Empty mempool')
            pass

        if self.model.verbose:
            print('Block #', self.model.schedule.steps, 'mined.\n\n')

    # Not used:
    def compute(self, num_seconds):
        gwei_spent = self.gas_per_second * num_seconds * self.gas_price
        return gwei_spent





class SensorBlockchainNetwork(Model):

    def __init__(self, num_sensors=20,
                 stochasticity=0.05,

       # Blockchain vars:
                 blockchain_gas_price=20,
                 block_gas_limit=9000000,
                 gas_per_byte=625,
                 gas_per_second=75000000,
                 avg_block_time=13,
                    # gas_per_byte and gas_per_second calculated based on
                    # https://hackernoon.com/ether-purchase-power-df40a38c5a2f

        # Sensor vars:
                 battery_life=1000,
                 record_cost=1, record_freq=1, record_bytes=32,
                 compute_cost_per_byte=1, info_reduction=1,
                 sign_cost=0.1,
                 transmit_cost_per_byte=1, transmit_freq=1,
                 sensor_gas_price=20,
                 mortal=True,

                 # Model vars:
                 verbose=False,
                 info_currency_window=1
                ):

        super().__init__()


        self.verbose = verbose
        if self.verbose:
            print('Verbose model')
        self.info_currency_window = info_currency_window
        self.running = True
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
                                model_reporters = {
                                    "active_sensors": get_active_sensors_at_current_tick,
                                },
                                agent_reporters = {
                                    "gwei_spent": 'gwei_spent',
                                    "battery_life": 'battery_life',
                                    "data_collected": get_total_data_collected,
                                    "informational_currency": get_informational_currency
                                })

        self.blockchain = Blockchain(self.next_id(), blockchain_gas_price, block_gas_limit,
                                    gas_per_byte, gas_per_second, avg_block_time, self)

        for i in range(num_sensors):
            sensor = Sensor(self.next_id(), battery_life, mortal,
                            record_cost, record_freq, record_bytes,
                            compute_cost_per_byte, info_reduction,
                            sign_cost,
                            transmit_cost_per_byte, transmit_freq,
                            sensor_gas_price,
                            self.blockchain, stochasticity, # << each sensor gets the same amount of stochasticity?
                            self)

            self.schedule.add(sensor)

        # Mine genesis block
        self.blockchain.chain.loc[1] = [False for col in self.blockchain.chain.columns]

        if self.verbose:
            print(num_sensors, "instantiated and added to schedule.")

    def step(self):
        self.schedule.step()
        if self.schedule.steps > 1:
            self.blockchain.mine_block()
        self.datacollector.collect(self)



# Reporter functions

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

def get_active_sensors_at_current_tick(model):
    return len([a for a in model.schedule.agents if np.isnan(a.dead)])

def get_total_data_collected(agent):
    return agent.db.sum()

def get_informational_currency(agent):
    """
    Calculate the proportion of data collected by a
    sensor that has been committed to the chain.

    **Note: This counts each tick as equal, even if
    different volumes of data were collected during
    the ticks.**

    Attributes:
        agent: The Sensor for which to calculate
            informational currency measure.
    """

    model = agent.model
    agent_id = agent.unique_id
    window = model.info_currency_window

    if window == 1 or window > len(model.blockchain.chain):
        try:
            return model.blockchain.chain[agent_id].value_counts()[True] / len(model.blockchain.chain[agent_id])
        except KeyError:
            return 0

    else:
        df = model.blockchain.chain[window * -1 :] # Last n rows
        try:
            return df[agent_id].value_counts()[True] / len(df[agent_id])
        except KeyError:
            return 0



# Post model run functions

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


def extract_network_life_cycle_from_batch_df(batch_df):
    return batch_df[[ 'num_sensors','record_bytes', 'record_freq', 'stochasticity', 'agent_expiry_ticks']]

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



# Output functions

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
