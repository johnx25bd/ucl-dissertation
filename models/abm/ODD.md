# Draft ODD Protocol

Agent-based modeling of interactions of participants of a connected sensor network.

## Overview

### Purpose

The purpose of this model is to investigate the informational dynamics of connected sensor networks. The Internet of Things holds promise of improving situational awareness to unprecedented scales and resolutions (cite). If leveraged properly, enormous systemic efficiency gains could be uncovered by a more accurate understanding of system patterns and dynamics - with substantial social, environmental and commercial implications. However, to tap this potential robust mechanisms for data governance must exist, to ensure that appropriate actors have access to appropriate information at appropriate times.

Data is not actionable: only once its meaning (the information contained) is perceived by entities whose behavior is affected by the meaning discerned does the opportunity latent in a network of connected sensors begin to be unlocked. This research intends to investigate the dynamics of such a system, with a particular focus on decentralized governance mechanisms.

Specifically, we will investigate how edge device accuracy (which can be affected by variability in sensors, malicious behavior and so on) affects aggregate informational accuracy. This is important as these data feeds, plus aggregated data,  are increasingly being used to inform important regulatory and business monitoring and decision-making ranging from assessing eligibility for crop insurance payout for small-holder farmers in developing countries (IBISA) to monitoring nuclear weapons production facilities in compliance with international treaties (National Academies Press 2005 https://www.nap.edu/read/11265/chapter/2#6). More and more of our systems and processes are coming to rely on information collected by connected sensors (citation).

We intend to investigate the trustworthiness of such information, and to assess the emergent behavior of such information networks based on various data governance models. Our hope is that developing such an understanding now will enable us to engage in the in technical, economic and regulatory development of such capacity with a greater awareness of the possible consequences of system design.

Frankly, I am hesitant to do this, because we have no datasets with which to validate our models, and are generally making them up as we go. However, acknowledging the constraints of the approach, I hope to better understand such a system and, possibly, behaviors that may emerge.

*Dr Wilson - How to validate models - most are not validated generally.*

*Life cycle cost of blockchain. Solving this with edge computing and trusted computing environments. Insights into these costs - to inform system design and balance resource ues. For every megabyte, $x*

*Could a model be used to predict data loads based on network size, transaction rates etc.*


### State variables and scales

These models will be composed of individual agents representing the computing nodes connected to an information transfer network such as the Internet. Nodes can be autonomous (i.e. installed with software that executes when certain conditions are met or events occur), or controlled by human operators (i.e. PCs or smartphones). Each agent is assumed to have an identity on the network (which must include an address - think MAC address), and be able to send and receive data to and from other connected nodes.

Our goal is to model centralized and decentralized data access and governance mechanisms to better understand the characteristics of each, and how system dynamics might behave as such networks scale. Agent characteristics are similar in both configurations; the path of information transfer differs. The centralized structure will simulate a client-server model of networked computing; the decentralized mechanism will simulate a peer-to-peer

#### Connected sensors

A primary agent in the proposed model is the connected sensor, defined as an empirical sensor (i.e. one that measures some physical characteristic of its environment such as temperature, sound, light, chemistry, orientation, force, and / or time) capable of digitizing such measurements and transmitting data to other computing nodes connected to the network. Beyond the processing capability (including power source) and information transceiving equipment required to meet these criteria, some quantity of digital storage is usually installed on the device, allowing a persistent record of such data to be kept. Often, though not always, these devices are constrained both in the computational power and RAM contained on the device (limiting the speed and types of computations possible), and in the energy available to perform such computations before depletion of the battery. As such, it is often infeasible to transfer the full raw dataset collected by such connected sensors to a centralized repository unbound by these computational constraints. These factors demand a level of creativity, to balance system characteristics in tension with each other, accounting for technical, environmental, commercial, political and ethical factors.

For the purposes of this investigation, the "edge" is defined as the interface between the physical environment and the informational one, i.e., the physical sensors that convert analogue qualities to digital signals. A distinction may be necessary between connected sensors designed for physical interact with users (smartphones, wearable IoT, some vehicles, appliances) and those that are not (air quality monitors, satellites, surveillance cameras, embedded sensors). The terms "edge devices",  "edge sensors", "Connected sensors" and so on will be used interchangeably.

**State Variables:**
- Computational processing
  - Different algorithms will have different costs
    - Descriptive statistics - mean, median, quartiles, standard deviation, etc  
    - Classification (ML on the edge - not training the model)
    - Encryption, decryption, signing, verifying
- Data transmission
- Data receipt
(Use each of these to calculate Energy usage, Disk usage and Bandwidth usage)

- Measured dimensions, based on onboard empirical sensors (temperature, force, moisture,  chemicals, light, sound (air pressure), time)
- Location
  - Use to determine direction of travel and velocity
  - Calculated from connection with (4+) other devices and measuring time required for data transfer

**Actions:**
- Measure sensor reading
- Transmit request
- Process received packet
- Compute data
- Write to database
- Delete from database

#### Gateways

Gateways serve as the interface between a local network of connected sensors. Gateways will be considered to have a reliable power source and greater computational, memory, storage and connectivity capacity than most edge sensors.

**State Variables:**
- Number of requests
- Number / volume of transmissions
- Computational load (based on computation of sensor data and processing of requests)

From these, derive
- Power usage
- Bandwidth usage
- Storage capacity
- Utilized storage

**Actions:**
- Transmit request
- Process received packet
- Compute data
- Write to database

#### Cloud repositories

Cloud repositories are informational architectures including code and data storage infrastructure with persistent connectivity to the Internet and effectively unbounded computing capacity. These may exist in centralized (i.e. traditional server-database systems such as LAMP or MEAN) or decentralized data stores (i.e. on the "web3" stack, in which data is stored or anchored on blockchains and business logic is encoded into smart contracts - also stored on blockchains). Critically, this model seeks to investigate dynamics of various cloud repository systems, including centralized and consortium private and public blockchain architectures. We are especially curious as to how decentralized autonomous organizations (cite) might be used to govern information access controls.

**State Variables:**

- Energy usage
- Disk space usage
- Computational resource usage
- Bandwidth usage
- Communications packets sent and received

**Actions:**
- Transmit request
- Process received packet
- Compute data
- Write to database

**Questions:**

*What are the limits of the on chain computational costs?*

*People request data from a data store - preprocessed at some level. Quite rare to actually speak to gateway. Systems set up to capture information of a certain type - info is presented to them in a precompiled form.*

*Julie McCann - autonomous systems from a database background. Distributed datasets.*

#### Human agents

The final agent participating in the system is the computing node controlled by a human operator - i.e. PC or smartphone. Such an operator may request data, either from edge devices, gateways or cloud servers, or seek to write to devices - either overwriting collected data (perhaps fraudulently) or installing code on  edge devices to operate their systems and their behavior on the network.

#### Actuators

Devices that act based on some signal.

#### Higher-order entities

Organizational entities will own, control or access groupings of these individual agents; we seek to investigate the dynamics of such relationships. Companies, private individuals, governments (and subsidiary government agencies or departments), and non-profit or third sector organizations each may own, control or seek access to connected devices on the network. We intend to model events that may rely on the distinction between device ownership; for example, perhaps a cyber attack would only affect devices operated by Company A, as the  vulnerability was only present on code running on those devices.

#### Spatial proximity

Devices are also related to one another by distance, or containment within certain geometries (i.e. a country's borders, or a port facility). We may simulate certain events that affect agents based on location, such as a natural disaster or dirty bomb, which may affect all computing resources within a radius of a certain point.

### Process overview and scheduling

The order of events taking place may substantially affect system behavior (Comer 2014 - Who Goes First?).

**?? How does this actually work? What is the process an edge device proceeds through in order to provide data to a requestor? How long does this take? Does data transfer time need to be incorporated into the model? How long is one tick?!?**

#### Critical events to schedule:

[] Record measurement (Sensor)
[] Transmit request (Gateway, Cloud, Blockchain)
[] Transmit data (Sensor, Gateway, Cloud, Blockchain (?) as scheduled or in response to a request)
[] Perform computation (Sensor, Gateway, Cloud, Blockchain)
[] Update database - write or delete

It is unclear how activation order will impact model behavior, and how activating agents of different types prior or subsequent to others might affect outcomes. As this is not the focus of our investigation, and typical networks do not have a coordination regarding timing of actions taken by different network nodes, we have opted to randomize all agents each tick, then activate each sequentially. This is "generally the default behavior for an ABM" (Mesa 2019), and most closely simulates how we understand computing networks to function (citation?). Various scheduling approaches may impact emergent system dynamics; however, the exploration of this is beyond the scope of this research.

### Design concepts

In our effort to design a middle range model (Gilbert 2008 Agent-Based Models) focused on simulating key system attributes, we were forced to select which behaviors and characteristics to include and which to exclude. Bias is introduced into our analysis through uninformed emphasis of certain aspects of the system over others, but a level of abstraction is necessary to conduct this analysis given resource and time constraints.

Our investigation seeks to model the behavior of a complex network of computing nodes based on the relatively simple behavior of each network participant. It is not, however, "adaptive": in our model agent behavior does not adjust in response to experience. Our goal is instead to understand the effect of levels of centralization on system dynamics.

Relevant design concepts:

#### Fitness



## Design

### Input parameters

- Frequency / condition of data transmission
- Amount of edge computation (battery - data load trade-off)
- Route of request (via server, peer to peer)
- Form of compromise (error, offline)
- Number and attributes (i.e. battery capacity, compute capacity, etc) of nodes

### Simulated events

- Miscalibrated sensors
- Organizational sensor compromise (non-spatial)
- Local sensor compromise (spatial)

### Variables to report

- Number of interactions experienced by each node (requests and transmissions)
- Resource consumption on device (calculated from computation volume, transmission volume, data collection volume / frequency) (reported as battery level - could simulate energy regeneration from, for example, an attached solar cell)
- Quantity of data transferred
- Actual vs reported data and aggregate statistic accuracy
- Number of sensor "deaths" (depletion of battery to 0)


#### Measure of network efficiency

Computing usage per tick
Bandwidth usage per tick (volume / quantity of data - does location matter?)
^^ Combine to estimate energy usage per tick

**?? Questions regarding need to simulate relay of data along network, or are all nodes topologically adjacent - can they all connect to all others ?**

#### Measure of network resiliency

Number of nodes operational per tick
Informational accuracy each tick (based on sweep of update frequencies - probabilistic and uniform)
Informational resolution each tick (proportion of sensors / nodes represented / accessible - based again on sweep of update frequencies.)

#### Measure of informational accuracy

Comparison of observed vs actual environmental dimensions from network.
- Need some master record of true values to compare observed values to ...
- Expressed as observed / actual. > 1 means overestimated, < 1 means underestimated. 1 is perfect accuracy ...
- Sweep sampling frequency (temporal and spatial)

#### Measure of informational interoperability *

Quantify proportion of data that is cross-comparable due to adherence to some protocol / standard. (* If there is time)

## Details

### Initialization



### Input

### Submodels

Content vs location addressing
  Essentially, what happens if x% of data you try to access is no longer available?







### *DEPRECATED* ---vvvvvv---

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
