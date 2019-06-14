# Agent-based model outline

## Agents

A challenge we face in model design is that some agent types contain sets of other agent types, and these sets are dynamic. Put another way, a Ship agent could contain many Container agents, though the set of containers carried on a Ship changes upon load / unload. Our model will need to accommodate this hierarchical nature of the logistics system.

Our initial thought is to define an agent class for each type of informational entity involved in the system. This means, essentially, sensor-transceivers (edge devices), gateways, and servers, though the server architecture would likely be nested as well. These are the nodes in our network; edges represent connections between these nodes, i.e. transmissions of data.

For example, a set of containers might connect to a gateway, which would in turn transmit data describing its containers to a ship's server. The ship's server may transmit data to other ships, as well as to the shipping company (and / or maybe container owner?) servers. The containers, gateways and servers are nodes; the connections established between the nodes are network edges. (Corda)

The primary question we're asking relates to the dynamics of these data networks. If we presume that the questions surrounding how access is authorized are answered,

What are the characteristics of network behavior based on different access authorization / data access mechanisms? This has to do with privacy and security of information, and optimizing efficiency of device power usage (i.e. collection volumes / frequency, computing load and transmission volumes).

### Nodes 

The leaf nodes of the network - the "edge" - will be the sensors, and associated processors / transceivers, that collect the raw data. For our use case these can be thought of as the smart containers in the network, but this could be understood as any edge device - surveillance camera, autonomous vehicle, smart device, etc.

This raises a question crucial to our investigation: what unit of analysis serves as the 'leaf' of the network? To illustrate: depending on the level of abstraction, an autonomous vehicle could be considered the end node of a network. But if you look within the object itself, there is an entire nested hierarchy of sensors and data processor-transceivers - the steering system, media system, engine, etc etc. Even within one subsystem of the engine there may be dozens of sensors.

For our purposes we feel it is important to consider the actual sensor - that interfaces with the physical world, detecting some environmental attribute and converting it into binary data  - as the leaf node.



### Containers (i.e. leaf sensor-transceivers)
