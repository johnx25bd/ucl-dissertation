# Dissertation Proposal

We are living as part of a phenomenon, in which objects exist in space and move forward through time. We are objects - physical bodies maintaining the cycles that keep us alive, and we perceive and interact with other objects, living, animate and inanimate in our experience.

Each object is distinct, either discrete or constituent to a discrete object - in fact, every object is at once its own and a constituent part of a superior, containing object. This is perhaps a bit pedantic but the need for deliberate and concise definition of the terms we will use will become apparent, hopefully.

Infinite distinctions between objects can be found, but it is incredibly infrequent for any object to occur only once - as a result of natural interactions or the application of work by a living thing usually they form in numbers, sometimes very great numbers. We perceive these distinctions and call these objects by their class name - staplers or rocks or mountains or airplanes or pancakes. Each instance is distinct, unique, but the similarities we perceive allows us to learn from and interact with our environment in a way to seek and avoid that should be sought and avoided in order for us to survive. We see pancakes, we look at them, maybe smell them, and know we probably can eat them, because we've encountered pancakes before or someone explained what they are and that they are edible (but best with maple syrup).

We will touch upon the distinctions between objects (probably in an annex or something) and the whole-part nature of everything in the manifest universe, including the manifest universe (which is the ultimate whole that includes us and everything we interact with - its constituent parts).

But to avoid being remiss any longer, we must clarify: it appears that the physical object is only part of an entity. A very important thing is contained within a physical object, something that is not separate: the subject. This is the meaning about the object, as understood or interpreted within some perceiving or sentient entity (object-subject pair).

This object-subject pair cannot be separated, though it stands to reason that the subjective aspect can actually survive much longer than the physical one. Every object has a subject, however rudimentary it might be, or at least every object that is composed of matter that has been encountered or conceived of by sentient life forms - and unsure about this, but every subject at least once had an object, or maybe must have one at all times (even if the object is some information stored in persistent state that would need to be decoded to be interpreted). The subjective aspect of an entity (which includes both physical and conceptual or subjective aspects) is immensely complex, dependent on others' (again, perceiving entities) perceptions of the entity through direct interaction, interaction with their image or word of mouth (more?) - impossible to quantify fully . infinite probably.

As entities with agency and sentience - a population of instances of a class (human being) - we are unique in our level of awareness and ability to act intentionally, conceiving of the consequences of our actions with considerable sophistication. We each have attributes - our physical dimensions and measurements, but also attributes that exist in the conceptual space, or emotive space (we will probably need to get into this quite thoroughly - the structure of the subjective space - concepts, feelings, ideas, symbols, etc). We know these about ourselves and can communicate them to others by transmitting or recording symbols, sounds or gestures that mean something to that which perceives, some time (always) in the future. Understanding the behavioral dynamics of the fundamental units in each of these spaces is critical to this research effort as it will form the basis for decision-making in the proposed restructuring of the physical-informational configuration in which objects in the human domain exist.

Obviously the vast vast vast vast vast majority of information (about anything, let alone everything) is unperceived and unrecorded. The envelope within the informational space (which is really the focus of this dissertation, the transmission and reception of meaning by matter - and the incredible interface between the two) which contains meaning interpretable by some one or some thing ... and, crucially - the *right* some one or some thing(s).

We intend to investigate the feasibility of a system of situationally aware secure objects able to detect, process, record and transmit information. Situational awareness means detection of environmental factors (internal and external to the object) and position in space relative to some meaningful origin.

We'd like to understand the intricacies of these processing sensors, how to build them and what challenges arise in achieving a system with minimum functionalities
- Detect and transmit location
- Detect and transmit interior, exterior temperature
- Detect and transmit interior and exterior moisture
- Accelerometer
- Detect breach in integrity of the object's surface

Perhaps even less for an MVP

Concurrently, we will be investigating the status of trusted hardware. Our idea is to create some process by which a private key can be generated on board this device that will never be revealed in plaintext format to any other entity (person or machine) but is processable by the device. Detecting a breach in the integrity of the case could be a critical backstop as it would enable any inforation (transactions) signed with that key to be invalidated from that point forward. But if this is possible, to reliably imbue machines with private keys unknown to any other object (and similarly, securely establish a one-to-one link between a person and a decentralized identifier), it may enable a profound shift to occur in the way we interact.

A metaphor I've been considering since I was on the beach at Famara: as water cools, the non-cooperative equilibrium of its constituent molecules persists, slowly changing perhaps as temperature decreases. Then, on the edge, ice begins to form - the water molecules are slowing enough for the hydrogen bonds to overpower its intrinsic energy ... a structure, ordered coherence is created from a volume of these molecules - entities - by adjusting the environment in which it exists.

I wonder if a similar phenomenon might occur as we near saturation of information transfer, but between entities in the physical/informational space. If understand improves, entities are less likely to act in a way that would disrupt another's intentions (unless their intentions are competing and overwhelm the risk of resistance or disagreement). In a situation of abundance of physical resources, with a proper configuration of incentives, perfect deconfliction of intentions between all interacting agents may be possible. i.e. a cooperative Nash equilibrium (right? I never studied game theory lol)

Ice is already forming at the edges of human society, and has been forming for millennia or longer or forever. Life coordinates to survive as much as it competes. In fact, the most successful communities (depending on the definition of success) of living organisms are the ones that coordinate best. For agents - people, plus machines - to coordinate properly there must be clearly defined ways in which they can communicate, that is, transmit meaning to other. We will briefly summarize the nature of information transmission and storage to ensure an accurate understanding, including analog, audio and binary information streams / sequences. By understanding how meaning is perceived, interpreted, and stored or communicated to be interpreted again in the future (be it centuries or nanoseconds) we hope to understand how a system of perfect coordination between human and computing entities might function.

Modeling this will entail creating spaces to allow the interaction between humans and machines

| | human | machine |
|---|---|---|
| human | image, spoken word, body language, written or recorded symbols (language, sensed data (audio and image recordings)) | code |
| machine | keyboard, mouse, camera, microphone, ports / browser, OS, speakers, screen | binary data, transmitted (requests, API, sensor or input) or persistent (on disk, in RAM, from sensor, from port) |


Something along those lines.

Understanding that information is encoded into matter (including electromagnetic radiation / some wave) and information contains meaning, and validity of information is a concern, how might we be able to create this system where we can trust the data it is collecting and transmitting? Again, to do with the private key, and each object containing its own blockchain, of which the merkle root / ipfs hash is registered on a global chain at some time interval. In this way privacy and integrity can be maintained and we can have a dataset that we can trust - perhaps not accurate or of variable precision, but some data about the experience of that sensor.

Here is an opportunity for edge computing - on-board algorithms process raw sensor input data, stores it (or some condensed version) on board, and transmits some summary to some authority (likely contract which then writes it to a globally-available persisstent storage). At any point - if required (and contracts could be configured to manage permissions - who is allowed to get data at what level of aggregation for what reason, even what purpose) the more granular data could be transmitted from the connected device upon next connection (i.e. receipt of request). Algorithms installed on the device (perhaps governed by some mechanism as described earlier or later) then are passed input data feeds to create whatever outputs they are programmed to provide, and output them as programmed (i.e. to disk or to transmission).

We have not spent too much time considering the opportunities created by such a physical-informational configuration of objects, but we suspect they may be broad. First of all, of course, are applications to global trade and supply chains. The level of situational awareness accessible to (let alone perceived by) humans regarding the maritime space is deeply constrained by the vastness of the ocean and maritime transport-related infrastructure and assets as well as, we believe, an inherent bias towards the way things are - poorly governed, even more poorly enforced. This is even in developed countries, but especially in developing ones. In a globalized world a unified system is demanded. Private firms and even sovereign governments lack the incentive to develop such a unified system (due to perceptions by leaders that they are operating in an adversarial worldspace), so no one has been. Initiatives to make interoperable the metarecords of maritime trade have been in effect since maritime trade began (surely), but they were always regional, between sets of actors, not amongst all actors.

Consider something as simple as a bill of lading. This document is required with all international freight transfers across national (and probably state or provincial) borders - I believe it violates the law for some commercial shipment not to have a BOL. These are slips of paper with ID numbers, company names, contact details, information about the contents of the container or ship, etc. This paper (registered where? I think with the freight forwarder or original company that purchased the shipping service - but not anywhere global, right?) (?) is required in compliance operations for purchase of insurance or obtainment of trade finance. We have no global database of trade - container or commodity flows. We have even less of an idea of who owns the companies engaging in the system, and very very often (in our understanding) the documents do not accurately or fully describe the contents of the shipment, either due to laziness or fraudulence.

My intuition is that this enables the movement of enormous quantities of harmful or deadly objects. The primary use case under investigation is that of arms and munitions as they are made, transferred and deployed on Earth. We glean that many of the people dying as a result of intentional human violence are being killed by people brandishing legally made weapons and ammunition that was diverted from its intended end user to its actual one, in violation of export control regimes (or due to ambiguous end user certificates and lax auditing and compliance enforcement). If we can create a system that securely tracks these assets from origin to destination and beyond, using the system of secure cases along with (ideally) deterministic biometric identification and use of decentralized identifiers to enable individual sovereignty over produced data (A Primer for Decentralized Identifiers p4) - by creating a one-to-one link between an entity and its on-chain metadata and metalogic, the reality of individual uniqueness of objects in our awareness can be reflected. (Note that exploration of this topic is likely beyond the scope of this dissertation, but we have observed that people very often confuse *similarity* of physical objects with *sameness*. Distinct physical objects can be similar - nearly identical. But they are never the same, just by being two. Sameness can exist in the conceptual space, however - an important distinction between the two.)

The mathematical proofs will be beyond the scope of this initial effort, but we hope to design a provably secure system of integrity of intention - all agents in the system are not lying or deceiving, a system antifragile to deceit and malicious behavior. The only way we can imagine to do this is to create a publicly-governed code base that is deployed to this network of connected things. All code would be open source, examinable by anyone able to interpret. Consensus found amongst those people (and possibly software agents) would determine which versions of software are approved to be executed on board these secure devices. As ice forms at the edge, we envision secure zones, where everything is on chain, declared, transparent. We suspect gains to physical security may be enormous - and these gains may be won while respecting the right to privacy (again, reliant on secure and trusted computing environments on board sensors / devices, including perhaps application of fully homomorphic encryption techniques for data processing). Even to imagine the machine context: secure containers packed in secure facilities, provided an unauthorized breach is not detected somewhere in the chain of custody, can be reliably tracked along its journey. The DID - metadata attached to information perceptible by scanning some ID (again, reliably) affixed to or exposed on the object - would offer an interface to retrieve data about the object, and to process it accordingly. This is worth further investigation - rather than centrally-directed logistics coordination architectures, model a more TCP/IP-like packet routing system: containers have data on board about where they are going and when they should arrive and logic can be built into the transhipment process to optimize the system-wide efficiency.

As an aside, there may be opportunity to create a publicly-funded, owned and governed physical-informational architecture to provide competitively-priced near realtime earth observation data. This would entail creating a DAO designed to raise and disburse funds to purchase the physical assets and secure the attention and efforts of qualified administrators of the assets to maintain their active status sensing, recording and transmitting data. But we don't see any reason why an ecosystem for players offering these services / capabilities couldn't be established. This would serve as a valuable asset to scientists working to understand present conditions and action while we wait (advocate) for the world's informational resources to be transferred to the public or self-sovereign domain. (DigitalGlobe, Facebook, Google, etc), in accordance with the desires of the owners and subjects of that data, naturally. Over time we suspect that these DAOs may be a way for digital democracies oriented towards management of funds (i.e. collectively-governed investment vehicles) to purchase and assume control of private, centralized firms that administer many of the fundamental infrastructures supporting human life, not just earth-observing.  

> A Decentralized Identifier (DID) is a new type of identifier that is globally unique, resolveable with high availability, and cryptographically verifiable. (A Primer for Decentralized Identifiers p1)

> For self-sovereign identity, which can be defined as a lifetime portable digital identity that does not depend on any centralized authority, we need a new class of identifier that fulfills all four requirements: persistence, global resolvability, cryptographic verifiability, and decentralization. (Ibid. p4)


> The purpose of the DID document is to describe the public keys, authentication protocols, and service endpoints necessary to bootstrap cryptographically- verifiable interactions with the identified entity. (Ibid. )

> DID infrastructure can be thought of as a global key-value database in which the database is all DID- compatible blockchains, distributed ledgers, or decentralized networks. (Ibid. 4. DID Documents p5)

> DIDs and DID documents can be adapted to any modern blockchain, distributed ledger, or other decentralized network capable of resolving a unique key into a unique value. It does not matter whether the blockchain is public, private, permissionless, or permissioned. (A Primer for Decentralized Identifiers 5. DID Methods p5)



We see many ways to empirically approach understanding the system we are describing, through agent-based and classical modeling.

Agent-based models

Port behavior
- At the level of the port - yards, containers, constituent packages of containers, etc
  - Port traffic controller, customs inspectors
- At the level of the body of water - transiting stretches of water (with this - lakes and islands, plus rivers and canals - we can model the entire world.)

Machine learning models
- outputs of agent-based models
- data on customs, ship traffic, etc
(classification of what ?)

Regression models





 (competition may be a tool to incentivize coordination. )
