# Draft ODD Protocol

Agent-based modeling of interactions of participants of a connected sensor network.

## Overview

### Purpose

The purpose of this model is to investigate the informational dynamics of connected sensor networks. The Internet of Things holds promise of improving situational awareness to unprecedented scales and resolutions (cite). If leveraged properly, enormous systemic efficiency gains could be uncovered by a more accurate understanding of system patterns and dynamics - with substantial environmental and commercial implications. However, to tap this potential robust mechanisms for data governance must exist, to ensure that appropriate actors have access to appropriate information at appropriate times.

Data is not actionable; only once its meaning (the information contained) is perceived by entities whose behavior is affected by the meaning carried does the opportunity latent in a network of connected sensors begin to be unlocked. This research intends to investigate the dynamics of such a system, with a particular focus on decentralized governance mechanisms. Specifically, we will investigate how edge device accuracy (which can be affected by variability in sensors, malicious behavior and so on) affects aggregate informational accuracy. This is important as these data feeds, plus aggregated data,  are increasingly being used to inform important regulatory and business monitoring and decision-making ranging from assessing eligibility for crop insurance payout for small-holder farmers in developing countries (IBISA) to monitoring nuclear weapons production facilities in compliance with international treaties (National Academies Press 2005 https://www.nap.edu/read/11265/chapter/2#6). More and more of our systems and processes are coming to rely on information collected by connected sensors.

We intend to investigate the trustworthiness of such information, and to assess the emergent behavior of such information networks based on various data governance models. Our hope is that developing such an understanding now will enable us to engage in the in technical, economic and regulatory development of such capacity with a greater awareness of the possible consequences of system design.

Frankly, I am hesitant to do this, because we have no datasets with which to validate our models, and are generally making them up as we go. However, acknowledging the constraints of the approach, I hope to better understand such a system and, possibly, behaviors that may emerge.

*Dr Wilson - How to validate models - most are not validated generally.*

*Life cycle cost of blockchain. Solving this with edge computing and trusted computing environments. Insights into these costs - to inform system design and balance resource ues. For every megabyte, $x*

*Could a model be used to predict data loads based on network size, transaction rates etc.*


### State variables and scales

These models will be composed of individual agents representing the computing nodes connected to an information transfer network such as the Internet. Nodes can be autonomous (i.e. installed with software that executes when certain conditions are met or events occur), or controlled by human operators. Each agent is assumed to have an identity on the network (which must include an address), and be able to send and receive data.

Our goal is to model centralized, distributed and decentralized data access and governance mechanisms to better understand the characteristics of each, and how system dynamics might behave as such networks scale.

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
(Use each of these to calculate Energy usage)

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

Cloud repositories are informational architectures including code and data storage infrastructure with persistent connectivity to the Internet and effectively unbound computing capacity. These may exist in centralized (i.e. traditional server-database systems such as LAMP or MEAN) or decentralized data stores (i.e. on the "web3" stack, in which data is stored or anchored on blockchains and business logic is encoded into smart contracts - also stored on blockchains). Critically, this model seeks to investigate dynamics of various cloud repository systems, including centralized and consortium private and public blockchain architectures. We are especially curious as to how decentralized autonomous organizations (cite) might be used to govern information access controls.

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

## Details

### Initialization

### Input

### Submodels

Content vs location addressing
  Essentially, what happens if x% of data you try to access is no longer available?
