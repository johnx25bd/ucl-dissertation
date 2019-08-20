import math
import random
import pandas as pd
import numpy as np

from mesa import Agent

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

        # vvvv Unused variables vvvv #
        self.compute_cost_per_byte = compute_cost_per_byte
        self.info_reduction = info_reduction
        # ^^^^ Unused variables ^^^^ #

        self.sign_cost = sign_cost
        self.transmit_cost_per_byte = transmit_cost_per_byte
        self.transmit_freq = transmit_freq
        self.gas_price = gas_price
        self.blockchain = blockchain
        self.stochasticity = stochasticity

        self.gwei_spent = 0
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

    def __init__(self, unique_id,
                # gas_price,
                block_gas_limit,
                gas_per_byte, gas_per_second,
                avg_block_time, model):

        super().__init__(unique_id, model)

        if self.model.verbose:
            print("Blockchain created: ID", unique_id)

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

    def mine_block(self):

        if self.model.verbose:
            print("Mining BLOCK NUMBER:", self.model.schedule.steps)
        self.chain.loc[self.model.schedule.steps] = [False for col in self.chain.columns]

        # Sort mempool to get highest-value, then more recent, transactions
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
    def write_data(self, num_bytes):
        # ^^ Unused method?
        gwei_spent = self.gas_per_byte * num_bytes * self.gas_price
        return gwei_spent

    def compute(self, num_seconds):
        gwei_spent = self.gas_per_second * num_seconds * self.gas_price
        return gwei_spent
