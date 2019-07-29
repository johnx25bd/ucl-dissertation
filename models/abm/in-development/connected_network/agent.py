from mesa import Agent
import random
import pandas as pd
import numpy as np


class Sensor(Agent):
    """
    An empirical sensor with battery, data store,
    processor and information transceiver.

    Attributes:
        unique_id: Universally unique identifier. Here, a randomly generated id.
            This could be a wallet address or public key, plus private key
        pos: An (x,y) tuple of the connected sensor's spatial position
        sync_freq: The frequency with which the sensor syncs with the cloud.
            If float 0.0 < n < 1.0, this is the probability of syncing on a given tick.
            If int n >= 1, this sensor syncs regularly every n ticks.
        parent_gateway: The superior gateway ID that the sensor reports to.
        accuracy: A float value representing the difference between the observed
            and actual value
        precision: A float value representing the standard deviation of distribution
            of measurements around observed value


        # attributes: The types of sensors connected to the device,
        #     including "temperature", "moisture", "pressure",
        #     "orientation", "light".
        # battery_life: The amount of battery available. If -999, the sensor
        #     is considered to be connected to a stable power source.
        # storage: The amount of data storage available on device in GB
        #     (i.e. SD card size)
        # computer_power: The processor speed in MHz
        # schema: The format the data is collected in, to be used in measuring
        #     interoperability


    """

    def __init__(self, unique_id, pos, sync_freq, parent_gateway, accuracy, precision, model):

        super().__init__( unique_id, model)

        self.agent_type = "Sensor"
        self.unique_id = unique_id
        self.pos = pos
        self.sync_freq = sync_freq
        self.parent_gateway = parent_gateway # agent id ...
        self.accuracy = accuracy
        self.precision = precision

        actual = random.randint(0,100)

        self.state_updates = {"actual": actual, "observed": actual + 2}

        self.records = pd.DataFrame(columns = ['tick', 'actual', 'observed'])
        self.records.append({ "tick" model.schedule.steps,
                            "actual": actual,
                            "observed": actual + 2 })

    # def __init__(self, uuid, attributes, battery_life, storage, compute_power, schema, model):
    #     super().__init__(self, uuid, attributes, battery_life, storage, compute_power, schema, model)
    #
    #     self.uuid = uuid
    #     self.attributes = attributes
    #     self.battery_life = battery_life
    #     self.storage = storage
    #     self.compute_power = compute_power
    #     self.schema = schema
    #     self.recordings = []


    # def transmit(self):

    def step(self):
        """

        """
        # Add prior state update to database
        self.records.append(self.state_updates)

        # Replace with new recordings
        actual = random.randint(0,100)

        self.state_updates = {"actual": actual, "observed": actual + 2}

        if self.sync_freq < 1:
            if self.random.random() > self.sync_freq:
                pass
        else:
            if self.model.schedule.steps % self.sync_freq == 0:
                print(self.records)
                # self.transmit(self.parent_gateway, self.recordings)


    def record(self, actual):
        self.records.loc[self.model.schedule.steps, "actual"] = actual

        # Calculate recorded value based on actual and sensor accuracy and precision valuess
        observed = actual * np.random.normal(actual + self.accuracy, self.precision)
        self.records.loc[self.model.schedule.steps, "observed"] = observed # << inject error here

    def transmit(self, target_id, data):
        self.model._agents[target_id].receive(self.unique_id, data)

    def sync(self, requestor):

        # Transmit data to server or gateway
        # Store tick of most recent transmission to
        self.last_transmission = self.model.schedule.steps



class Gateway(Agent):
    """
    A computing node positioned between edge Sensors and the
    broader internet.

    Attributes:
        child_sensors: Sensors connected to the gateway, distal on the
            network tree
        storage: The amount of data storage available on device in GB
    """

    def __init__(self, unique_id, child_sensors, storage, parent_cloud, model):
        super().__init__(unique_id, model)

        self.agent_type = "Gateway"
        self.unique_id = unique_id
        self.child_sensors = {}
        self.storage = storage
        self.parent_cloud = parent_cloud

    def step(self):
        pass

    def receive(self, origin_id, data):
        self.child_sensors[origin_id].append(data)


class Cloud(Agent):
    """
    A centralized data storage and computing environment
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        self.agent_type = "Cloud"
        self.unique_id = unique_id






class Blockchain(Agent):
    """
    A decentralized data storage and computing environment
    """


# class TreeCell(Agent):
#     """
#     A tree cell.
#
#     Attributes:
#         x, y: Grid coordinates
#         condition: Can be "Fine", "On Fire", or "Burned Out"
#         unique_id: (x,y) tuple.
#
#     unique_id isn't strictly necessary here, but it's good
#     practice to give one to each agent anyway.
#     """
#     def __init__(self, pos, model):
#         """
#         Create a new tree.
#         Args:
#             pos: The tree's coordinates on the grid.
#             model: standard model reference for agent.
#         """
#         super().__init__(pos, model)
#         self.pos = pos
#         self.condition = "Fine"
#
#     def step(self):
#         """
#         If the tree is on fire, spread it to fine trees nearby.
#         """
#         if self.condition == "On Fire":
#             for neighbor in self.model.grid.neighbor_iter(self.pos):
#                 if neighbor.condition == "Fine":
#                     neighbor.condition = "On Fire"
#             self.condition = "Burned Out"
#
#     def get_pos(self):
#         return self.pos
