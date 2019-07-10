import random

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import Grid

from .schedule import RandomActivationByBreed
from .agent import Sensor, Gateway, Cloud, Blockchain

# Measuring utility of data from network:
def compute_interoperability(model):
    """
    Compute the proportion of data adhering to
    """
    pass

def compute_accuracy(model):
    pass

def compute_accessibility(model):
    pass

def compute_speed(model):
    pass

# Network loads
# Transaction volumes

class CentralizedArchitecture(Model):
    """
    Simulating traditional cloud server web architectures including
    client-server relationship
    """

    def __init__(self, num_gateways, num_sensors,
                num_clouds, height=100, width=100):
        """
        Create a new model with centralized database architectures.

        """
        super().__init__()

        self.height = height
        self.width = width

        self.schedule = RandomActivationByBreed(self)
        self.grid = Grid(height, width, torus=False)

        self.datacollector = DataCollector(
            {"Temperature": lambda m: self.retrieve_state_updates(m)
            })

        # self.agents_by_breed = defaultdict(dict)

        for sensor in range(0, num_sensors):
            pos = (random.randint(0,width -1), random.randint(0,height -1))
            new_sensor = Sensor( self.next_id(), pos, 10, self)

            self.grid._place_agent(pos, new_sensor)
            self.schedule.add(new_sensor)


        for gateway in range(0, num_gateways):
            new_gateway = Gateway(self.next_id(), None, 0, self)

            self.grid._place_agent((0, gateway ), new_gateway)
            self.schedule.add(new_gateway)

    def step(self):
        print("STEP:", self.schedule.steps)
        self.schedule.step()
        self.datacollector.collect(self)

        # if self.duration <

    @staticmethod
    def retrieve_state_updates(model):
        state_updates = {}
        # # print(model.schedule.agents)
        # for breed in model.schedule.agents_by_breed:
        #     print(breed)
        #     state_updates[breed] = {}
        #     for agent in model.schedule.agents_by_breed[breed]:
        #         state_updates[breed][agent] = model.schedule.agents_by_breed[breed][agent].state_updates
        #     # recordings[sensor.pos] = sensor.recordings

        return state_updates

class PrivateBlockchainArchitecture(Model):
    """
    Simulating a permissioned blockchain data storage resource
    and trusted consortium

    """

class PublicBlockchainArchitecture(Model):
    """
    Simulating a permissionless system, including (possibly)
    decentralized public key infrastructure and peer to peer
    relationship
    """


# DEPRECATED, but retained for reference:
# class ForestFire(Model):
#     """
#     Simple Forest Fire model.
#     """
#     def __init__(self, height=100, width=100, density=0.65):
#         """
#         Create a new forest fire model.
#
#         Args:
#             height, width: The size of the grid to model
#             density: What fraction of grid cells have a tree in them.
#         """
#         # Initialize model parameters
#         self.height = height
#         self.width = width
#         self.density = density
#
#         # Set up model objects
#         self.schedule = RandomActivation(self)
#         self.grid = Grid(height, width, torus=False)
#
#         self.datacollector = DataCollector(
#             {"Fine": lambda m: self.count_type(m, "Fine"),
#              "On Fire": lambda m: self.count_type(m, "On Fire"),
#              "Burned Out": lambda m: self.count_type(m, "Burned Out")})
#
#         # Place a tree in each cell with Prob = density
#         for (contents, x, y) in self.grid.coord_iter():
#             if self.random.random() < self.density:
#                 # Create a tree
#                 new_tree = TreeCell((x, y), self)
#                 # Set all trees in the first column on fire.
#                 if x == 0:
#                     new_tree.condition = "On Fire"
#                 self.grid._place_agent((x, y), new_tree)
#                 self.schedule.add(new_tree)
#
#         self.running = True
#         self.datacollector.collect(self)
#
#     def step(self):
#         """
#         Advance the model by one step.
#         """
#         self.schedule.step()
#         # collect data
#         self.datacollector.collect(self)
#
#         # Halt if no more fire
#         if self.count_type(self, "On Fire") == 0:
#             self.running = False
#
#     @staticmethod
#     def count_type(model, tree_condition):
#         """
#         Helper method to count trees in a given condition in a given model.
#         """
#         count = 0
#         for tree in model.schedule.agents:
#             if tree.condition == tree_condition:
#                 count += 1
#         return count
