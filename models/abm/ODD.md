# Draft ODD Protocol

Agent-based modeling of interactions of participants of a connected sensor network.

## Overview

### Purpose

The purpose of this model is to investigate the informational dynamics of connected sensor networks. The Internet of Things holds promise of improving situational awareness to unprecedented scales and resolutions (cite). If leveraged properly, enormous systemic efficiency gains could be uncovered by a more accurate understanding of system patterns and dynamics - with substantial environmental and commercial implications. However, to tap this potential robust mechanisms for data governance must exist, to ensure that appropriate actors have access to appropriate information at appropriate times. Data is not actionable; only once its meaning (the information contained) is perceived by entities whose behavior is affected by the meaning carried does the opportunity latent in a network of connected sensors begin to be unlocked. This research intends to investigate the dynamics of such a system, with a particular focus on decentralized governance mechanisms. Specifically, we will investigate how edge device accuracy (which can be affected by variability in sensors, malicious behavior and so on) affects aggregate informational accuracy. This is important as these data feeds, plus aggregated data,  are increasingly being used to inform important regulatory and business monitoring and decision-making ranging from assessing eligibility for crop insurance payout for small-holder farmers in developing countries (IBISA) to monitoring nuclear weapons production facilities in compliance with international treaties (National Academies Press 2005 https://www.nap.edu/read/11265/chapter/2#6). More and more of our systems and processes are coming to rely on information collected by connected sensors.

We intend to investigate the trustworthiness of such information, and to assess the emergent behavior of such information networks based on various data governance models. Our hope is that developing such an understanding now will enable us to engage in the in technical, economic and regulatory development of such capacity with a greater awareness of the possible consequences of system design.

Frankly, I am hesitant to do this, because we have no datasets with which to validate our models, and are generally making them up as we go. However, acknowledging the constraints of the approach, I hope to better understand such a system and, possibly, behaviors that may emerge.

### State variables and scales

These models will be composed of individual agents representing the computing nodes connected to an information transfer network such as the Internet. Nodes can be autonomous (i.e. installed with software that executes when certain conditions are met or events occur), or controlled by human operators. Each agent is assumed to have an identity on the network (which must include an address), and be able to send and receive data.

Our goal is to model centralized, distributed and decentralized data access and governance mechanisms to better understand the characteristics of each, and how system dynamics might behave as such networks scale.

#### Connected sensors

A primary agent in the proposed model is the connected sensor, defined as an empirical sensor (i.e. one that measures some physical characteristic of its environment such as temperature, sound, light, chemistry, orientation, force, and / or time) capable of digitizing such measurements and transmitting data to other computing nodes connected to the network. Beyond the processing capability (including power source) and information transceiving equipment required to meet these criteria, some quantity of digital storage is usually installed on the device, allowing a persistent record of such data to be kept. Often, though not always, these devices are constrained both in the computational power and RAM contained on the device (limiting the speed and types of computations possible), and in the energy available to perform such computations before depletion of the battery. As such, it is often infeasible to transfer the full raw dataset collected by such connected sensors to a centralized repository unbound by these computational constraints. These factors demand a level of creativity, to balance system characteristics in tension with each other, accounting for technical, environmental, commercial, political and ethical factors.

For the purposes of this investigation, the "edge" is defined as the interface between the physical environment and the informational one, i.e., the physical sensors that convert analogue qualities to digital signals. A distinction may be necessary between connected sensors designed for physical interact with users (smartphones, wearable IoT, some vehicles, appliances) and those that are not (air quality monitors, satellites, surveillance cameras, embedded sensors). The terms "edge devices",  "edge sensors", "Connected sensors" and so on will be used interchangeably.

#### Gateways

Gateways serve as the interface between a local network of connected sensors. Gateways will be considered to have a reliable power source and greater computational, memory, storage and connectivity capacity than most edge sensors.

#### Cloud repositories

Cloud repositories are informational architectures including code and data storage infrastructure with persistent connectivity to the Internet and effectively unbound computing capacity. These may exist in centralized (i.e. traditional server-database systems such as LAMP or MEAN) or decentralized data stores (i.e. on the "web3" stack, in which data is stored or anchored on blockchains and business logic is encoded into smart contracts - also stored on blockchains). Critically, this model seeks to investigate dynamics of various cloud repository systems, including centralized and consortium private and public blockchain architectures. We are especially curious as to how decentralized autonomous organizations (cite) might be used to govern information access controls.

#### Human agents

The final agent participating in the system is the computing node controlled by a human operator - i.e. PC or smartphone. Such an operator may request data, either from edge devices, gateways or cloud servers, or seek to write to devices - either overwriting collected data (perhaps fraudulently) or installing code on  edge devices to operate their systems and their behavior on the network. 

### Process overview and scheduling

## Design


## Details

### Initialization

### Input

### Submodels
