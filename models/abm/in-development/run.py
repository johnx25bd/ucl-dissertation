# from connected_network.server import server
from connected_network.model import CentralizedArchitecture

ca = CentralizedArchitecture(2,10,10,10,10)

ca.step()
ca.step()


# print('SERVER WILL NOT RUN - it is not configured')
# server.launch()
