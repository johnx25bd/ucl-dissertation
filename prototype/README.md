# Physical and informational security of smart containers

## Vision

We envision a decentralized global logistics network, in which transported units (i.e. containers) are autonomous, transiting the network much like packets of information do on the internet. This means that no specific firm needs to retain custody of the container throughout its transit - instead, various players in the ecosystem can assume custody of the self sovereign object, responsive to changes in the complex system. We suspect that enormous gains in the efficiency and reliability of the global logistics network could be achieved by transitioning to this system. Crucially, we do not see this as a replacement of the existing system: current market leaders would still play a profitable role.

This vision is grounded in the observation that emergent informational architectures - blockchains as globally-accessible informational utilities - the need for cooperative organizations (i.e. firms) to provide the coordination services might be eclipsed by the adherence of players in a less-coordinated ecosystem to open protocols defining the schemas of the information required to shepherd a shipment through the logistics chain, along with the use of globally-accessible smart contract code to keep track of a shipment's meta-information.

However, crucial to this system is the assurance to the owners of the goods being shipped that the physical and informational contents of the container cannot be accessed by unauthorized entities.

Here we outline such a system. This is conceptualized and described as it would be implemented on the Ethereum blockchain, but is general enough to be adapted to other public, or private blockchain implementations.

## Physical security

First: containers must only be accessible to authorized actors. We propose several mechanisms to ensure the security of the contents of the container is maintained, as well as possible responses to the eventuality that container integrity is compromised.

First, and most obviously, accessing the contents of the container - by opening the door - could be controlled by a smart lock and biometric identification system. Access rights could be defined within the smart contract instance probably a `Container` contract, rather than `Shipment`. (More on smart contract design later.)

Critically, a container will need to control its own externally-owned account (EOA). This means that it will need its own private key, from which to derive a public key and wallet address. **IF** we can be confident that transactions signed by that private key did indeed originate onboard the container, and that the on-board processors execute code in a secure or uncompromised environment, we believe the system described is possible.

The reason that a smart container needs its own private key is because it will need to invoke smart contract functions, and use the returned values as inputs into algorithms executed within the container's computing environment. A simple implementation of this would include a mapping of `containerID`s to `address`es authorized to access - unlock - the case. (Similarly, a `struct` containing information about the time and place in which that address has the right to access contents could be defined.) We imagine an authorized entity attempting to gain access require the container to invoke a `view` function, checking if they are authorized, and prove to the container that they are who they say they are, likely by transmitting a piece of data signed by that authorized entity's private key. A simple `verify()` function invocation on the container would provide necessary data for the container to open, or not.

It is very easy to see this extended to multisignature access controls (imagining highly sensitive shipments such as weapons / munitions, dual-use goods, high value objects like art or jewelry, or pharmaceuticals). Further, extending the system to include biometric identification hardware on board the container - camera, fingerprint scan, voice recognition - including, perhaps, an on-chain registry where a container could check to ensure that the person submitting credentials through these scanners is authorized. (Clearly some security scheme would need to be adhered to, as this biometric information may be highly sensitive.)

The key take-away: to write the logic required to gain access to these smart containers directly onto the blockchain, to improve system security. Again, this assumes appropriate management of private keys, as well as reliable hardware (locks) - areas worth further investigation, but assumptions worth making in investigating the feasibility of the concept.


      <!-- |=====================================|
      |                EVM                  |
      |                                     |
      |                                     |
      | hasAccess(containerId, address)     |
      |  |--[True]|[False]-|                |
      |  v                 ^                |
      |  |                 |                |
      |==|=================|================|
         |-----------|     | << Checks if actor
                     v     ^    has access rights
|====================|=====|=|
|   Smart Container  |    [|]|--------<--------| << Sends access request,
|                    |       |                 |    signed by private key
|                    |-{open}|       |=========|====|
|                    |-{not} |       |  Authorized  |
|============================|       |    actor     |
                                     |==============| -->


## Information security

Improving situational awareness for stakeholders in the global transport supply chain would create numerous opportunities to improve system efficiency, resulting in commercial and environmental benefits ([UN CEFACT Smart Containers White Paper 2019](http://www.unece.org/fileadmin/DAM/cefact/GuidanceMaterials/WhitePaperSmartContainers.pdf)). A transparent and reliable mechanism to ensure the security of the smart container's meta-information is a requirement if such a smart logistics network is to be implemented.

Ethical reasons

Legal reasons

Commercial reasons

Capturing the value contained in sensor data is the primary incentive for participants in the logistics network ecosystem to invest in smart container technology. Unless regulated to do so, firms compelled by a profit motive necessarily need to see the business case for such an investment. Improvements to operational efficiency may offer enough justification to forward-thinking or large actors in the space, but a clearer path to adoption would be to create new revenue opportunities, rather than increase profits by reducing costs. The clearest revenue opportunity created by investing in smart container technology is to monetize the data collected by these sensors.

This opportunity is constrained, however, by technical and business realities. Edge sensors are often highly constrained by intermittent or constrained bandwidth, and by limitations to computing capacity due to storage / memory or energy consumption. Further, datasets increase in value in a non-linear way with scale, provided accuracy (or at least precision). Potential customers of data will be willing to pay much more for datasets covering greater spatial and temporal extents, and of higher resolution.

This final point is the strongest case for the establishment of and adherence to an industry-wide protocol (as referenced in the UN CEFACT white paper). By ensuring that data collected - even from a single sensor at a single point in spacetime - is interoperable with data collected by competing entities will improve the value of everyone's data.
