from .Agents import *

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import Grid
from mesa.time import RandomActivation

from .reporters import *

class SensorBlockchainNetwork(Model):

    def __init__(self, num_sensors=20,
                 stochasticity=0.05,

           # Blockchain vars:
                 # blockchain_gas_price=20,
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

        self.blockchain = Blockchain(self.next_id(),
                                    # blockchain_gas_price,
                                    block_gas_limit,
                                    gas_per_byte,
                                    gas_per_second,
                                    avg_block_time,
                                    self)

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
