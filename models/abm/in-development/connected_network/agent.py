from mesa import Agent



class Sensor(Agent):
    """
    An empirical sensor with batter, data store,
    processor and information transceiver.

    Attributes:
        uuid: Universally unique identifier. Here, a randomly generated id.
            This could be a wallet address or public key, plus private key
        pos: An (x,y) tuple of the connected sensor's spatial position
        attributes: The types of sensors connected to the device,
            including "temperature", "moisture", "pressure",
            "orientation", "light".
        battery_life: The amount of battery available. If -999, the sensor
            is considered to be connected to a stable power source.
        storage: The amount of data storage available on device in GB
            (i.e. SD card size)
        computer_power: The processor speed in MHz


    """

    def __init__(self, uuid, attributes, battery_life, storage, compute_power, model):
        super().__init__(self, uuid, attributes, battery_life, storage, compute_power, model)

        self.uuid = uuid
        self.attributes = attributes
        self.battery_life = battery_life
        self.storage = storage
        self.compute_power = compute_power


    def step(self):
        """

        """

class Gateway(Agent):
    """
    A computing node positioned between edge Sensors and the
    broader internet.

    Attributes:
        child_sensors: Sensors connected to the gateway, distal on the
            network tree
        storage: The amount of data storage available on device in GB
    """

    def __init__(self, child_sensors, storage):
        super().__init__(self, child_sensors, storage)

        self.child_sensors = child_sensors
        self.storage = storage

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
