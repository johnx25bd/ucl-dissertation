pragma solidity ^0.5.10;


contract DeviceRegistry {
    enum PermissionLevel {Full, Some, Little, None}
    enum DeviceType {a, b, c, na}

    struct Device {
        address deviceAddr;
        address ownerAddr;
        bool registered;
        bool destroyed;
        // DeviceType dType;
        mapping (address => DevicePermissions) userPermissions;
    }

    struct DevicePermissions {
        PermissionLevel permission;
        uint maxDistance;
        int[2][2] withinBBox; // <-- what about multiple bboxes?
    }

  mapping (address => Device) deviceOwners; // maps device address to owner address?

    function checkRegistry (
            address _deviceAddr)
        public view returns (address deviceAddr_,
            address ownerAddr_,
            bool registered_,
            bool destroyed_) {

        return (deviceOwners[_deviceAddr].deviceAddr,
            deviceOwners[_deviceAddr].ownerAddr,
            deviceOwners[_deviceAddr].registered,
            deviceOwners[_deviceAddr].destroyed);
    }

  function registerOwnership (
    address _deviceAddr,
    address _ownerAddr
    ) public {
      // require device is not already registered
        require(deviceOwners[_deviceAddr].registered != true);

        Device memory newDevice = Device(_deviceAddr, _ownerAddr, true, false);

        deviceOwners[_deviceAddr] = newDevice;
    }

  function reassignOwnership (
    address _deviceAddr,
    address _newOwner ) public {

    require(deviceOwners[_deviceAddr].ownerAddr == msg.sender, "Only owner can re-assign ownership.");
    deviceOwners[_deviceAddr].ownerAddr = _newOwner;
  }

  function destroyDevice (
    address _deviceAddr
    ) public {
      require(deviceOwners[_deviceAddr].ownerAddr == msg.sender, "Only device owner can destroy device.");

      deviceOwners[_deviceAddr].destroyed = true;

    }
}
