from mesa import Agent
import random


class Sensor(Agent):
    """
    An empirical sensor with batter, data store,
    processor and information transceiver.

    Attributes:
        unique_id: Universally unique identifier. Here, a randomly generated id.
            This could be a wallet address or public key, plus private key
        pos: An (x,y) tuple of the connected sensor's spatial position
        sync_freq: The frequency with which the sensor syncs with the cloud.
            If n < 1.0, this is the probability of syncing on a given tick.
            If n > 1, this sensor syncs regularly every n ticks.

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

    def __init__(self, unique_id, pos, sync_freq, model):
        super().__init__( unique_id, model)

        self.agent_type = "Sensor"
        self.pos = pos
        self.unique_id = unique_id
        self.sync_freq = sync_freq
        self.state_updates = []
        self.records = []

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
        self.state_updates = random.randint(0,100)

        if self.sync_freq < 1:
            if self.random.random() > self.sync_freq:
                pass
        else:
            print(self.schedule.steps)



class Gateway(Agent):
    """
    A computing node positioned between edge Sensors and the
    broader internet.

    Attributes:
        child_sensors: Sensors connected to the gateway, distal on the
            network tree
        storage: The amount of data storage available on device in GB
    """

    def __init__(self, unique_id, child_sensors, storage, model):
        super().__init__(unique_id, model)

        self.agent_type = "Gateway"
        self.unique_id = unique_id
        self.child_sensors = child_sensors
        self.storage = storage

    def step(self):
        pass

class Cloud(Agent):
    """
    A centralized data storage and computing environment
    """

class Blockchain(Agent):
    """
    A decentralized data storage and computing environment
    """


class TreeCell(Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """
    def __init__(self, pos, model):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Fine"

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """
        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.condition == "Fine":
                    neighbor.condition = "On Fire"
            self.condition = "Burned Out"

    def get_pos(self):
        return self.pos
