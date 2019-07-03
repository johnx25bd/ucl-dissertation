# A DAO for access control

A decentralized governance system for accessing information captured by and contained on self-sovereign machines.

## Entity types

### Edge device

An Edge device is one that contains an empirical sensor, here defined as a sensor that detects some environmental condition, recording that condition in a digital format. Examples include:

- Temperature;
- Accelerometer data, including tilt and impact;
- Moisture or humidity;
- Light, including multispectral sensors (i.e. cameras);
- Distance to other sensors. This enables triangulation of location;
- Sound, including intensity and frequency.

Trusted Platform Module.

Optional identity, pseudonymity or anonymity.

### Gateway

An [IoT gateway](https://www.globalsign.com/en/blog/what-is-an-iot-gateway-device/) is a device that serves as an intermediary between edge devices, which are often resource-constrained (limited in its capability to compute and transceive data by energy constraints), and the wider internet. These "devices offer local processing and storage solutions", and, for the purposes of our proof of concept, have a stable power source and internet connection.

### Cloud server

Any private computing environment that is not the edge device, gateway or EVM will be considered a "cloud server". In this context, cloud servers will typically occupy the Requestor role, or provide proxy computational services for tasks too intensive to execute at or near the edge, or on the EVM.

### Ethereum Virtual Machine (EVM)

Core logic and critical data will be stored on the Ethereum blockchain, invokable by participants controlling wallet addresses (i.e. in possession of private keys). The primary function of smart contracts deployed to the EVM is to manage the decentralized public key infrastructure (DPKI) that we investigate.

### Proxy Re-encryption Network  

To both enable end-to-end encryption of sensor data and to address resource constraints inherent to edge computing, a proxy re-encryption service will be employed. In this scheme, semi-trusted proxy node re-encrypt data with a Requestor's public key *without revealing the plaintext* to the proxy node.

### Human agents

Human agents interact with the system through connected devices (PCs and smartphones) with private keys and software enabling them to generate and transmit valid transactions to invoke smart contract functions.



## Actions

1. Register edge device.

Upon manufacture, edge devices must be registered on the DPKI smart contract DeviceRegistry. Perhaps manufacturing company owns the device initially, then upon purchase ownership is transferred to purchaser's wallet address

```
contract DeviceRegistry {
  mapping (address => address) deviceOwners; // maps device address to owner address?

  function registerOwnership (
    address deviceAddress,
    address ownerAddress
    ) public {
      // require device is not already registered

      deviceOwners[deviceAddress] = ownerAddress;
    }

  function reassignOwnership (
    address deviceAddress,
    address newOwner ) public {

    // Only owner can re-assign ownership
    require(deviceOwners[deviceAddress] == msg.sender);
    // Update deviceOwners mapping
    deviceOwners[deviceAddress] = newOwner;
  }

}
```

2. Grant permissions.

For the proof of concept, device owners can grant permissions to wallet addresses as they wish. More advanced implementations may require contract logic to ensure permission is granted to certain actors in certain contexts - for example, to customs authorities while a device is in an inspection facility, or to nearby devices.

```
contract Device {

  enum DeviceTypes { Container, Ship, Human }

  struct permissionParams {
    address requestorAddress;
    // other parameters including temporal, spatial, multisig, etc?
  }

  mapping (address => permissionParams) accessTable;

  function hasAccess ( address _requestorAddr, int[3] _requestorLocation address _deviceAddr, int[3] _deviceLocation, ) public returns (bool) {
    // check
    if (accessTable[_requestor] == permissionParams) {
      return true;
    } else { return false; }
  }
}
```

3. Request access

Device receives access request. Authenticates request (avoid replay attacks?). Submits transaction to EVM detecting whether requestor has access (or what they have access to) based on identity (address), location (bounding box, bounding cube, proximity), type.

Depending on response from EVM invocation, device may send data to requestor or return permission denied message. 
