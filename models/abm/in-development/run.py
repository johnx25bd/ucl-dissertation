# from connected_network.server import server
from connected_network.model import CentralizedArchitecture

ca = CentralizedArchitecture(1,2,3,10,10)

for i in range(0,20):
    ca.step()
# ca.step()


# print('SERVER WILL NOT RUN - it is not configured')
# server.launch()
